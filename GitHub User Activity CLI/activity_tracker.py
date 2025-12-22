import requests
import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
        print("======================================================")
        print("=                                                    =")
        print("=            GITHUB USER ACTIVITY CHECKER            =")
        print("=                                                    =")
        print("======================================================")

# Main
headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

message = "\nA simple command line interface (CLI) to fetch the recent activity of a GitHub user."

while True:
    clear_screen()
    print(message)
    username = input("\nProvide the GitHub user name whose activities you want to check.\n\n> github-activity ")
    print("\nChecking if user name provided is valid...\n")
    response = requests.get(f'https://api.github.com/users/{username}/events', headers)

    if response.status_code == 200:
        events = response.json()
        if len(events) == 0:
            print("This user has no recent events.")
            break
        print(f"User {username}'s recent events: ")
        for event in events:
            if event["type"] == "CommitCommentEvent":
                pass
            elif event["type"] == "CreateEvent":
                pass
            elif event["type"] == "DeleteEvent":
                pass
            elif event["type"] == "DiscussionEvent":
                pass
            elif event["type"] == "ForkEvent":
                pass
            elif event["type"] == "GollumEvent":
                pass
            elif event["type"] == "IssueCommentEvent":
                pass
            elif event["type"] == "IssuesEvent":
                pass
            elif event["type"] == "MemberEvent":
                pass
            elif event["type"] == "PublicEvent":
                pass
            elif event["type"] == "PullRequestEvent":
                pass
            elif event["type"] == "PullRequestReviewEvent":
                pass
            elif event["type"] == "PullRequestReviewCommentEvent":
                pass
            elif event["type"] == "PushEvent":
                pass
            elif event["type"] == "ReleaseEvent":
                pass
            elif event["type"] == "WatchEvent":
                pass
            else:
                print("Event not identified.")
    else:
        message = "\nUser not found. Try again."