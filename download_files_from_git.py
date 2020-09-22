import os
from git.repo.base import Repo


Repo.clone_from("https://github.com/sakshamsahu007/DevOps.git", "H:\\Download_GIT")

pip install -r requirements.txt














'''
import urllib.request

url = "https://github.com/sakshamsahu007/DevOps.git"
print ("download start!")
filename, headers = urllib.request.urlretrieve(url, filename="H:\\Download_GIT")
print ("download complete!")
print ("download file location: ", filename)
print ("download headers: ", headers)
'''