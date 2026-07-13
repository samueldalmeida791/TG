#!/usr/bin/env python3
"""Text Adventure Game - Explore a simple world."""

import random


# Game world
ROOMS = {
    "entrance": {
        "description": "You are at the entrance of a dark cave. A cold wind blows from within.",
        "exits": {"north": "hallway"},
        "items": ["torch"]
    },
    "hallway": {
        "description": "A long, narrow hallway with torches on the walls. The flickering light casts eerie shadows.",
        "exits": {"south": "entrance", "east": "treasure", "west": "armory"},
        "items": ["key"]
    },
    "treasure": {
        "description": "A room filled with gold and jewels! But there's a locked chest in the corner.",
        "exits": {"west": "hallway"},
        "items": ["gold"],
        "locked": True
    },
    "armory": {
        "description": "A dusty armory with rusted weapons lining the walls.",
        "exits": {"east": "hallway", "north": "dungeon"},
        "items": ["sword"]
    },
    "dungeon": {
        "description": "A dark dungeon. You hear strange noises in the distance.",
        "exits": {"south": "armory"},
        "items": ["shield"],
        "enemy": "goblin"
    }
}


def main():
    print("\n" + "=" * 50)
    print("TEXT ADVENTURE".center(50))
    print("=" * 50)
    print("\nCommands: go [direction], get [item], use [item], look, inventory, quit")
    
    current_room = "entrance"
    inventory = []
    
    while True:
        # Display current room
        room = ROOMS[current_room]
        print("\n" + "=" * 50)
        print(room["description"])
        
        # Show exits
        exits = list(room["exits"].keys())
        print(f"Exits: {', '.join(exits)}")
        
        # Show items
        if room["items"]:
            print(f"Items: {', '.join(room['items'])}")
        
        # Show if room is locked
        if room.get("locked", False):
            print("(This room is locked!)")
        
        # Show enemy
        if room.get("enemy"):
            print(f"There is a {room['enemy']} here!")
        
        # Get command
        command = input("\n> ").strip().lower().split()
        
        if not command:
            continue
        
        if command[0] == "quit":
            print("Goodbye!")
            break
        elif command[0] == "look":
            continue  # Room description is already shown
        elif command[0] == "inventory":
            if inventory:
                print(f"Inventory: {', '.join(inventory)}")
            else:
                print("Your inventory is empty.")
        elif command[0] == "go":
            if len(command) < 2:
                print("Go where?")
                continue
            
            direction = command[1]
            if direction in room["exits"]:
                next_room = room["exits"][direction]
                
                # Check if next room is locked
                if ROOMS[next_room].get("locked", False):
                    if "key" in inventory:
                        print("You unlock the door with the key!")
                        ROOMS[next_room]["locked"] = False
                        current_room = next_room
                    else:
                        print("The door is locked! You need a key.")
                else:
                    current_room = next_room
            else:
                print(f"You can't go {direction} from here.")
        elif command[0] == "get":
            if len(command) < 2:
                print("Get what?")
                continue
            
            item = command[1]
            if item in room["items"]:
                inventory.append(item)
                room["items"].remove(item)
                print(f"You picked up the {item}.")
            else:
                print(f"There is no {item} here.")
        elif command[0] == "use":
            if len(command) < 2:
                print("Use what?")
                continue
            
            item = command[1]
            if item in inventory:
                print(f"You use the {item}.")
                # Special item effects
                if item == "torch" and current_room == "entrance":
                    print("The torch lights up the cave entrance!")
                elif item == "sword" and ROOMS[current_room].get("enemy"):
                    print(f"You defeat the {ROOMS[current_room]['enemy']}!")
                    del ROOMS[current_room]["enemy"]
                else:
                    print(f"Nothing special happens with the {item}.")
            else:
                print(f"You don't have a {item}.")
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
