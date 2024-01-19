import requests
import base64

def upload_file_to_github(file_path, repo_owner, repo_name, branch, token):
    # Read the binary content of the file
    with open(file_path, 'rb') as file:
        file_content = base64.b64encode(file.read()).decode('utf-8')

    # API endpoint to create or update a file
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'

    # Create a commit message
    commit_message = f"Add {file_path}"

    # Create the data payload for the API request
    data = {
        "message": commit_message,
        "content": file_content,
        "branch": branch
    }

    # Add authentication token to headers
    headers = {
        'Authorization': f'Token {token}'
    }

    # Make the API request to create or update the file
    response = requests.put(url, json=data, headers=headers)

    # Check if the request was successful
    if response.status_code == 201:
        print(f"File '{file_path}' uploaded successfully.")
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")
        print(response.json())


# Set your GitHub repository details and authentication token
file_path_to_upload = 'C:/Users/Analyst07/Documents/datadna_january/poster.pptx'
github_repo_owner = 'hazimutalib'
github_repo_name = 'blood_donation'
github_branch = 'main'
github_token = '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'

# Upload the file
upload_file_to_github(file_path_to_upload, github_repo_owner, github_repo_name, github_branch, github_token)
