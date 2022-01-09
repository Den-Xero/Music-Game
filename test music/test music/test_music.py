import random
import csv
from Login import login
print("Top 5 scores:")
with open("leaderboard.csv") as readfile:
  readCSV1 = csv.reader(readfile, delimiter=",")
  for row in readCSV1:
    print(row)
  user = input("Enter user name: ")
  z = True
  while z:
    if (len(user)<= 0):
      user = input("Enter your user name plz: ")
    else:
     z = False
     break 
  print("Loging you in", user)
  responces = ""
  while responces != "yes": responces = input("welcome " + user + " are u ready to play? ")
  from Game import game#calls for the subroutine game form the module Game to run#
  from Game import score#calls for the variable score to be imported in form the module Game#
r = csv.reader(open('leaderboard.csv'))
lines = list(r)
if score > int(lines[0][1]):	
	lines[0][1] = score
	lines[0][0] = user
	writer = csv.writer(open('leaderboard.csv', 'w'))
	writer.writerows(lines)
elif score > int(lines[2][1]):	
	lines[2][1] = score
	lines[2][0] = user
	writer = csv.writer(open('leaderboard.csv', 'w'))
	writer.writerows(lines)
elif score > int(lines[6][1]):	
	lines[4][1] = score
	lines[4][0] = user
	writer = csv.writer(open('leaderboard.csv', 'w'))
	writer.writerows(lines)
elif score > int(lines[8][1]):	
	lines[6][1] = score
	lines[6][0] = user
	writer = csv.writer(open('leaderboard.csv', 'w'))
	writer.writerows(lines)
elif score > int(lines[8][1]):	
	lines[8][1] = score
	lines[8][0] = user
	writer = csv.writer(open('leaderboard.csv', 'w'))
	writer.writerows(lines)



