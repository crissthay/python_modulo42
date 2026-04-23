import sys


def main():
    fiche = None
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
        print("---\n")
        print(fileprint)
        print("\n---")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except PermissionError as err:
        print(f"Caught PermissionError: {err}")
    finally:
        if fiche:
            fiche.close()
            print(f"File {name_file} closed")


if __name__ == '__main__':
    main()
