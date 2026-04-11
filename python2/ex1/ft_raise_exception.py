def input_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        if temp < 0:
            print(
                f"Caught input_temperature error:"
                f" {temp} is too cold for plants (min 0°C)\n"
            )
        elif temp > 40:
            print(
                f"Caught input_temperature error: "
                f"{temp} is too hot for plants (max 40°C)\n"
            )
        else:
            print(f"Temperature is {temp}°C\n")


def test_temperature():
    print("=== Garden Temperature Checker ===")
    print()

    valid_input = "25"
    print(f"Input data is '{valid_input}'")
    input_temperature(valid_input)

    invalid_input = "abc"
    print(f"Input data is '{invalid_input}'")
    input_temperature(invalid_input)

    max_input = "100"
    print(f"Input data is '{max_input}'")
    input_temperature(max_input)

    min_input = "-50"
    print(f"Input data is '{min_input}'")
    input_temperature(min_input)

    print("All tests completed - program didn't crash!")


def main():
    test_temperature()


if __name__ == "__main__":
    main()
