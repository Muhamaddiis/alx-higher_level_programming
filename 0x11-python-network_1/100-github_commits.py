import urllib.request
import json
import sys

def list_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            commits = json.loads(data)
            for commit in commits[:10]:  # Get the 10 most recent commits
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
    except urllib.error.HTTPError as e:
        print(f"Error: Failed to retrieve commits. Status code: {e.code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
