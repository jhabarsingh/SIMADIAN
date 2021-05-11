import os
import sys
import json

def extract(filename):
	with open(filename, "r+") as file:
		districts = []
		data = file.read()
		data = json.loads(data).get("states")
		for state in data:
			for i in state.get("districts"):
				districts.append(i)
		
		with open("district.txt", "w+") as wfile:
			wfile.write(str(districts))
	

if __name__ =="__main__":
	filename = sys.argv[1]
	extract(filename)
