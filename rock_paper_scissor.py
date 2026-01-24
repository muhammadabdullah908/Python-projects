import random

choices = ["Rock", "Paper", "Scissor"]
player_score = 0
computer_score = 0

def rpsLogic(pmove, cmove):
    global player_score
    global computer_score
    if cmove == "Rock" and pmove == "Rock":
        print(f"Player:{pmove}  Computer:{cmove}")
        print()
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()
    elif cmove == "Rock" and pmove == "Paper":
        print(f"Player:{pmove}  Computer:{cmove}")
        player_score += 1
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()
    elif cmove == "Rock" and pmove == "Scissor":
        print(f"Player:{pmove}  Computer:{cmove}")
        computer_score += 1
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()
    elif cmove == "Scissor" and pmove == "Scissor":
        print(f"Player:{pmove}  Computer:{cmove}")
        print()
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()
    elif cmove == "Scissor" and pmove == "Paper":
        print(f"Player:{pmove}  Computer:{cmove}")
        computer_score += 1
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()
    elif cmove == "Scissor" and pmove == "Rock":
        print(f"Player:{pmove}  Computer:{cmove}")
        player_score += 1
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()
    elif cmove == "Paper" and pmove == "Rock":
        print(f"Player:{pmove}  Computer:{cmove}")
        computer_score += 1
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()
    elif cmove == "Paper" and pmove == "Paper":
        print(f"Player:{pmove}  Computer:{cmove}")
        print()
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()
    elif cmove == "Paper" and pmove == "Scissor":
        print(f"Player:{pmove}  Computer:{cmove}")
        player_score += 1
        print(f"Computer:{computer_score}  Player:{player_score}")
        print()

def finalScore():
    if player_score > computer_score:
        print("Player won!")
    elif player_score < computer_score:
        print("Computer won!")
    else:
        print("It's a tie!")

def play():
    rounds = 5
    current = 1

    # normalization: accept many user input forms and map to your choices list
    normalize = {
        "rock": "Rock",
        "paper": "Paper",
        "scissor": "Scissor",
        "scissors": "Scissor"
    }

    while current <= rounds:
        raw = input("Rock, Paper or Scissors? ").strip().lower()

        if raw not in normalize:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue  # ask again without advancing the round

        player_choice = normalize[raw]
        computer_choice = choices[random.randint(0, 2)]
        rpsLogic(player_choice, computer_choice)
        current += 1

    finalScore()

play()
