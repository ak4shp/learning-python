'''The Car Game'''

command = ""
started = False
print("****** WELCOME TO THE CAR GAME ******")
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started...")
    elif command == 'stop':
        if not started:
            print('Car is already stopped.')
        else:
            started = False
            print("Car stopped.")
    elif command == 'left':
        if not started:
            print("please start the car first")
        else:
            # started = False
            print("Car is turning left...")
    elif command == 'right':
        print("Car is turning right...")
    elif command == 'help':
        print("""
start -> to start car
stop -> to stop car
left -> to turn left
right -> to turn right
quit -> to exit game
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry I don't understand. Please type help.")


