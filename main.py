cat_attributes = {
    "intelligence": 50,
    "energy": 20,
    "weight": 15,
    # change the inital values above
    }

intelligence = cat_attributes["intelligence"]
energy = cat_attributes["energy"]
weight = cat_attributes["weight"]

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name: ")
colour = input("Enter colour: ")
# ...

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Feed it 4. Put it to sleep 5.show stats:  ")

    if option == '1':
        cat_attributes['weight'] = cat_attributes['weight'] - 2
        cat_attributes['energy'] = cat_attributes['energy'] - 2
        cat_attributes['intelligence']= cat_attributes['intelligence']+ 1
    elif option == '2':
        cat_attributes['intelligence'] = cat_attributes['intelligence'] + 2
        cat_attributes['energy'] = cat_attributes['energy'] - 5
        cat_attributes['weight'] = cat_attributes['weight'] - 3
    elif option == '3':
        cat_attributes['weight'] = cat_attributes['weight'] + 3
        cat_attributes['energy'] = cat_attributes['energy'] + 4
    elif option =='4':
        cat_attributes['energy'] = cat_attributes['energy'] + 5
    elif option == '5':
        print('Your cats intelligence is' , cat_attributes['intelligence'])
        print('Your cats energy is' , cat_attributes['energy'])
        print('Your cats weight is' , cat_attributes['weight'])
    

    # finish off the if statements below
    if cat_attributes['energy'] < 5:
        print('Your cat is out of energy')
        break
    elif cat_attributes['weight']< 10:
        print('Your cat is underweight')
        break
    elif cat_attributes['intelligence']<10:
        print('Your cat is not intelligent')
   
    