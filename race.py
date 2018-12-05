# gives the place ea racer came in 


def choice_to_number(choice):
    
    if choice == "Usain":
        return 1
    elif choice == "Luke":
        return 2
    elif choice == "Mike":
        return 3

def number_to_choice(number):
    
    if number == 1:
        print('Usain')
    elif number == 2:
        print('Luke')
    elif number == 3:
        print('Mike')

print(choice_to_number())

# print(number_to_choice(3))
