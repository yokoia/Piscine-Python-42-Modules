
import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argc: int = len(sys.argv)

    if argc <= 1:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    try:
        scores = []
        for arg in sys.argv[1:]:
            score: int = int(arg)
            scores.append(score)
        print("Scores processed:", scores)
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    except ValueError as message:
        print("Error:", message)


if __name__ == "__main__":
    main()
