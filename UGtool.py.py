#!/usr/bin/python3
import os
from time import sleep
import subprocess

def adduser():
	menu = True
	while menu == True:
		os.system("clear")
		subprocess.call(["cat", "/etc/passwd"])
		print()
		ask = str(input("Input Name for create: "))
		sure = str(input("Are you sure to create the User? y/n 'main' for Main Menu: "))
		if sure == "main":
			print ("Going back to Main Menu")
			sleep(1)
			menu = False
		elif sure == "y" or sure == "Y":
			subprocess.call(["sudo", "useradd", "-m", "-k", "/etc/skel", "-s", "/usr/bin/bash", ask])
			print(ask, "created")
			sleep(1)
		elif sure == "n" or sure == "N":
			print("Aborting...")
			sleep(1)
		else:
			print("Wrong Input")
			sleep(1)

def deluser():
	menu = True
	while menu == True:
		os.system("clear")
		subprocess.call(["cat", "/etc/passwd"])
		print()
		ask = str(input("Input Name to delete: "))
		sure = str(input("Are you sure to delete the User? y/n 'main' for Main Menu: "))
		if sure == "main":
			print("Going back to Main Menu")
			sleep(1)
			menu = False
		elif sure == "y" or sure == "Y":
			subprocess.call(["sudo", "userdel", "-r", ask])
		elif sure == "n" or sure == "N":
			print("Aborting...")
			sleep(1)
		else:
			print("Wrong Input")
			sleep(1)

def addgroup():
	menu = True
	while menu == True:
		os.system("clear")
		subprocess.call(["cat", "/etc/group"])
		print()
		ask = str(input("Input Group to create: "))
		sure = str(input("Are you sure to create the Group? y/n 'main' for Main Menu: "))
		if sure == "main":
			print("Going back to Main Menu")
			sleep(1)
			menu = False
		elif sure == "y" or sure == "Y":
			subprocess.call(["sudo", "groupadd", ask])
		elif sure == "n" or sure == "N":
			print("Aborting...")
			sleep(1)
		else:
			print("Wrong Input")
			sleep(1)

def delgroup():
	menu = True
	while menu == True:
		os.system("clear")
		subprocess.call(["cat", "/etc/group"])
		print()
		ask = str(input("Input Group to delete: "))
		sure = str(input("Are you sure to delete the Group? y/n 'main' for Main Menu: "))
		if sure == "main":
			print("Going back to Main Menu")
			sleep(1)
			menu = False
		elif sure == "y" or sure == "Y":
			subprocess.call(["sudo", "groupdel", ask])
		elif sure == "n" or sure == "N":
			print("Aborting...")
			sleep(1)

def main():
	menu = True
	while menu == True:
		os.system("clear")
		print("Welcome to the User-Group-Manager Tool")
		print("1: Add User to System")
		print("2: Delete User from System")
		print("3: Add Group to your System")
		print("4: Delete Group from System")
		print("5: Exit")
		ask = int(input("Choose: "))
		if ask == 1:
			adduser()
		elif ask == 2:
			deluser()
		elif ask == 3:
			addgroup()
		elif ask == 4:
			delgroup()
		elif ask == 5:
			print("Thanks for using User-Group-Manager")
			sleep(1)
			menu = False
main()
