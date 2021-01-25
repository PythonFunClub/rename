import os

folder = [File path]

files = []
for file in os.listdir(folder):
	files.append(os.path.join(folder,file))
	
for file in files:
	newPath = file.replace("","")
	os.rename(file,newPath)