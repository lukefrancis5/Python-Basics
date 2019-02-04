# program asks user for age and loops through until
# value of 5 hits zero(number of tickets)

films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
    }

choice = input("What film would you like to watch?:").strip().title()

while True:
    if choice in films:
        age = int(input("How old are you?: ").strip())

        # Check users age
        
        if age >= films[choice][0]:
            # Check enough seats

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
                
            else:
                print("Sorry we are sold out")
        else:
            print("You are too young to see that film")
    else:
        print("We don't have that film...")
