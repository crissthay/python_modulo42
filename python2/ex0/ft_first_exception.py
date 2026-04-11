def input_temperature(temp_str):
    try:
        return int(temp_str)
    except ValueError:
        return None


def test_temperature():
    print("=== Garden Temperature ===")

    valid_input = "25"
    print(f"input data is '{valid_input}'")
    result = input_temperature(valid_input)
    if result is not None:
        print(f"Temperature is now {result}°C")

    print()

    invalid_input = 'a'
    print(f"input data is '{invalid_input}'")
    result1 = input_temperature(invalid_input)
    if result1 is None:
        print(
            f"Caught input_temperature error: "
            f"invalid literal for int() with base 10: '{invalid_input}'"
        )
    print()
    print("All tests completed - program didn")


def main():
    test_temperature()


if __name__ == "__main__":
    main()
