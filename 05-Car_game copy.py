"""The Car Game"""

command = ""  # No Commands 
engine_on = False  # Engine OFF (Not ON)

print("****** WELCOME TO THE CAR GAME ******")

while True:
    command = input("> ").lower()

    # Start
    if command == "start":
        if not engine_on:
            engine_on = True
            print("Car Started.") 
        else:
            print("Car Already Running...")
    # Stop
    elif command == "stop":
        if engine_on:
            engine_on = False
            print("Car Stopped.")
        else:
            print("Car Not Running...")
    # Left
    elif command == "left":
        if engine_on:
            print("Turning Left...")
        else:
            print("Car Not Running...")
    # Right
    elif command == "right":
        if engine_on:
            print("Turning Right...")
        else:
            print("Car Not Running...")
    # Quit
    elif command == "quit":
        engine_on = False
        break
    # Help
    elif command == "help":
        print("""
start -> to start car
stop -> to stop car
left -> to turn left
right -> to turn right
quit -> to exit game
        """)
    # Invalid Command Supplied
    else:
        print("Sorry I don\'t understand. Please type help.") 
