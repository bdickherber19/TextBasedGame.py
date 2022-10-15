def user_instructions():
    # instructions to game play
    print('Toy Story Game!')
    print('Collect all 6 items to save Jessie and win or be eaten by the cat!')
    print('Move commands: go north, go south, go east, go west')
    print('Add to inventory: get "item"')


def moving_rooms(current_room, move, rooms):
    # movement through rooms
    current_room = rooms[current_room][move]
    return current_room


def get_item(current_room, rooms, inventory):
    # add item to inventory and remove from room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of rooms with items
    rooms = {
        'Toy box': {'west': 'Main floor', 'item': 'Slink'},
        'Main floor': {'north': 'Window', 'west': 'Under bed', 'south': 'Top drawer', 'east': 'Toy box'},
        'Top drawer': {'north': 'Main floor', 'south': 'Under dresser', 'item': 'army men'},
        'Under dresser': {'north': 'Top drawer', 'west': 'Closet', 'item': 'monkeys'},
        'Closet': {'north': 'Under bed', 'south': 'Under dresser', 'item': 'shoe laces'},
        'Under bed': {'north': 'Top of bed', 'east': 'Main floor', 'south': 'Closet', 'item': 'skateboard'},
        'Top of bed': {'south': 'Under bed', 'west': 'Night stand', 'item': 'teddy'},
        'Night stand': {'east': 'Top of bed', 'item': 'battery'},
        'Window': {'south': 'Main floor', 'item': 'Cat'}
    }

    # list of inventory for gamer
    inventory = []
    # starting room
    current_room = 'Toy box'
    # directions
    move = ['north', 'south', 'east', 'west']

    while True:
        # villain
        if current_room == 'Window':
            # win the game
            if len(inventory) == 6:
                print('Awesome! You got passed the cat and saved Jessie! You win!')
                break
            # lost the game
            else:
                print('You did not make it passed the cat')
                break
        # give play the current room and inventory
        print('You are in the ' + current_room)
        print(inventory)
        # let the player know what item is in the room
        if current_room != 'Window' and 'item' in rooms[current_room].keys():
            print('Theres is {}'.format(rooms[current_room]['item']))
        print('------------------')

        move = input('Next move?!: ').title().split()

        # commanding room movement
        if len(move) >= 2 and move[0] in rooms[current_room].keys():
            current_room = moving_rooms(current_room, move, rooms)
            continue

        # getting an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print(f'You got {rooms[current_room]["item"]}')
            print('----------------')
            get_item(current_room, rooms, inventory)
            continue
        # invalid commands
        else:
            print('Invalid move, try another move!')
            continue


if __name__ == '__main__':
    main()
