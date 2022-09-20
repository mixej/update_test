#!/usr/bin/python3
import os
import subprocess



FILENAME = 'update_list.txt'

#p = input("hello: ")

last_ver = subprocess.run(["git", "log", "--pretty=format:'%s'", "-1"], stdout=subprocess.PIPE, text=True, encoding='utf-8' )
#version = last_ver

with open(FILENAME,'a+') as file:
	source = file.readlines()
	b = []  # получаешь свои результаты
	s = ''.join(b) + '\n'
	source.insert(0, s)
	file.writelines(source)
	file.write(last_ver.stdout)
	
	
print("successful")	
