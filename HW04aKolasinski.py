#Jakub Kolasinski
#HW 04a


import requests
import json




def reposcommits(github):
    count = dict()
    url = "https://api.github.com/users/"+github+"/repos"
    repository = requests.get(url)
    repos = repository.json()
    
    for repo in repos:
        commiturl = "https://api.github.com/repos/"+github+"/"+repo['name']+"/commits"
        get = requests.get(commiturl)
        commit = get.json()
        count[repo['name']] = len(commit)
    return count




def main():
    while True:
        try:
            github = input("Input GitHub username to get a repository list and commit count: ")
            count = reposcommits(github)
            for repositories,commits in count.items():
                print("Repository:", repositories, "Number of commits:", commits)   
        
        except TypeError:
            print("Username entered is not valid") 
        return
        
    








if __name__ == "__main__":
    main()