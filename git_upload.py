from github import Github
import auth

if __name__ == "__main__":
    """
    Using properties from hidden auth.py environment 
    to authorize github by tokens and repository to work on.
    Push file from 'data_path' to 'file_position' in auth.REPO_PATH
    """
    # 'g' is an instance to connect to GitHubAPI
    g = Github(auth.token)   
    file_position= 'ECU_Requirement.rst'
    data_path = 'output/ECU_Req.rst'
    repo = g.get_repo(auth.REPO_PATH)

    branch_name = 'output' # You need to create a branch in order to make the following code work. 

    with open(data_path,'r') as f:    
        data = f.read()        
        try: 
            """
            Try to delete file_position if it exists
            """
            repo.get_contents(file_position,branch_name)
            temp_content = repo.get_contents(file_position,branch_name)
            repo.delete_file(file_position,message='Sound fun',branch=branch_name,sha = temp_content.sha)
        except:
            pass
        """
        Create file anyway
        """
        repo.create_file(file_position,branch=branch_name,message=file_position,content=f.read())
    f.close()