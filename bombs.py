from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = deque([int(x) for x in input().split(", ")])

bombs = {40: "Datura Bombs",
        60:"Cherry Bombs" ,
        120 : "Smoke Decoy Bombs"
}
bomb_counter = {
        "Datura Bombs": 0,
        "Cherry Bombs": 0,
        "Smoke Decoy Bombs": 0
}


while bomb_effects and bomb_casings:
    if bomb_counter["Datura Bombs"] >= 3 and bomb_counter["Cherry Bombs"] >= 3 and bomb_counter["Smoke Decoy Bombs"] >= 3:
        print(f"Bene! You have successfully filled the bomb pouch!")
        break


    effect = bomb_effects[0]
    casing = bomb_casings[-1]

    if effect + casing in bombs:
        bomb_effects.popleft()
        bomb_casings.pop()
        counter = bombs[effect + casing]
        bomb_counter[counter] += 1
    else:
        bomb_casings[-1] -= 5


if bomb_counter["Datura Bombs"] < 3 or bomb_counter["Cherry Bombs"] < 3 or bomb_counter["Smoke Decoy Bombs"] < 3:
        print(f"You don't have enough materials to fill the bomb pouch.")


if not bomb_effects:
    print(f"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
if not  bomb_casings:
    print(f"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")

for k, v in sorted(bomb_counter.items()):
    print(f"{k}: {v}")