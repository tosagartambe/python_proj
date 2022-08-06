from github import Github
import json
import os
from dotenv import load_dotenv

load_dotenv('.env')
token = os.getenv("github_access_token")
g = Github(token)

file = open("issues.json", "r")
j_data = json.load(file)
repo = g.get_repo("tosagartambe/python_proj")

i = 0
for i in range(0,2):

    j_title = json.dumps(j_data[i]["title"])
    j_body = json.dumps(j_data[i]["body"])
    j_lables = (j_data[i]["lables"])

    repo.create_issue(title=j_title, body=j_body, labels=[j_lables],assignee="tosagartambe")
    
    print(j_title,j_body,j_lables)