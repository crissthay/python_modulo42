import sys


def main():
    fiche = None
    fiche_new = None
    name_program = sys.argv[0]
    contentent = ''

    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) < 2:
        print(f"Usage {name_program} <file>")
        return

    name_file = sys.argv[1]
    print(f"Accessing file '{name_file}'")

    try:
        fiche = open(name_file, 'r')
        printfile = fiche.read()
        print(f"---\n{printfile}\n---")
        fiche.close()
        print(f"File {name_file} closed")

        print("Transform data:\n----")

        fiche_new = open(name_file, 'w')
        for line in printfile.splitlines():
            new = line.strip() + '#'
            print(new)
            fiche_new.write(new + '\n')
            contentent += new + '\n'
        fiche_new.close()

        print("---")

        print("Enter new file name (or empty):", end='')
        new_name = sys.stdin.readline().strip()

        if not new_name:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_name}'")
            new_filee = open(new_name, "w")
            new_filee.write(contentent)
            new_filee.close()
            print(f"Data saved in file '{new_name}'")

    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{name_file}': {e}\n")
    except PermissionError as err:
        sys.stderr.write(f"[STDERR] Error opening file '{name_file}': {err}\n")


if __name__ == '__main__':
    main()
