import os
from git.repo.base import Repo
import pathlib
import pip



Repo.clone_from("https://github.com/sakshamsahu007/DevOps.git", "H:\\Download_GIT")

file = pathlib.Path('requirements.txt')

if file.exists():
    print('File exists and installing...')
    #os.system('pip install -r requirements.txt')
    pip.main(['install', '-t', 'H:\\Download_GIT', '-r', 'requirements.txt'])














'''
import urllib.request

url = "https://github.com/sakshamsahu007/DevOps.git"
print ("download start!")
filename, headers = urllib.request.urlretrieve(url, filename="H:\\Download_GIT")
print ("download complete!")
print ("download file location: ", filename)
print ("download headers: ", headers)
'''