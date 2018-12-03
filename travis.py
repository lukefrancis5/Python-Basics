# Travis asks user for name to see if they're on the list
# if they are it asks user if they want to be removed
# if they're not on the list the program asks if they would like to be added

known_users = ["Alice","Bob","Clair","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi ! My name is Travis")
    name = input("What is your name ?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ")

        if remove == "y":   
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway")
            
    else:
        print("Hmm I don't think I've met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print("No worries, see you around !")
