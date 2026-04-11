def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        result = 10 / 0
    elif operation_number == 2:
        with open("/non/existent/file", "r") as file:
            content = file.read()
            _ = content
    elif operation_number == 3:
        result = "str" + 10
        _ = result
    else:
        print("Operation completed successfully")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    print("Testing operation 4...")
    result2 = garden_operations(4)
    if result2 is None:
        print()

    print("All error types tested successfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
