import sys


print("=== Player Score Analytics ===")

score = []

for arg in sys.argv[1:]:
    try:
        n = int(arg)
        score += [n]
    except ValueError:
        print(f"Invalid parameter: '{arg}'")


if len(score) == 0:
    print(
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
        )
else:
    print("tatal player:", len(sys.argv) - 1)
    print("Total score:", sum(score))
    print("Average score:", sum(score) / len(score))
    print("High score:", max(score))
    print("Low score:", min(score))
    print("Score range:", max(score) - min(score))
