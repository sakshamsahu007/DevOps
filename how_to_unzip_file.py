import zipfile

with zipfile.ZipFile('C:\\Users\\Saksham Sahu\\Desktop\\Desktop Study Doc\\files.zip',"r") as zip_ref:
    zip_ref.extractall('C:\\Users\\Saksham Sahu\Desktop\\Desktop Study Doc\\unzipped')
    
print("Unzip Successful")