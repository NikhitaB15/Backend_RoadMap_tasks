#!/usr/bin/env python3
import sys
import json
import urllib.request
import urllib.error

def fetch_github_activity(username):
    """
    Fetch GitHub user activity from the GitHub API
    """
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8'))  # Debugging line to print raw data
            print(f"Fetched data for user: {username}")
            return json.loads(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found on GitHub.")
        else:
            print(f"Error: Failed to fetch data from GitHub (HTTP {e.code}).")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error: Could not connect to GitHub API. {e.reason}")
        sys.exit(1)

def format_activity(events):
    """
    Format GitHub events into human-readable strings
    """
    formatted_events = []
    for event in events:
        event_type = event['type']
        repo = event['repo']['name']
        
        if event_type == 'PushEvent':
            commit_count = len(event['payload']['commits'])
            action = f"Pushed {commit_count} commit{'s' if commit_count != 1 else ''} to"
        elif event_type == 'IssuesEvent':
            action = event['payload']['action'].capitalize() + " an issue in"
        elif event_type == 'PullRequestEvent':
            action = event['payload']['action'].capitalize() + " a pull request in"
        elif event_type == 'WatchEvent':
            action = "Starred"
        elif event_type == 'CreateEvent':
            action = "Created a " + event['payload']['ref_type'] + " in"
        elif event_type == 'DeleteEvent':
            action = "Deleted a " + event['payload']['ref_type'] + " from"
        elif event_type == 'ForkEvent':
            action = "Forked"
        elif event_type == 'IssueCommentEvent':
            action = "Commented on an issue in"
        elif event_type == 'PullRequestReviewEvent':
            action = "Reviewed a pull request in"
        elif event_type == 'PullRequestReviewCommentEvent':
            action = "Commented on a pull request review in"
        elif event_type == 'CommitCommentEvent':
            action = "Commented on a commit in"
        else:
            action = f"Performed {event_type} on"
        
        formatted_events.append(f"- {action} {repo}")
    return formatted_events

def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    print(f"Fetching recent activity for GitHub user: {username}")
    
    events = fetch_github_activity(username)
    formatted_events = format_activity(events)
    
    if not formatted_events:
        print("No recent activity found for this user.")
    else:
        print("\nRecent activity:")
        for event in formatted_events[:10]:  # Limit to 10 most recent events
            print(event)

if __name__ == "__main__":
    main()