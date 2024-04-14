import random
from game_data import data_list
from art import logo, vs 


def get_random_dict(data_list):
    random_result = random.choice(data_list)
    return random_result  
# def compare():
#     random_result_A = get_random_dict(data_list)
#     random_result_B = get_random_dict(data_list)
#     compare_value_A = random_result_A['follower_count']
#     compare_value_B = random_result_B['follower_count']
#     return random_result_A, random_result_B, compare_value_A, compare_value_B

def game():
    attempt = True 
    score = 0
    random_result_A = get_random_dict(data_list)
    random_result_B = get_random_dict(data_list)
    while random_result_A == random_result_B:
        random_result_B = get_random_dict(data_list)
    compare_value_A = random_result_A['follower_count']
    compare_value_B = random_result_B['follower_count']
    def listing():
        random_result_A = get_random_dict(data_list)
        random_result_B = get_random_dict(data_list)
        compare_value_A = random_result_A['follower_count']
        compare_value_B = random_result_B['follower_count']
        print(f"Compare A: {compare_value_A} {random_result_A['name']}, {random_result_A['description']} from {random_result_A['country']}")
        print(vs)
        print(f"Against B:{compare_value_B} {random_result_B['name']}, {random_result_B['description']} from {random_result_B['country']}")
    
    while attempt:
        listing()
        user_input = input("Who has more followers? Type A/B: ").lower()    
        if (compare_value_A > compare_value_B and user_input == 'a') or (compare_value_A < compare_value_B and user_input == "b"):
            score += 1
            print("you'r right")
        else:
            print(f"Sorry that's wrong. Your score is {score}")
        print (score)

game()