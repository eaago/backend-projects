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
    username = input("\nProvide the GitHub user name whose activities you want to check. Enter 'end' to close.\n\n> github-activity ")
    if username == "end":  # This does make it you can't search the user named 'end'. As of 12/25/2025, it has no recent events.
        print("\nClosing activity tracker. Goodbye.")
        break
    print("\nChecking if user name provided is valid...\n")
    response = requests.get(f'https://api.github.com/users/{username}/events', headers)

    if response.status_code == 200:
        events = response.json()
        if len(events) == 0:
            message = "This user has no recent events."
        else:
            print(f"User {username}'s recent events:\n")
            for event in events:
                if event["type"] == "CommitCommentEvent":
                    print(f"Created a commit comment event to {event["repo"]["name"]}")
                elif event["type"] == "CreateEvent":
                    print(f"Created a Git branch or tag at {event["repo"]["name"]}")
                elif event["type"] == "DeleteEvent":
                    print(f"Deleted a Git branch or tag at {event["repo"]["name"]}")
                elif event["type"] == "DiscussionEvent":
                    print(f"Created a discussion at {event["repo"]["name"]}")
                elif event["type"] == "ForkEvent":
                    print(f"Forked the repository {event["repo"]["name"]}")
                elif event["type"] == "GollumEvent":
                    print(f"Created or updated a wiki page at {event["repo"]["name"]}")
                elif event["type"] == "IssueCommentEvent":
                    action = event["payload"]["action"].capitalize()
                    print(f"{action} an issue or pull request comment at {event["repo"]["name"]}")
                elif event["type"] == "IssuesEvent":
                    action = event["payload"]["action"].capitalize()
                    print(f"{action} an issue at {event["repo"]["name"]}")
                elif event["type"] == "MemberEvent":
                    action = event["payload"]["action"].capitalize()
                    print(f"{action} repository collaborators at {event["repo"]["name"]}")
                elif event["type"] == "PublicEvent":
                    print(f"Private repository {event["repo"]["name"]} was made public")
                elif event["type"] == "PullRequestEvent":
                    action = event["payload"]["action"].capitalize()
                    print(f"{action} pull request at {event["repo"]["name"]}")
                elif event["type"] == "PullRequestReviewEvent":
                    action = event["payload"]["action"].capitalize()
                    print(f"{action} pull request review at {event["repo"]["name"]}")
                elif event["type"] == "PullRequestReviewCommentEvent":
                    action = event["payload"]["action"].capitalize()
                    print(f"{action} pull request review comment at {event["repo"]["name"]}")
                elif event["type"] == "PushEvent":
                    print(f"Pushed a commit to {event["repo"]["name"]}")
                elif event["type"] == "ReleaseEvent":
                    action = event["payload"]["action"].capitalize()
                    print(f"{action} release at {event["repo"]["name"]}")
                elif event["type"] == "WatchEvent":
                    print(f"Starred {event["repo"]["name"]}")
                else:
                    print("Event not identified.")
            while True:
                choice = input("\n> Would you like to view another user's events? (Y/N): ")
                if choice == "Y":
                    break
                elif choice == "N":
                    break
                else:
                    print("Input invalid. Please try again.")
                    
            if choice == "Y":
                continue
            elif choice == "N":
                print("\nClosing activity tracker. Goodbye.")
                break

    else:
        message = "\nUser not found. Try again."