import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RepeatPlayer(Player):
    def move(self):
        return 'rock'


class Randomplayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        x = input("please enter ur move: ")
        while x != "rock" and x != "paper" and x != "scissors":
            x = input("invalid move plz try again:")

        return x


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = moves[0]

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.round = 0

    def move(self):
        if (self.round == 0):
            self.round += 1
            return moves[0]
        elif self.round == 1:
            self.round += 1
            return moves[1]
        else:
            return moves[2]
            self.round = 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_game(self):
        score1 = 0
        score2 = 0

        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            # self.play_round()
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Player 1: {move1}  Player 2: {move2}")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
            print("Player1 played " + str(move1))
            print("player2 played " + str(move2))

            if beats(move1, move2):
                score1 += 1
                print("Player1 wins")
                print(score1)
            elif beats(move2, move1):
                score2 += 1
                print("player2 wins")
                print(score2)
            else:
                print("Tie")
        if score1 > score2:
            print("Player1 Wins The Game!!")
        elif score2 > score1:
            print("Player2 Wins The Game!!")
        else:
            print("Draw")
        print("Final score " + str(score1) + " for Player1 &" + str(score2) +
              " for Player2. ")

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
