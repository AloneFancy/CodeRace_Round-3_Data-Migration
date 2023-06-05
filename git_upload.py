from github import Github
import auth
# using an access token
g = Github(auth.token)

file_to_upload= 'ECU_Requirement.rst'
# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
print(g.get_user())