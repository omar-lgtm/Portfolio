



import random  

def main():
    username=input("please enter your username: ")
    available_categories = [1, 2, 3, 4, 5, 6]  
    category_names = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]  
    filename = "High_Scores.txt"  
    print_banner(username)
    total_score = play_game(available_categories, category_names)
    handle_high_scores(filename, username, total_score)

def roll_dice():
    dice_roll = []
    for i in range(0, 5):
        dice_roll.append(random.randrange(1, 7))
    return dice_roll

def print_banner(username):
    print("**********************")
    print(f"* Yacht by {username} *")
    print("**********************")

def calculate_roll_score(category, dice_roll):
    score = 0
    for die in dice_roll:
        if die == category:
            score += die
    return score

def get_category(available_categories):
    print(f"Available categories: {available_categories}")
    
    selected = input("Please choose a category from those available: ")
    chosen_category = int(selected)

    while chosen_category not in available_categories:
        print(f"{chosen_category} is not available!")
        selected = input("Please choose a category from those available: ")
        chosen_category = int(selected)
    return chosen_category

def play_game(available_categories, category_names):
    total_score = 0

    for round_number in range(0, 6):
        dice_roll = roll_dice()
        dice_roll.sort()

        print(f"You have rolled the following: {dice_roll}")

        chosen_category = get_category(available_categories)
        print(f"You have chosen {category_names[chosen_category - 1]}")

        round_score = calculate_roll_score(chosen_category, dice_roll)
        print(f"You have scored {round_score} this round.")

        total_score += round_score

        if round_number < 5:
            print(f"Your current total score is {total_score}.")
            i=0
            while i < len(available_categories):
                current_categoory=available_categories[i]
                if current_categoory==chosen_category:
                    available_categories.pop(i)
                i += 1

        print()

    print(f"Congratulations! You have scored {total_score}!")
    return total_score

def read_high_scores(filename):
    scores = []

    with open(filename, "r") as file:
        file.readline()

        for line in file:
            line = line.strip().split(". ")
            scores.append(int(line[1]))
    return scores

def update_high_scores(filename, username, high_scores, new_score):
    if len(high_scores) < 5 or new_score > min(high_scores):
        high_scores.append(new_score)
        high_scores.sort(reverse=True)
        high_scores = high_scores[:5]  # Keep only the top 5 scores

        with open(filename, "w") as file:
            file.write(f"High Scores for {username}\n")
            for i in range(1, 6):
                file.write(f"{i}. {high_scores[i-1]}\n")

def handle_high_scores(filename, username, new_score):
    high_scores = read_high_scores(filename)
    update_high_scores(filename, username, high_scores, new_score)

main() 
