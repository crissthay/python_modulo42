import sys


def main():
    fiche = None
    content = ''
    print("=== Cyber Archives Recovery ===")
    name = sys.argv[0]

    if len(sys.argv) < 2:
        print(f"Usage {name} <file>")
        return

    name_file = sys.argv[1]
    print(f"Accessing file '{name_file}'")
    try:
        fiche = open(name_file, "r")
        fileprint = fiche.read()
        print(f"---\n{fileprint}\n---")

        fiche.close()
        print()
        print("Transform data:\n")
        print("---\n")

        file_data = open(name_file, 'w')
        for line in fileprint.splitlines():
            new = line.strip() + '#'
            print(new)
            file_data.write(new + '\n')
            content += new + '\n'

        file_data.close()
        file_new = input("Enter new file name (or empty):")
        if not file_new:
            print("Not saving data.")
        else:
            print(f"Saving data to '{file_new}'")
            new_filee = open(file_new, "w")
            new_filee.write(content)
            new_filee.close()
            print(f"Data saved in file '{file_new}'")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except PermissionError as err:
        print(f"Caught PermissionError: {err}")


if __name__ == "__main__":
    main()
