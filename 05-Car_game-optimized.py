class Engine:
    ON = True
    OFF = False


class Car:
    def __init__(self, initial_engine_status: bool = Engine.OFF) -> None:
        self.turn_directions = ["left", "right"]
        self.engine_status: bool = initial_engine_status
        self.command: str = ""

        self.commands = {
            "start": self.start(),
            "stop": self.stop(),
            "left": self.turn("left"),
            "right": self.turn("right")
        }

    def start(self) -> None:
        self.engine_status = Engine.ON

    def stop(self) -> None:
        self.engine_status = Engine.OFF

    def turn(self, direction = "") -> str:
        if self.engine_status == Engine.ON:
            if direction in self.turn_directions:
                return f"Turning {direction}..."
            else:
                return "Invalid direction."
        else:
            return "Car is not running."

    def run(self, command: str = "") -> None:
        if command == "start":
            self.start()
            print("Car Started.")
        elif command == "stop":
            self.stop()
            print("Car Stopped.")
        elif command == "left":
            print(self.turn("left"))
        elif command == "right":
            print(self.turn("right"))
        elif command == "help":
            print("""
start -> to start car
stop -> to stop car
left -> to turn left
right -> to turn right
quit -> to exit game
        """)
        else:
            print("Invalid Command. (type help for playing modes.)")


# main 
if __name__ == "__main__":
    print("****** WELCOME TO THE CAR GAME ******")
    
    car = Car(Engine.OFF)
    command = ""

    while True:
        command = input("> ")
        if command == "quit":
            break
        car.run(command)





