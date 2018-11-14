from datetime import datetime  
from datetime import timedelta
import subprocess
from random import randint
import os.path

def string_to_date(datestring):
	return datetime.strptime(datestring, "%Y-%m-%d %H:%M").date()
def date_to_string(date):
	return date.strftime('%Y-%m-%d 00:00')

now = datetime.now()

if os.path.isfile("lastday"):
	f = open("lastday", "r")
	lastday = f.read()
	f.close()
else:
	lastday = date_to_string(now - timedelta(days=365))

processing_day = lastday
starting_day = processing_day
today = date_to_string(now)

count = 0
while today != processing_day:

	processing_day_date = string_to_date(starting_day) + timedelta(days=count)
	processing_day = date_to_string(processing_day_date)
	count = count + 1

	for commits in range(1, randint(0, 6)):
		f = open("random", "w")
		f.write(str(randint(0, 100000)))
		f.close()	

		subprocess.check_output(["git", "add", "."])
		subprocess.check_output(["git", "commit", "--date=format:iso8601:\"" + processing_day + "\"", "-m", "commit"])

		print("committing for day " + processing_day.split()[0])
	
f = open("lastday", "w")
f.write(processing_day)

subprocess.check_output(["git", "push"])

