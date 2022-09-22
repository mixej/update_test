#!/usr/bin/python3
# получение номера обновления
import os
import subprocess

FILENAME = 'update_list.txt'

def get_update_num()
	last_ver = subprocess.run(["git", "log", "--pretty=format:'%s'", "-1"], stdout=subprocess.PIPE, text=True, encoding='utf-8' )

	with open(FILENAME,'w') as file:
		file.write(last_ver.stdout + '\n')
	

#print("successful")	
