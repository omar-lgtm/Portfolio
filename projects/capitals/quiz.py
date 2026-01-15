"""
World Capitals Quiz
Author: Syed Muhammad Omar
Description:
A geography quiz that tests the user on the capital cities of the world.
The program asks 6 multiple-choice questions, calculates the user’s score,
and maintains a high-score table in a text file.
"""

import random  


def print_banner(username):
    print("#####################################")
    print(f"# World Capitals Quiz For {username.upper()} #")
    print("#####################################\n")


def get_world_capitals_dictionary(filename):
    world_capitals = {}
    file = open(filename, "r")
    for sentence in file:
        part = sentence.strip().split(":")
        if len(part) == 2:
            country = part[0].strip()
            capital = part[1].strip()
            world_capitals[country] = capital
    file.close()
    return world_capitals


def get_player_answer(target_country, cities):
    print("Choices available:", cities)
    answer = input(f"What is the capital city of {target_country}? ")
    while answer not in cities:
        print("You must choose from the city choices available!")
        answer = input(f"What is the capital city of {target_country}? ")
    cities.remove(answer)
    return answer


def run_round(world_capitals_dict, countries_tested):
    target_country, cities = get_question_data(world_capitals_dict, countries_tested)
    correct_capital = world_capitals_dict[target_country]
    attempts = 3
    round_score = 0
    while attempts > 0:
        player_choice = get_player_answer(target_country, cities)
        if player_choice == correct_capital:
            print("Your answer is correct! Well done!\n")
            if attempts == 3:
                round_score = 3
            elif attempts == 2:
                round_score = 2
            else:
                round_score = 1
            return round_score
        else:
            attempts = attempts - 1
            if attempts > 0:
                print("Your answer is incorrect! Please try again!\n")
            else:
                print("Your answer is incorrect! Better luck next time!\n")
    return round_score


def run_quiz(world_capitals_dict):
    total_score = 0
    countries_tested = []
    round_number = 1
    while round_number <= 6:
        print(f"Round {round_number}:\n")
        total_score = total_score + run_round(world_capitals_dict, countries_tested)
        round_number = round_number + 1
        print()
    print(f"You have scored {total_score} out of 18 for the World Capital's Quiz!")
    return total_score


def read_high_scores(filename):
    high_scores = []
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    for line in lines[1:]:
        parts = line.strip().split(". ")
        if len(parts) == 2 and parts[1].isdigit():
            high_scores.append(int(parts[1]))
    return high_scores


def sort_high_scores(high_scores):
    n = len(high_scores)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if high_scores[j] < high_scores[j + 1]:
                temp = high_scores[j]
                high_scores[j] = high_scores[j + 1]
                high_scores[j + 1] = temp
            j = j + 1
        i = i + 1
    return high_scores


def update_high_scores(filename, username, high_scores, new_score):
    high_scores.append(new_score)
    high_scores = sort_high_scores(high_scores)
    if len(high_scores) > 5:
        high_scores = high_scores[:5]
    file = open(filename, "w")
    file.write(f"High Scores for {username}\n")
    i = 0
    while i < len(high_scores):
        file.write(f"{i + 1}. {high_scores[i]}\n")
        i = i + 1
    file.close()


def handle_high_scores(filename, username, new_score):
    high_scores = read_high_scores(filename)
    update_high_scores(filename, username, high_scores, new_score)


def main():
    input_filename = "WorldCapitals.txt"
    output_filename = "HighScores.txt"
    username = "tdan315"

    print_banner(username)
    world_capitals_dict = get_world_capitals_dictionary(input_filename)
    score = run_quiz(world_capitals_dict)
    handle_high_scores(output_filename, username, score)


def get_question_data(world_capitals_dict, countries_tested):
    countries = list(world_capitals_dict.keys())
    target_country = countries[random.randrange(0, len(countries))]
    while target_country in countries_tested:
        target_country = countries[random.randrange(0, len(countries))]
    countries_tested.append(target_country)
    countries.remove(target_country)

    cities = [world_capitals_dict[target_country]]
    while len(cities) < 5:
        country = countries[random.randrange(0, len(countries))]
        countries.remove(country)
        cities.append(world_capitals_dict[country])
    random.shuffle(cities)
    return target_country, cities


main()
