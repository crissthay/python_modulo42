import math


def get_player_pos():
    while True:
        try:
            inputt = input(
                "Enter new coordinates as floats "
                "in format 'x,y,z':")
            splitup = inputt.split(",")
            return tuple(float(x) for x in splitup)
        except ValueError:
            print("invalid syntax")

        try:
            for p in splitup:
                float(p.strip())
        except ValueError:
            print(
                f"Error on parameter '{p.strip()}':"
                f"could not convert string to float: '{p.strip()}'")


def main():
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    fun = get_player_pos()

    print(f"Got a first tuple: {fun}")
    print(f"It includes: X={fun[0]}, Y={fun[1]}, Z={fun[2]}")

    m1 = math.sqrt(fun[0]**2 + fun[1]**2 + fun[2]**2)
    print(f"Distance to center: {round(m1, 4)}")
    print("")

    print("Get a first set of coordinates")
    fun1 = get_player_pos()

    m2 = math.sqrt((fun1[0]-fun[0])**2 +
                   (fun1[1]-fun[1])**2 +
                   (fun1[2]-fun[2])**2)
    print(f"Distance to center: {round(m2, 4)}")


if __name__ == "__main__":
    main()
