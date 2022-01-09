def login():
        password = input("Enter password:")
        if password == "password":
          print("Access Granted")
        else:
          print("Access Denied")
          login()
login()