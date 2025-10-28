# rock paper scissors function

def RPSgame():
    import random
    while True:
        hand_signals=["rock", "paper", "scissors"]
        print(f"Rock...\nPaper...\nScissors...")
        player_signal=input("Pick your hand signal:").lower()
        print("Shoot!")
        if player_signal in hand_signals:
            cpu_signal=random.choice(hand_signals)
            print(f"The computer picked {cpu_signal}.")
            print(f"You picked {player_signal}.")
            if cpu_signal==player_signal:
                print("Tie! Try again")
            elif player_signal=="rock":
                if cpu_signal=="scissors":
                    print("You win!")
                else:
                    print("You Lose!")
            elif player_signal=="scissors":
                if cpu_signal=="paper":
                    print("You win!")
                else:
                    print("You Lose!")
            else:
                if cpu_signal=="rock":
                    print("You win!")
                else:
                    print("You Lose!")
        else:
            print("I didn't understand that response try again.")
            continue
        loop=input("Play again? Type 'yes' or 'no':").lower()
        if loop == "yes":
            continue
        elif loop== "no":
            print("Quitting...")
            break
        else:
            print("I didn't understand that response. Quitting...")
            break

RPSgame()
