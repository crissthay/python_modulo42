import random


def gen_event():
    names = ['Liza', 'Thay', 'Vic', 'Dinis', 'Taerae', 'erica']
    actions = ['Kill', 'pregnant', 'KILL THE BABY', 'A hug', 'Mpreg']

    while True:
        name = random.choice(names)
        act = random.choice(actions)
        yield (name, act)


def ten_events(exmple):
    exmple = list(exmple)
    while exmple:
        remove1 = random.choice(exmple)
        exmple.remove(remove1)
        yield remove1


def main():

    print("=== Game Data Stream Processor ===")
    events_all = gen_event()
    for i in range(10):
        name, act = next(events_all)
        print(f"Event {i}:  Player {name} did action {act}")
        i += 1
    print("")
    rmv = [next(events_all) for i in range(10)]
    print(f"Built list of 10 events: {rmv}")
    for events in ten_events(rmv):
        print(f"Got event from list: {events}")
        print(f"Remains in list: {rmv}")


if __name__ == "__main__":
    main()
