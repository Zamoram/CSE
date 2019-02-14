world_map = {
    'Living Room': {
        'Name': "Living Room",
        'Description': "This is where you live and start.",
        'Paths': {
            'North': "Outside",
            'South': "Dining Room"
        }
    },
    'Dining Room': {
        'Name': "Eating Area",
        'Description': "This is where you eat",
        'Paths': {
            'East': "Bed_Room",
            'South': " Kitchen"
        }
    },
    'Outside': {
        'Name': "Outside of the house",
        'Description': "You are outside of the house and you can not go any farther and you must go back.",
        'Paths': {
            'South': "Living Room"
        }
    },
    'Bed_Room': {
        'Name': "Place to sleep",
        'Description': "This is where you sleep and do your homework and where you play video games.",
        'Paths': {

        }
    }


}
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["Living Room"]  # This is your current location
playing = True

print(current_node['NAME'])
command = input(">_")
if command in ['q', 'quit', 'exit']:
    playing = False
elif command in directions:
    try:
        room_name = current_node["PATHS"][command]
        current_node = world_map[room_name]
    except KeyError:
        print("I can't go that way.")

else:
    print("Command not recognized.")