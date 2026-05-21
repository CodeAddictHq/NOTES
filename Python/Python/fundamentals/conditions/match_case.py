# match/case: structural pattern matching (Python 3.10+)
# Similar to switch/case in other languages

command = "quit"

match command:
    case "quit":
        print("Quitting the program.")
    case "help":
        print("Showing help.")
    case "start":
        print("Starting...")
    case _:
        print(f"Unknown command: {command}")

# Match with values
point = (0, 1)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis at {x}")
    case (0, y):
        print(f"On y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")
