import random

player1wins = 0
player2wins = 0

while True:
    player1 = input("Select Rock, Paper, or Scissor: ").lower()
    player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
    print("Player 2 selected:", player2)

    if player1 == "rock" and player2 == "paper":
        print("Player 2 Won")
        player2_wins += 1
    elif player1 == "paper" and player2 == "scissor":
        print("Player 2 Won")
        player2_wins += 1
    elif player1 == "scissor" and player2 == "rock":
        print("Player 2 Won")
        player2_wins += 1
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 1 Won")
        player1wins += 1

    print(f"Player 1 Wins: {player1wins}, Player 2 Wins: {player2wins}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing. Goodbye!")
        break
