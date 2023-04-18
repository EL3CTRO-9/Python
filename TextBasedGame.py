# Sahil Shaikh
from typing import List

import time


# Defining the rooms dictionary
def main():
    rooms = {
        'EntryWay': {'East': 'Living Room'},
        'Living Room': {'North': 'Kitchen', 'East': 'BedRoom1', 'South': 'Store Room', 'item': 'Flash Light'},
        'Kitchen': {'South': 'Living Room', 'East': 'Safe Room', 'item': 'Cash'},
        'Store Room': {'North': 'Living Room', 'East': 'Garage', 'item': 'Key'},
        'Safe Room': {'West': 'Kitchen', 'item': 'Gold'},
        'Garage': {'West': 'Store Room', 'item': 'Car'},
        'BedRoom1': {'North': 'BedRoom2', 'West': 'Living Room', 'item': 'Safe Key'},
        'BedRoom2': {'South': 'BedRoom1', 'item': 'Guard Dog'},  # Boss Room
    }

    # defining function to show instructions/rules at the beginning of the game
    def show_instructions():
        # print a main menu and the commands
        print("Jewel Thief Text Game")
        print("Collect 6 items to win the game, or get mauled by the guard dog.")
        print("Move commands: South, North, East, West")
        print("Add to Inventory: add 'item name'")
        print("Best of luck!!")

    # Shows player status and item status. Shows player room, items in inventory and if item in the room is in inventory
    def user_status(current_room, inventory):
        print('\n-------------------------')
        print('You are in the {}'.format(current_room))
        if 'item' in rooms[current_room] and rooms[current_room]['item'] in inventory:
            print("You already have the item from this room {}".format(current_room))
        elif 'item' in rooms[current_room]:
            print("Do you want to add {} to your inventory?".format(rooms[current_room]['item']))
        # prints the items that are currently in the players inventory.
        print("Inventory:", inventory)
        print("-------------------------")

    # creates an empty list called inventory
    inventory: List[str] = []
    # gives "EntryWay" string to current_room variable
    current_room = "EntryWay"
    show_instructions()
    # while loop runs continuously until exited using user input or if conditions are met
    while True:
        # If player has all 6 items in his inventory then it displays the end message and breaks the while loop
        user_status(current_room, inventory)
        if len(inventory) == 6:
            print("Congratulations! You have collected all 6 items and won the game!")
            time.sleep(4)
            break
        print(inventory)
        command = input("Where do you want to go next?(type -add- to add an item to your inventory ")

        # if user input is not one of the valid inputs then it would print the following statement
        if command.lower() not in ["north", "south", "east", "west", "add", "exit"]:
            print("Not a valid command; Possible commands: North, South, East, West, Add, Exit")
            continue

        # if there isn't a room in the direction the player wants to go it lets them know.
        if command.lower() in ["north", "south", "east", "west"]:
            if command.capitalize() not in rooms[current_room]:
                print("You can't go in that direction!")
                continue

        # Changes current room variable according to user input by referencing it to the dictionary
        if command.lower() == "north":
            current_room = rooms[current_room].get("North", current_room)
        elif command.lower() == "south":
            current_room = rooms[current_room].get("South", current_room)
        elif command.lower() == "east":
            current_room = rooms[current_room].get("East", current_room)
        elif command.lower() == "west":
            current_room = rooms[current_room].get("West", current_room)
        # if user input is 'add' it checks if the entered item exists in the current room and adds it to inventory if it
        # does
        if command.lower() == "add":
            item = input("Enter the name of the item you want to add: ")
            if item.lower() == rooms[current_room].get("item", "").lower() and item not in inventory:
                inventory.append(item)
                print(f"{item} added to your inventory!")
            else:
                print(f"{item} is not present in the current room.")
        elif command.lower() == "exit":
            break
        # if the player enters BedRoom2 or Boss Room then it displays the following message and exits the game
        if current_room == "BedRoom2":
            print("You've reached the guard dog! Game Over. The game will be shutting down in a few seconds")
            # adds an 8 sec pause so the player has time to read the statement before it exits the program
            time.sleep(8)
            break


if __name__ == "__main__":
    main()
