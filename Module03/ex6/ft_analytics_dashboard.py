
# comprehension: instead of appending to a list its a short way
#           to append inside a list/dict/set
# dict(): makes a dictionary
# keys(): returns a list of names in dict
# values(): returns a list of only values in dic
# items(): returns a list of tupples (names, values)
# get("name"): gets the value of a name
# update({"b": 2, "a": 10}): updates values


players = {
    "alice": {
        "score": 2300,
        "achievements": {"first_kill", 'treasure_hunter', 'speed_demon',
                         'perfectionist', 'explorator'},
        "region": "north",
        "active": True
    },
    "bob": {
        "score": 1800,
        "achievements": {"level_10", 'boss', 'explorator'},
        "region": "east",
        "active": True
    },
    "charlie": {
        "score": 2150,
        "achievements": {"boss_slayer", 'treasure_hunter', 'speed_demon',
                         'collector', 'perfectionist', 'explorator',
                         'boss'},
        "region": "central",
        "active": True
    },
    "diana": {
        "score": 2050,
        "achievements": {'explorator', 'boss', 'collector'},
        "region": "north",
        "active": False
    }
}


def list_comp() -> None:
    print("\n=== List Comprehension Examples ===")

    hight_scores_names = [x for x in players if players[x]["score"] > 2000]
    print("High scorers (>2000):", hight_scores_names)

    doubled_scores = [players[x]["score"] * 2 for x in players]
    print("Scores doubled:", doubled_scores)

    active_players = [x for x in players if players[x]["active"] is True]
    print("Active players:", active_players)


def dict_comp() -> None:
    print("\n=== Dict Comprehension Examples ===")

    player_score = {x: players[x]["score"] for x in players}
    print("Player scores:", player_score)

    score_categories = {
        "high": sum(1 for p in players.values() if p["score"] > 2100),
        "medum": sum(1 for p in players.values() if 2000 < p["score"] <= 2100),
        "low": sum(1 for p in players.values() if p["score"] <= 2000),
    }
    print("Score categories:", score_categories)

    ach_count = {
        name: len(stat["achievements"]) for name, stat in players.items()
        if stat["active"] is True
    }
    print("Achievement counts:", ach_count)


def set_comp() -> None:
    print("\n=== Set Comprehension Examples ===")
    unique_players = {name for name in players}
    print("Unique players:", unique_players)

    achievement_count = {}
    for p in players.values():
        for ach in p["achievements"]:
            achievement_count[ach] = achievement_count.get(ach, 0) + 1
    unique_ach = {name for name, val in achievement_count.items() if val == 1}
    print("Unique achievements:", unique_ach)

    regions = {p["region"] for p in players.values() if p["active"] is True}
    print("Active regions:", regions)


def analysis() -> None:
    print("\n=== Combined Analysis ===")

    print("Total players:", len(players))

    total_ach = {ach for p in players.values() for ach in p["achievements"]}
    print("Total unique achievements:", len(total_ach))

    score_list = [p["score"] for p in players.values()]
    print("Average score:", sum(score_list) / len(players))

    topscore = max(score_list)
    top = {k: v["score"] for k, v in players.items() if v["score"] == topscore}
    top_player = list(top.keys())[0]
    print(f"Top performer: {top_player} ({players[top_player]['score']} "
          f"points, {len(players[top_player]['achievements'])} achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    list_comp()
    dict_comp()
    set_comp()
    analysis()
