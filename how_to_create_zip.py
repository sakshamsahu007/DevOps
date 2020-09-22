import zipfile

zf=zipfile.ZipFile('C:\\Users\\Saksham Sahu\\Desktop\\Desktop Study Doc\\files.zip','w',zipfile.ZIP_DEFLATED)

zf.write('C:\\Users\\Saksham Sahu\\Desktop\\Desktop Study Doc\\lambda_function.py')

#zf.write('H:\\Back End\\Lambda\\demo.py')
#zf.write('H:\\Back End\\Lambda\\demo.txt')

zf.close()

print('zip file created successfully')


