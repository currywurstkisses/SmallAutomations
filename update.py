# This file was created to make automatic updates to a hosted site.
# The site is currently static, and while it changes to a more dymanic setup
# This should help apply any changes needed overnight.
# It will probably be called as a cronjob each night

#Imports
import os
import sys
import base64
import hashlib
import checksumdir
import zipfile
import logging

def refreshDirectory():
	#This function will return the hash of the latest version
	#Set the variables for what to get and where to put it
	where = "/Home/the/directory"
	pull = "git pull files.git"
	sshKey = "ssh stuff"
	#Will Need to add decrypted base64 ssh, write it in local file
	os.system("ssh data here")
	os.chdir(where)
	os.system(pull)

def getFilePaths(directory):
	filePaths = []

	for root, directories, files, in os.walk(directory):
		for filename, in files:
			filePath = os.path.join(root, filename)
			filePaths.append(filePath)

	return filePaths 

def getLatestHash():
	#This function will get the newest hash
	directory = "thedirectory"
	newHash = dirhash(directory, 'sha1')

	#Directory needs to be zipped so hashing is easier
	zip_file = zipfile.ZipFile(directory + '.zip', 'w')
	filePaths = retrieve_file_paths(directory)
	with zip_file:
		for file in filePaths:
			zip_file.write(file)


	return newHash


def getPreviousHash():
	#This function will read previous hash from a file
	#Open file here
	fileGet = open ('hashes.txt', 'r')
	lines = fileGet.readlines()
	fileGet.close()

	previousHsah = lines[-1]

	return previousHash


def updateHashFile():
	# This function will update the hash file when after its been updated.
	# Set the file location
	theFile = "hashes.txt"

	#Append the new hash to the file

def ftpUpdate():


def main():
	#Call all functions here
	refreshDirectory()
	newHashValue = getNewHash()
	oldHashValue = getPreviousHash()

	if(newHashValue != oldHashValue):
		ftpUpdate()
		updateHashFile()
	else
		exit()

if __name__ == '__main__':
	main()
