import json
import requests
import os
import ast
import base64
github_user = str(input("Please enter in your github handle: "))
github_api = os.environ.get("GITHUB_API")

view = True
url = "https://api.github.com/user/repos"
r = requests.Session()
r.auth = (github_user,github_api)

# # push files to a certain repo
# # get a reference to the head 
# repo = "automation_scripts"
# path = "https://api.github.com/repos/philiplee13/automation_scripts/git/ref/heads/main"
# rget = r.get(path)
# head_reference = rget.json()
# # print(json.dumps(head_reference,indent=4))
# sha = head_reference["object"]["sha"]
# head_url = head_reference["object"]["url"]

# # # grab the commit the head points to
# rget2 = r.get(head_url)
# rget2_json = rget2.json()
# # print(json.dumps(rget2_json,indent=4))
# commit_sha = rget2_json["parents"][0]["sha"]
# tree_sha = rget2_json["tree"]["sha"]
# tree_url = rget2_json["tree"]["url"]

# # # post your new file to the server
# url = "https://api.github.com/repos/philiplee13/automation_scripts/git/blobs"
# filename="github_automate.py"
# base64content = base64.b64encode(open(filename,"rb").read())
# data = {
#     "message":"update",
#     "branch":"main",
#     "content":base64content.decode("utf-8"),
#     "sha":sha
#     }
# resp = requests.post(url,data=json.dumps(data),headers = {"Content-Type": "application/json", "Authorization": "token "+github_api})
# resp = json.loads(resp.text)
# resp_sha = resp["sha"]

# # create a tree containing your new file
# post_tree_url = "https://api.github.com/repos/philiplee13/automation_scripts/git/trees"
# data = {
#     # "base_tree": "",
#     "tree" : [
#     {
#     "path":"github_automate.py",
#     "mode":"100644",
#     "type":"blob",
#     "sha":resp_sha
#     }
# ]
# }
# tree_file = r.post(post_tree_url,data=json.dumps(data),headers = {"Content-Type": "application/json", "Authorization": "token "+github_api})
# tree_file = json.loads(tree_file.text)
# tree_file_sha = tree_file["sha"]

# # create a new commit
# commit_url = "https://api.github.com/repos/philiplee13/automation_scripts/git/commits"
# data = {
#     "message":"update through api",
#     "parents":[commit_sha],
#     "tree":tree_file_sha
# }
# commit_post = r.post(commit_url,data=json.dumps(data),headers = {"Content-Type": "application/json", "Authorization": "token "+github_api})
# commit_post = json.loads(commit_post.text)
# new_commit_sha = commit_post["sha"]

# # update head
# update_url = "https://api.github.com/repos/philiplee13/automation_scripts/git/refs/heads/main"
# data = {
#     "sha":new_commit_sha,
#     "force":True
# }
# update_post = r.patch(update_url,data=json.dumps(data),headers = {"Content-Type": "application/json", "Authorization": "token "+github_api})
# update_post = json.loads(update_post.text)
# print(json.dumps(update_post,indent=4))



# while view:
#     # have option for user to choose task
#     option = int(input("""Which of the options would you like to do?
#     1. View all Repos?
#     2. Create a new repo?
#     3. Push files to a certain repo
#     """))
#     # option 1 - view all current repos 
#     if option == 1:
#         repos = json.loads(r.get(url).text)
#         for repo in repos:
#             print(repo["name"])
#         do_more = str(input("Would you like to do something else? Y/N")).upper()
#         if do_more == "Y":
#             view = True
#         else:
#             view = False
#     # option 2 - create a new repo
#     elif option == 2:
#         str_data = (input("""
#         Please enter in the following information for your repo in the order provided
#         Name,Description
#         """))
#         boolean_data = input("""
#         Please enter True or False if you need the following
#         README,private repo
#         """)
#         boolean_data = boolean_data.split(",")
#         data = {
#             "name":str_data.split(",")[0],
#             "description":str_data.split(",")[1],
#             "auto_init":ast.literal_eval(boolean_data[0]),
#             "private":ast.literal_eval(boolean_data[1])
#             }
#         print(data)
#         r.post(url,json.dumps(data))
#         do_more = str(input("Would you like to do something else? Y/N")).upper()
#         if do_more == "Y":
#             view = True
#         else:
#             view = False
#     elif option == 3:
#         # push files to a certain repo
        
#         # get a reference to the head 
#         repo = "automation_scripts"
#         path = "https://api.github.com/repos/philiplee13/automation_scripts/git/ref/heads/main"
#         rget = r.get(path)
#         head_reference = rget.json()
#         # print(json.dumps(head_reference,indent=4))
#         sha = head_reference["object"]["sha"]
#         head_url = head_reference["object"]["url"]

#         # grab the commit the head points to
#         rget2 = r.get(head_url)
#         rget2_json = rget2.json()
#         # print(json.dumps(rget2_json,indent=4))
#         commit_sha = rget2_json["parents"][0]["sha"]
#         tree_sha = rget2_json["tree"]["sha"]
#         tree_url = rget2_json["tree"]["url"]

#         # # post your new file to the server
#         url = "https://api.github.com/repos/philiplee13/automation_scripts/git/blobs"
#         filename="github_automate.py"
#         base64content = base64.b64encode(open(filename,"rb").read())
#         data = {
#             "message":"update",
#             "branch":"main",
#             "content":base64content.decode("utf-8"),
#             "sha":sha
#             }
#         resp = requests.post(url,data=json.dumps(data),headers = {"Content-Type": "application/json", "Authorization": "token "+github_api})
#         resp = json.loads(resp.text)
#         resp_sha = resp["sha"]

#         # create a tree containing your new file
#         post_tree_url = "https://api.github.com/repos/philiplee13/automation_scripts/git/trees"
#         data = {
#             # "base_tree": "",
#             "tree" : [
#             {
#             "path":"github_automate.py",
#             "mode":"100644",
#             "type":"blob",
#             "sha":resp_sha
#             }
#         ]
#         }
#         tree_file = r.post(post_tree_url,data=json.dumps(data),headers = {"Content-Type": "application/json", "Authorization": "token "+github_api})
#         tree_file = json.loads(tree_file.text)
#         tree_file_sha = tree_file["sha"]

#         # create a new commit
#         commit_url = "https://api.github.com/repos/philiplee13/automation_scripts/git/commits"
#         data = {
#             "message":"update through api",
#             "parents":[commit_sha],
#             "tree":tree_file_sha
#         }
#         commit_post = r.post(commit_url,data=json.dumps(data),headers = {"Content-Type": "application/json", "Authorization": "token "+github_api})
#         commit_post = json.loads(commit_post.text)
#         new_commit_sha = commit_post["sha"]

#         # update head
#         update_url = "https://api.github.com/repos/philiplee13/automation_scripts/git/refs/heads/main"
#         data = {
#             "sha":new_commit_sha,
#             "force":True
#         }
#         update_post = r.patch(update_url,data=json.dumps(data),headers = {"Content-Type": "application/json", "Authorization": "token "+github_api})
#         update_post = json.loads(update_post.text)
#         print(json.dumps(update_post,indent=4))
#         do_more = str(input("Would you like to do something else? Y/N")).upper()
#         if do_more == "Y":
#             view = True
#         else:
#             view = False