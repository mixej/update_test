#!/usr/bin/python3
#сравнение текущего номера версии на гитхабе с последним сохраненным в фаил
import os
import subprocess
import update_num

FILENAME = 'update_list.txt'


def get_new_ver():
	new_ver = subprocess.run(["git", "log", "--pretty=format:%s", "-1"], stdout=subprocess.PIPE, text=True, encoding='utf-8' )
	return str(new_ver.stdout)
	
def get_old_ver():
	with open(FILENAME,'r') as file:
		for line in file:
			old_ver = line
			return str(old_ver)	

def update_file_version():
	with open(FILENAME,'w') as file:
		file.write(get_new_ver())		

def update_version(): 	
	old_version = get_old_ver()
	new_version = get_new_ver()	
	if new_version == old_version:
		print("no update")
	else:
		print("can update to: ", new_version)
		print("old_version ", old_version)
		print("new_version ", new_version)
		
if __name__ == '__main__':
	
	answer = input("Обновляемся?: ")
	if answer == "Yes" and new_version != old_version:
		update_version()
		update_file_version()
		print("successful")
	
	
	
	
	
	
	
	
	
	
	
	
