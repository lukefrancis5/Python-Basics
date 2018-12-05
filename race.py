# gives the place ea racer came in
# used dictionary for cleaner code

def choice_to_number(choice):
    race_dict = {'Usain': 1, 'Luke': 2, 'Mike': 3}
    return race_dict[choice]

def number_to_choice(number):
    race_dict = {1: 'Usain', 2:'Luke', 3: 'Mike'}
    return race_dict[number]



# print(choice_to_number('Luke'))

print(number_to_choice(3))
