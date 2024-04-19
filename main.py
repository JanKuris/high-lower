import random
import os 
from game_data import data_list
from art import logo, vs 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

def get_random_account():
    return random.choice(data_list)

def format_account_info(acount):
    name = acount['name']
    description = acount['description']
    city = acount['country']
    return f"{name} {description} from {city}"

def check_answer(guess, a_account, b_account,):
    if a_account > b_account:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    # print(logo)
    score = 0
    game_should_continue = True
    a_account = get_random_account()
    b_account = get_random_account()
    
    while game_should_continue:
        a_account = b_account
        b_account = get_random_account()

        while a_account == b_account:
            b_account = get_random_account()
        
        print(f"Compare A: {format_account_info(a_account)}")
        print(vs)
        print(f"Compare B: {format_account_info(b_account)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_numb = a_account['follower_count']
        b_follower_numb = b_account['follower_count']
        is_correct = check_answer(guess, a_follower_numb, b_follower_numb)

        clear_screen()
        print(logo)
        if is_correct:
            score += 1 
            print(f"You are right! Current score: {score} ")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
game()