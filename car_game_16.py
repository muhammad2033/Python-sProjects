command = ""
started = False
while True:
    command = input(">")
    if command == "start": 
        if started=="started": 
            print(" car is already started, what are u doing!")
        else:
            started = True
            print("start the car")
    elif command == "stop": 
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("stop the car")

    elif command == "help": 
        print("""
                start -  start the car 
                stop -   stop the car
                quit - exit() """)

    elif command == "quit":
        print("exit() ")
        break
    else:
        print(" sorry, i dont understand.....")
    