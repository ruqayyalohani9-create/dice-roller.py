import random

dice_art = {
    1: (
        "---------",
        "|       |",
        "|   ●   |",
        "|       |",
        "---------"
    ),
    2: (
        "---------",
        "| ●     |",
        "|       |",
        "|     ● |",
        "---------"
    ),
    3: (
        "---------",
        "| ●     |",
        "|   ●   |",
        "|     ● |",
        "---------"
    ),
    4: (
        "---------",
        "| ●   ● |",
        "|       |",
        "| ●   ● |",
        "---------"
    ),
    5: (
        "---------",
        "| ●   ● |",
        "|   ●   |",
        "| ●   ● |",
        "---------"
    ),
    6: (
        "---------",
        "| ●   ● |",
        "| ●   ● |",
        "| ●   ● |",
        "---------"
    )
}

def main():
    dice = []
    total = 0
    
    try:
        number_of_dice = int(input("How many dice? "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if number_of_dice <= 0:
        print("Number of dice must be at least 1.")
        return

    for _ in range(number_of_dice):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for die in dice:
            print(dice_art[die][line], end="  ")
        print()

    for die in dice:
        total += die

    print(f"\nTotal: {total}")

if __name__ == "__main__":
    main()