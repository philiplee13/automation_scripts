import json
import requests
import os
import ast

github_user = str(input("Please enter in your github handle: "))
github_api = os.environ.get("GITHUB_API")

view = True
url = "https://api.github.com/user/repos"
r = requests.Session()
r.auth = (github_user,github_api)

while view:
    # have option for user to choose task
    option = int(input("""Which of the options would you like to do?
    1. View all Repos?
    2. Create a new repo?
    3. Push files to a certain repo
    """))
    # option 1 - view all current repos 
    if option == 1:
        repos = json.loads(r.get(url).text)
        for repo in repos:
            print(repo["name"])
        do_more = str(input("Would you like to do something else? Y/N")).upper()
        if do_more == "Y":
            view = True
        else:
            view = False
    # option 2 - create a new repo
    elif option == 2:
        str_data = (input("""
        Please enter in the following information for your repo in the order provided
        Name,Description
        """))
        boolean_data = input("""
        Please enter True or False if you need the following
        README,private repo
        """)
        boolean_data = boolean_data.split(",")
        data = {
            "name":str_data.split(",")[0],
            "description":str_data.split(",")[1],
            "auto_init":ast.literal_eval(boolean_data[0]),
            "private":ast.literal_eval(boolean_data[1])
            }
        print(data)
        r.post(url,json.dumps(data))
        do_more = str(input("Would you like to do something else? Y/N")).upper()
        if do_more == "Y":
            view = True
        else:
            view = False