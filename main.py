def run_robot():
    position_x = 0
    position_y = 3

    grid_x = 10
    grid_y = 10

    fuel = 51

    direction = "E"
    # Move Robot
    while True:

        # Exit condition 1: Robot out of positive range of grid
        if position_x > grid_x or position_y > grid_y:
            result_str = "Robot is out of range x={} : y={} "
            print(result_str.format(position_x, position_y))
            break

        # Exit condition 2: Robot out of zero range of grid
        if position_x < 0 or position_y < 0:
            result_str = "Robot is out of range x={} : y={} "
            print(result_str.format(position_x, position_y))
            break

        # Check robot fuel
        if fuel <= 0:
            result_str = "Robot is out of gas {} "
            print(result_str.format(fuel))
            break

        # Move Robot
        if direction == "S":
            position_y -= 1
        elif direction == "N":
            position_y += 1
        elif direction == "E":
            position_x += 1
        elif direction == "W":
            position_x -= 1

        # Consume fuel
        fuel -= 1  # Fuel = Fuel - 2 = 4

        result_str = "Robot is still running {} : gas {} : pos x: {} : pos y: {}"
        print(result_str.format(direction,fuel,position_x, position_y))
    # End of While


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    run_robot()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
