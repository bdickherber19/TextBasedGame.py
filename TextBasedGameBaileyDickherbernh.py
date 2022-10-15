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


# def get_item(current_room, rooms, inventory):
def get_item(current_room, move, rooms, inventory):
    # add item to inventory and remove from room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of rooms with items
    rooms = {
        'Toy box': {'West': 'Main floor', 'item': 'Slink'},
        'Main floor': {'North': 'Window', 'West': 'Under bed', 'South': 'Top drawer', 'East': 'Toy box'},
        'Top drawer': {'North': 'Main floor', 'South': 'Under dresser', 'item': 'Army Men'},
        'Under dresser': {'North': 'Top drawer', 'West': 'Closet', 'item': 'Monkeys'},
        'Closet': {'North': 'Under bed', 'South': 'Under dresser', 'item': 'Shoe Laces'},
        'Under bed': {'North': 'Top of bed', 'East': 'Main floor', 'South': 'Closet', 'item': 'Skateboard'},
        'Top of bed': {'South': 'Under bed', 'West': 'Night stand', 'item': 'Teddy'},
        'Night stand': {'East': 'Top of bed', 'item': 'Battery'},
        'Window': {'South': 'Main floor', 'item': 'Cat'}
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
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = moving_rooms(current_room, move[1], rooms)
            continue

        # getting an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You got {}'.format(rooms[current_room]['item']))
            print('----------------')
            get_item(current_room, move, rooms, inventory)
            continue
        # invalid commands
        else:
            print('Invalid move, try another move!')
            continue


if __name__ == '__main__':
    main()
