score = int("0")
def game():#declares that this is where the subroutine starts
  import csv#imports the premade module CSV which allows the programmer to use CSV files in their program
  import random#imports the premade module random which allows the programmer to use random elements in their program
  with open("songs.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    artists = []
    songs = []
    firstLs = []
    for row in readCSV:
      artist = row[0]
      song = row[1]
      firstL = row[2]
      artists.append(artist)
      songs.append(song)
      firstLs.append(firstL)
      x = random.randint(1,5)
    global score#makes score a global variable
    if x == 1:
      print("The artist is " + artists[0])
      print("The first letters of the song is " + firstLs[0])
      answer = input("what is the song ")
      if answer == songs[0]:
        print("correct")
        score = score + 3
        game()
      else:
        print("Incorrect plz try again")
        answer = input("what is the song ")
        if answer == songs[0]:
          print("correct")
          score = score + 1
          game()
        else:
          print("Incorrect, Game over!")
          print("Answer was ", songs[0])
          print("your score is: ")
          print(score)
    elif x == 2:
      print("The artist is " + artists[1])
      print("The first letters of the song is " + firstLs[1])
      answer = input("what is the song ")
      if answer == songs[1]:
        print("correct")
        score = score + 3
        game()
      else:
        print("Incorrect plz try again")
        answer = input("what is the song ")
        if answer == songs[1]:
          print("correct")
          score = score + 1
          game()
        else:
          print("Incorrect, Game over!")
          print("Answer was ", songs[1])
          print("your score is: ")
          print(score)
    elif x == 3:
      print("The artist is " + artists[2])
      print("The first letters of the song is " + firstLs[2])
      answer = input("what is the song ")
      if answer == songs[2]:
        print("correct")
        score = score + 3
        game()
      else:
        print("Incorrect plz try again")
        answer = input("what is the song ")
        if answer == songs[2]:
          print("correct")
          score = score + 1
          game()
        else:
          print("Incorrect, Game over!")
          print("Answer was ", songs[2])
          print("your score is: ")
          print(score)
    elif x == 4:
      print("The artist is " + artists[3])
      print("The first letters of the song is " + firstLs[3])
      answer = input("what is the song ")
      if answer == songs[3]:
        print("correct")
        score = score + 3
        game()
      else:
        print("Incorrect plz try again")
        answer = input("what is the song ")
        if answer == songs[3]:
          print("correct")
          score = score + 1
          game()
        else:
          print("Incorrect, Game over!")
          print("Answer was ", songs[3])
          print("your score is: ")
          print(score)
    elif x == 5:
      print("The artist is " + artists[4])
      print("The first letters of the song is " + firstLs[4])
      answer = input("what is the song ")
      if answer == songs[4]:
        print("correct")
        score = score + 3
        game()
      else:
        print("Incorrect plz try again")
        answer = input("what is the song ")
        if answer == songs[4]:
          print("correct")
          score = score + 1
          game()
        else:
          print("Incorrect, Game over!")
          print("Answer was ", songs[4])
          print("your score is: ")
          print(score)
game()