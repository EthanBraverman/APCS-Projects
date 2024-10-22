import random

print("WELCOME TO ROCK, PAPER, SCISSORS!")
print("")

like_to_play = True

while like_to_play == True:
    player_score = 0
    computer_score = 0
    
    pick_options = ["rock", "paper", "scissors"]
    
    while player_score < 5 and computer_score < 5:
        player_pick_is_valid = False
        
        while player_pick_is_valid == False:
            player_pick = input("Would you like to play rock, paper, or scissors?: ")
            print("")
            
            if player_pick == pick_options[0] or player_pick == pick_options[1] or player_pick == pick_options[2]:
                player_pick_is_valid = True
            else:
                print('That is not a valid option. Please select, "rock," "paper," or "scissors."')
        
        computer_pick = random.choice(pick_options)
        print("The computer picked " + computer_pick + ".")
        
        if player_pick == "rock" and computer_pick == "rock":
            winner = "tie"
        elif player_pick == "rock" and computer_pick == "paper":
            winner = "computer"
            computer_pick = "Paper"
            action = "covers"
        elif player_pick == "rock" and computer_pick == "scissors":
            winner = "player"
            player_pick = "Rock"
            action = "smashes"
        elif player_pick == "paper" and computer_pick == "rock":
            winner = "player"
            player_pick = "Paper"
            action = "covers"
        elif player_pick == "paper" and computer_pick == "paper":
            winner = "tie"
        elif player_pick == "paper" and computer_pick == "scissors":
            winner = "computer"
            computer_pick = "Scissors"
            action = "cuts"
        elif player_pick == "scissors" and computer_pick == "rock":
            winner = "computer"
            computer_pick = "Rock"
            action = "smashes"
        elif player_pick == "scissors" and computer_pick == "paper":
            winner = "player"
            player_pick = "Scissors"
            action = "cuts"
        elif player_pick == "scissors" and computer_pick == "scissors":
            winner = "tie"
            
        if winner == "player":
            print(player_pick + " " + action + " " + computer_pick + ". The player won!")
            player_score += 1
        elif winner == "computer":
            print(computer_pick + " " + action + " " + player_pick + ". The computer won!")
            computer_score += 1
        elif winner == "tie":
            print("It was a tie.")
        
        print("")
        print("Player: " + str(player_score) + ", Computer: " + str(computer_score))
        
        print("")
        print("----------------------")
        print("")
    
    if player_score == 5:
        print("The player reached 5 points first. The player wins!")
    elif computer_score == 5:
        print("The computer reached 5 points first. The computer wins!")
    
    play_again_input_is_valid = False
    
    while play_again_input_is_valid == False:
        play_again = input("Would you like to play again? [y/n] ")
    
        if play_again == "y":
            play_again_input_is_valid = True
            print("")
            print("----------------------")
            print("")
        elif play_again == "n":
            print("")
            print("Thank you for playing.")
            like_to_play = False
            play_again_input_is_valid = True
        else:
            print("")
            print('That is not a valid option. Please answer with "y" for yes and "n" for no.')
