import random


def gen_player_achievements():
    ativ = [
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'
        ]

    alice = set(random.sample(ativ, 5))
    print(f"Player Alice: {alice}")
    bob = set(random.sample(ativ, 7))
    print(f"Player Bob: {bob}")
    charlie = set(random.sample(ativ, 5))
    print(f"Player Charlie: {charlie}")
    dylan = set(random.sample(ativ, 8))
    print(f"Player Dylan: {dylan}")
    print("")

    all_a = set(ativ)
    print("All distinct achievements:", all_a)
    print()

    result = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {result}")
    print("")

    alice1 = alice.difference(bob.union(charlie, dylan))
    print("Only Alice has:", alice1)
    bob1 = bob.difference(alice.union(charlie, dylan))
    print("Only Bob has:", bob1)
    charlie1 = charlie.difference(alice.union(bob, dylan))
    print("Only Charlie has:", charlie1)
    dylan1 = dylan.difference(alice.union(bob, charlie))
    print("Only Dylan has:", dylan1)
    print("")

    alice2 = all_a.difference(alice)
    print("Alice is missing:", alice2)
    bob2 = all_a.difference(bob)
    print("Bob is missing:", bob2)
    charlie2 = all_a.difference(charlie)
    print("Charlie is missing:", charlie2)
    dylan2 = all_a.difference(dylan)
    print("Bob is missing:", dylan2)


def main():
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()


if __name__ == "__main__":
    main()
