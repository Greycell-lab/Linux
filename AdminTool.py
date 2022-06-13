#!/usr/bin/python3
import subprocess
import os
from time import sleep

def Useradd():
	menu = True
	while menu == True:
		os.system("clear")
		print("Welcome to the Useradd Script!")
		sleep(1)
		name = str(input("Username: "))
		if name == "q":
			menu = False
		else:
			fullname = str(input("Full Name: "))
			subprocess.call(["sudo", "useradd", name, "-c", fullname, "-m"])
			ask = input("More? y/n")
			menu1 = True
			while menu1 == True:
				if ask == "y" or ask == "Y":
					print("OK!")
					sleep(1)
					menu1 = False
				elif ask == "n" or ask == "N":
					print("Bye Bye!")
					sleep(1)
					os.system("clear")
					menu1 = False
					menu = False
				else:
					print("Wrong Input!")

def Directory():
	menu = True
	while menu == True:
		os.system("clear")
		dir = input("Directory Name: ")
		if dir == "q":
			menu = False
		else:
			subprocess.call(["mkdir", "-p", dir])
			print(dir, "created!")
			sleep(1)

def Userdel():
	menu = True
	while menu == True:
		os.system("clear")
		subprocess.call(["cat", "/etc/passwd"])
		name = str(input("Username: "))
		subprocess.call(["sudo", "userdel", name])
		if name == "q":
			menu = False

def Remove():
	menu = True
	while menu == True:
		os.system("clear")
		subprocess.call(["ls", "-l", "--color=auto"])
		ask = str(input("Input File or Directory: "))
		subprocess.call(["rm", "-ri", ask])
		print(ask, "got deleted!")
		if ask == "q":
			menu = False 

def Main():
	menu = True
	while menu == True:
		os.system("clear")
		print(" __________ ")
		print("|1: Useradd|")
		print("|2: Mkdir  |")
		print("|3: Userdel|")
		print("|4: Remove |")
		print("|5: Quit   |")
		print("|__________|")
		ask = int(input("   Choose: "))
		if ask == 1:
			Useradd()
		elif ask == 2:
			Directory()
		elif ask == 3:
			Userdel()
		elif ask == 4:
			Remove()
		elif ask == 5:
			print("Bye!")
			menu = False
		else:
			print("Wrong Input")

Main()
