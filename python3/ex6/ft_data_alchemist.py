import random


def main():
    print("=== Game Data Alchemist ===")
    players = ['Taerae', 'sunoo', 'Beomgyu', 'Jiahao', 'ZhangHao']
    print(f"Initial list of players: {players}")
    cap_players = [i.capitalize() for i in players]
    print(f"New list with all names capitalized: {cap_players}")
    yetcap = [i for i in players if i[0].isupper()]
    print(f"New list of capitalized names only: {yetcap}")
    score = {item: random.randint(1, 500) for item in cap_players}
    print(score)
    soma = sum(score.values()) / len(score)
    avascr = round(soma, 5)
    print(f"Score average is {avascr}")
    high = {k: score[k] for k in score.keys() if score[k] > avascr}
    print(high)


if __name__ == "__main__":
    main()
