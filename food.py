favourite_foods = []

while True:
    print("Favourite Food Manager")
    print("1. Exit")
    print("2. Add a Food")
    print("3. Remove a Food")
    print("4. View All Favourite Foods")

    choice = input("Choose an option: ")

    if choice == '1':
        print("Thank you for using the food manager")
        break
    elif choice == '2':
        food = input("Enter Your Favourite Food Name: ")
        favourite_foods.append(food)
        print(f'{food} Added Successfully')
    elif choice == '3':
        food = input("Enter The Food Name To Remove: ")
        if food in favourite_foods:
            favourite_foods.remove(food)
            print(f'{food} Removed Successfully')
        else:
            print(f'{food} not found in the list')
    elif choice == '4':
        if favourite_foods:
            print("Your Favourite Foods")
            for index, food in enumerate(favourite_foods, start=1):
                print(f'{index}. {food}')
        else:
            print("Food list is empty or nothing added yet!")
    else:
        print("Invalid Choice")