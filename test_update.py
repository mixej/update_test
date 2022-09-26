#!/usr/bin/python3
#сравнение текущего номера версии на гитхабе с последним сохраненным в фаил
import os
import subprocess

FILENAME = 'update_list.txt'


def get_new_ver():
	new_ver = subprocess.run(["git", "log", "--pretty=format:%s", "-1"], stdout=subprocess.PIPE, text=True, encoding='utf-8' )
	return str(new_ver.stdout)
	
def get_old_ver():
	with open(FILENAME,'r') as file:
		for line in file:
			old_ver = line
			return str(old_ver)	

def update_file_version(new_ver):
	with open(FILENAME,'w') as file:
		file.write(new_ver)		

def update_version(): 	
	old_version = get_old_ver()
	new_version = get_new_ver()
	
	if new_version == old_version:
		print("no update")
		
	else:
		print("can update to: ", new_version, "from: ", old_version)
		answer = input("Обновляемся? Yes or No: ")
		if answer == "Yes":
			update_file_version()
			print("successful")
		
		
if __name__ == '__main__':
	update_version()

	
	
