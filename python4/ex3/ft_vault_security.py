def secure_archive(filename, action='r', content=None):
    try:
        if action == 'r':
            with open(filename, 'r') as files:
                content = files.read()
                return (True, content)
        elif action == 'w':
            with open(filename, 'w') as files_w:
                files_w.write("Content successfully written to file")
                return (True, "Content successfully written to file")
    except FileNotFoundError as e:
        return (False, f"{e}")
    except PermissionError as err:
        return (False, f"{err}")


def main():
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('/not/existing/file')}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive('/ex3/test.txt')}\n")

    contentt = secure_archive('test.txt')
    print("Using 'secure_archive' to read from a regular file:")
    print(contentt)
    print()
    contentt_new = {secure_archive('new_test.txt', 'w')}
    print("Using 'secure_archive' to write previous content to a new file:")
    print(contentt_new)


if __name__ == '__main__':
    main()
