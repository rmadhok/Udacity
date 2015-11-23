import os

def rename_files():
	#1 - get file names from folder
	file_list = os.listdir("/Users/rmadhok/Documents/MOOC/Udacity/Python/files/prank/")
	print(file_list)
	saved_path = os.getcwd()
	print("Current path is "+saved_path)
	os.chdir("/Users/rmadhok/Documents/MOOC/Udacity/Python/files/prank/")
		#2 - for each file name, rename file
	for file_name in file_list: 
		print("Old Name - "+file_name)
		print("New Name - "+file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
		
rename_files()