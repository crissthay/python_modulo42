import sys


def main():
    print("=== Inventory System Analysis ===")

    inv = {}

    for arg in sys.argv[1:]:
        if ':' not in arg:
            print("Error - invalid parameter")
            continue

        words = arg.split(':')
        if len(words) != 2:
            print("Error")
            continue

        name = words[0]

        try:
            quantity = int(words[1])
        except ValueError:
            print("Error - not a valid value")
            continue

        if name in inv:
            print("Error - duplicate argument")
            continue

        inv[name] = quantity

    print('Inventory:', inv)

    items = list(inv.keys())
    print('Items:', items)

    total = sum(inv.values())
    print('Total quantity:', total)

    print('Percentages:')
    for name, q in inv.items():
        percent = (q / total) * 100 if total > 0 else 0
        print(f'{name}: {round(percent, 2)}%')

    maxitem = None
    minitem = None

    for name in inv:
        if maxitem is None or inv[name] > inv[maxitem]:
            maxitem = name
        if minitem is None or inv[name] < inv[minitem]:
            minitem = name

    print('Most abundant:', maxitem)
    print('Least abundant:', minitem)

    newi = "ex"
    newq = 10
    inv[newi] = newq

    print('Updated inventory:', inv)


if __name__ == "__main__":
    main()
