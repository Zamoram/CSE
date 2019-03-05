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
            'South': "Kitchen",
            'North': "Living Room",
            'West': "Bed_Room2"
        }
    },
    'Outside': {
        'Name': "Outside of the house",
        'Description': "You are outside of the house and you can not go any farther and you must go back.",
        'Paths': {
            'South': "Living Room"
        }
    },
    'Bed_Room1': {
        'Name': "Place to sleep",
        'Description': "This is where you sleep and do your homework and where you play video games.",
        'Paths': {
            'North': "Restroom",
            'West': "Dining Room"
        }
    },
    'Restroom': {
        'Name': "A place you do your buisness",
        'Description': "This is where you go to relieve yourself.",
        'Paths': {
            'South': "Bed_Room1"
        }
    },
    'Bed_Room2': {
        'Name': "The Sleeper",
        'Description': "This is where you go to sleep",
        'Paths': {
            'East': "Dining_Room",
            'South': "Hallway"
        }
    },
    'Kitchen': {
        'Name': "The Eater",
        'Description': "This is where you cook food",
        'Paths': {
            'North': "Dining_Room",
            'South': "Laundry Room",
            'West': "Hallway"
        }
    },
    'Hallway': {
        'Name': "The intersection",
        'Description': "This leads to many routes.",
        'Paths': {
            'North': "BedRoom2",
            'East': "Kitchen",
            'South': "BedRoom3",
            'West': "BathRoom"
        }

    },
    'BathRoom': {
        'Name': "The pooper",
        'Description': "Another room to take care of your business",
        'Paths': {
            'East': "Hallway"

        }
    },
    'BedRoom3': {
        'Name': "The guest bedroom",
        'Description': "This is where your guests can go to sleep when you have visitors over",
        'Paths': {
            'North': "Hallway"
        }
    },
    'LandryRoom': {
        'Name': "The washing room",
        'Description': "This is where you go to wash your clothes.",
        'Paths': {
            'North': "Kitchen"
        }
    },
    'Restroom1': {
        'Name': "The buisness taker",
        'Description': "This is the first bathroom built in the house",
        'Paths': {
            'South': "BedRoom1"
        }
    },
    'Garage': {
        'Name': "The car storer",
        'Description': "This is where you park your cars",
        'Paths': {
            'East': "Outside"
        }
    },
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