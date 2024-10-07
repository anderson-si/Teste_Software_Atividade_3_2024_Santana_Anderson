

# Tic Tac Toe
# started on Sept. 7, 2022
# finished on Sept. 22, 2022

from random import randrange
import time
keep_going = True
# pieces for solo game
s1 = "X"
s2 = "O"
# pieces for multi game
m1 = "U"
m2 = "N"


def solo_game():
    global s1
    global s2
    global keep_going
    keep_going = True

    print("\n\n\n\n\n\n\n\n\n")
    print("T I C   T A C   T O E - Single player")
    place = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    # solo board
    def solo_show():
        print("\n\n\n\n\n\n\n")
        print("[" + place[0] + "][" + place[1] + "][" + place[2] + "]")
        print("[" + place[3] + "][" + place[4] + "][" + place[5] + "]")
        print("[" + place[6] + "][" + place[7] + "][" + place[8] + "]")
        print("\n\n\n")

    # player turn
    def player_turn():
        global s1
        pchoice = input("Your turn! Enter a number from 1 - 9 to take that slot!   ")
        pchoice.rstrip()
        # fool-proof
        while pchoice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pchoice = input("Please enter a valid number between 1 and 9 (inclusive):   ")
        pchoice = int(pchoice)
        placement = pchoice - 1
        if place[0 + placement] == "-":
            place[0 + placement] = s1
            solo_show()
        else:
            print("Sorry, that spot is taken!")
            player_turn()

    def bot_turn2():
        # bot offence
        # horizontal offence
        # row 1
        if place[0] == place[1] == s2 and place[2] == "-":
            place[2] = s2

        elif place[0] == place[2] == s2 and place[1] == "-":
            place[1] = s2

        elif place[1] == place[2] == s2 and place[0] == "-":
            place[0] = s2

        # row 2
        elif place[3] == place[4] == s2 and place[5] == "-":
            place[5] = s2

        elif place[3] == place[5] == s2 and place[4] == "-":
            place[4] = s2

        elif place[4] == place[5] == s2 and place[3] == "-":
            place[3] = s2

        # row 3
        elif place[6] == place[7] == s2 and place[8] == "-":
            place[8] = s2

        elif place[6] == place[8] == s2 and place[7] == "-":
            place[7] = s2

        elif place[7] == place[8] == s2 and place[6] == "-":
            place[6] = s2

        # vertical offence
        # column 1
        elif place[0] == place[3] == s2 and place[6] == "-":
            place[6] = s2

        elif place[0] == place[6] == s2 and place[3] == "-":
            place[3] = s2

        elif place[3] == place[6] == s2 and place[0] == "-":
            place[0] = s2

        # column 2
        elif place[1] == place[4] == s2 and place[7] == "-":
            place[7] = s2

        elif place[1] == place[7] == s2 and place[4] == "-":
            place[4] = s2

        elif place[4] == place[7] == s2 and place[1] == "-":
            place[1] = s2

        # column 3
        elif place[2] == place[5] == s2 and place[8] == "-":
            place[8] = s2

        elif place[2] == place[8] == s2 and place[5] == "-":
            place[5] = s2

        elif place[5] == place[8] == s2 and place[2] == "-":
            place[2] = s2

        # diagonal offence
        # 1 -> 9
        elif place[0] == place[4] == s2 and place[8] == "-":
            place[8] = s2

        elif place[0] == place[8] == s2 and place[4] == "-":
            place[4] = s2

        elif place[4] == place[8] == s2 and place[0] == "-":
            place[0] = s2

        # 3 -> 7
        elif place[2] == place[4] == s2 and place[6] == "-":
            place[6] = s2

        elif place[2] == place[6] == s2 and place[4] == "-":
            place[4] = s2

        elif place[4] == place[6] == s2 and place[2] == "-":
            place[2] = s2

        # bot defence
        # horizontal defence
        elif place[0] == place[1] == s1 and place[2] == "-":
            place[2] = s2

        elif place[0] == place[2] == s1 and place[1] == "-":
            place[1] = s2

        elif place[1] == place[2] == s1 and place[0] == "-":
            place[0] = s2

        # row 2
        elif place[3] == place[4] == s1 and place[5] == "-":
            place[5] = s2

        elif place[3] == place[5] == s1 and place[4] == "-":
            place[4] = s2

        elif place[4] == place[5] == s1 and place[3] == "-":
            place[3] = s2

        # row 3
        elif place[6] == place[7] == s1 and place[8] == "-":
            place[8] = s2

        elif place[6] == place[8] == s1 and place[7] == "-":
            place[7] = s2

        elif place[7] == place[8] == s1 and place[6] == "-":
            place[6] = s2

        # vertical defence
        # column 1
        elif place[0] == place[3] == s1 and place[6] == "-":
            place[6] = s2

        elif place[0] == place[6] == s1 and place[3] == "-":
            place[3] = s2

        elif place[3] == place[6] == s1 and place[0] == "-":
            place[0] = s2

        # column 2
        elif place[1] == place[4] == s1 and place[7] == "-":
            place[7] = s2

        elif place[1] == place[7] == s1 and place[4] == "-":
            place[4] = s2

        elif place[4] == place[7] == s1 and place[1] == "-":
            place[1] = s2

        # column 3
        elif place[2] == place[5] == s1 and place[8] == "-":
            place[8] = s2

        elif place[2] == place[8] == s1 and place[5] == "-":
            place[5] = s2

        elif place[5] == place[8] == s1 and place[2] == "-":
            place[2] = s2

        # diagonal defence
        # 1 -> 9
        elif place[0] == place[4] == s1 and place[8] == "-":
            place[8] = s2

        elif place[0] == place[8] == s1 and place[4] == "-":
            place[4] = s2

        elif place[4] == place[8] == s1 and place[0] == "-":
            place[0] = s2

        # 3 -> 7
        elif place[2] == place[4] == s1 and place[6] == "-":
            place[6] = s2

        elif place[2] == place[6] == s1 and place[4] == "-":
            place[4] = s2

        elif place[4] == place[6] == s1 and place[2] == "-":
            place[2] = s2

        # if cant defend or attack, choose a random slot
        else:
            turnend = False
            while not turnend:
                resort = randrange(9)
                if place[resort] == "-":
                    place[resort] = s2
                    turnend = True

    # win checks
    def horizontal_win():
        global keep_going
        if place[0] == place[1] == place[2] == s1:
            keep_going = False
            print("you win!")
        if place[3] == place[4] == place[5] == s1:
            keep_going = False
            print("you win!")
        if place[6] == place[7] == place[8] == s1:
            keep_going = False
            print("you win!")

    def vertical_win():
        global keep_going
        if place[0] == place[3] == place[6] == s1:
            keep_going = False
            print("you win!")
        if place[1] == place[4] == place[7] == s1:
            keep_going = False
            print("you win!")
        if place[2] == place[5] == place[8] == s1:
            keep_going = False
            print("you win!")

    def diagonal_win():
        global keep_going
        if place[0] == place[4] == place[8] == s1:
            keep_going = False
            print("you win!")
        if place[2] == place[4] == place[6] == s1:
            keep_going = False
            print("you win!")

    # loss checks
    def horizontal_loss():
        global keep_going
        if place[0] == place[1] == place[2] == s2:
            keep_going = False
            print("you lose!")
        if place[3] == place[4] == place[5] == s2:
            keep_going = False
            print("you lose!")
        if place[6] == place[7] == place[8] == s2:
            keep_going = False
            print("you lose!")

    def vertical_loss():
        global keep_going
        if place[0] == place[3] == place[6] == s2:
            keep_going = False
            print("you lose!")
        if place[1] == place[4] == place[7] == s2:
            keep_going = False
            print("you lose!")
        if place[2] == place[5] == place[8] == s2:
            keep_going = False
            print("you lose!")

    def diagonal_loss():
        global keep_going
        if place[0] == place[4] == place[8] == s2:
            keep_going = False
            print("you lose!")
        if place[2] == place[4] == place[6] == s2:
            keep_going = False
            print("you lose!")

    def solo_tie():
        global keep_going
        if "-" not in place:
            print("It's a tie!")
            keep_going = False

    # game administrator
    solo_show()
    while keep_going:
        time.sleep(1)
        player_turn()
        horizontal_win()
        vertical_win()
        diagonal_win()
        solo_tie()
        if keep_going:
            time.sleep(1)
            bot_turn2()
            solo_show()
            horizontal_loss()
            vertical_loss()
            diagonal_loss()
            solo_tie()


def multi_game():
    global m1
    global m2
    global keep_going
    print("\n\n\n\n\n\n\n\n\n T I C   T A C   T O E - Multiplayer \n\n\n")
    print("Player 1, what symbol would you like to use? \n")
    symbol_choose = input("Enter [O] or [X]:   ")
    symbol_choose = symbol_choose.lower()

    while symbol_choose not in ["o", "x"]:
        symbol_choose = input("Enter [O] or [X]:   ")
        symbol_choose.lower()

    if symbol_choose == "o":
        print("Player 1 has chosen the symbol 'O'. Player 2 will use the symbol 'X'")
        m1 = "O"
        m2 = "X"
        time.sleep(2)
    elif symbol_choose == "x":
        print("Player 1 has chosen the symbol 'X'. Player 2 will use the symbol 'O'")
        m1 = "X"
        m2 = "O"
        time.sleep(2)

    # establish board
    place = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    def multi_show():
        print("\n\n\n\n\n\n\n")
        print("[" + place[0] + "][" + place[1] + "][" + place[2] + "]")
        print("[" + place[3] + "][" + place[4] + "][" + place[5] + "]")
        print("[" + place[6] + "][" + place[7] + "][" + place[8] + "]")
        print("\n\n\n")

    def p1_turn():
        global m1
        pchoice = input("[X]'s turn! Enter a number from 1 - 9 to take that slot!   ")
        pchoice.rstrip()
        # fool-proof
        while pchoice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pchoice = input("Please enter a valid number between 1 and 9 (inclusive):   ")
        pchoice = int(pchoice)
        placement = pchoice - 1
        if place[0 + placement] == "-":
            place[0 + placement] = m1
            multi_show()
        else:
            print("Sorry, that spot is taken!")
            p1_turn()

    def player2_turn():
        global m2
        pchoice = input("[O]'s turn! Enter a number from 1 - 9 to take that slot!   ")
        pchoice.rstrip()
        # fool-proof
        while pchoice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pchoice = input("Please enter a valid number between 1 and 9 (inclusive):   ")
        pchoice = int(pchoice)
        placement = pchoice - 1
        if place[0 + placement] == "-":
            place[0 + placement] = m2
            multi_show()
        else:
            print("Sorry, that spot is taken!")
            player2_turn()

    def p1_hwin():
        global keep_going
        if place[0] == place[1] == place[2] == m1:
            keep_going = False
            print("Player 1 wins!")
        if place[3] == place[4] == place[5] == m1:
            keep_going = False
            print("Player 1 wins!")
        if place[6] == place[7] == place[8] == m1:
            keep_going = False
            print("Player 1 wins!")

    def p1_vwin():
        global keep_going
        if place[0] == place[3] == place[6] == m1:
            keep_going = False
            print("Player 1 wins!")
        if place[1] == place[4] == place[7] == m1:
            keep_going = False
            print("Player 1 wins!")
        if place[2] == place[5] == place[8] == m1:
            keep_going = False
            print("Player 1 wins!")

    def p1_dwin():
        global keep_going
        if place[0] == place[4] == place[8] == m1:
            keep_going = False
            print("Player 1 wins!")
        if place[2] == place[4] == place[6] == m1:
            keep_going = False
            print("Player 1 wins!")

    # player 2 wins
    def p2_hwin():
        global keep_going
        if place[0] == place[1] == place[2] == m2:
            keep_going = False
            print("Player 2 wins!")
        if place[3] == place[4] == place[5] == m2:
            keep_going = False
            print("Player 2 wins!")
        if place[6] == place[7] == place[8] == m2:
            keep_going = False
            print("Player 2 wins!")

    def p2_vwin():
        global keep_going
        if place[0] == place[3] == place[6] == m2:
            keep_going = False
            print("Player 2 wins!")
        if place[1] == place[4] == place[7] == m2:
            keep_going = False
            print("Player 2 wins!")
        if place[2] == place[5] == place[8] == m2:
            keep_going = False
            print("Player 2 wins!")

    def p2_dwin():
        global keep_going
        if place[0] == place[4] == place[8] == m2:
            keep_going = False
            print("Player 2 wins!")
        if place[2] == place[4] == place[6] == m2:
            keep_going = False
            print("Player 2 wins!")

    def multi_tie():
        global keep_going
        if "-" not in place:
            print("It's a tie!")
            keep_going = False

    # game administrator
    multi_show()
    while keep_going:
        time.sleep(1)
        p1_turn()
        p1_hwin()
        p1_vwin()
        p1_dwin()
        multi_tie()
        if keep_going:
            time.sleep(1)
            player2_turn()
            multi_show()
            p2_hwin()
            p2_vwin()
            p2_dwin()


def menu():
    global keep_going

    print("\n -----======= T I C   T A C   T O E =======----- \n\n ")
    menu_choice = input("Input [P] to play, or [T] for the tutorial:   ")
    menu_choice = menu_choice.lower()
    while menu_choice not in ["t", "p"]:
        menu_choice = input("Input [P] to play, or [T] for the tutorial:   ")

    if menu_choice == "t":
        print("\n\n\n")
        print("This is how to play Tic-Tac-Toe!\n")
        time.sleep(3)
        print("The goal of the game is to get three in a row of your pieces (either X or O). \n"
              "You can get three in a row horizontally, vertically, or diagonally.\n")
        time.sleep(7)
        print("[1][2][3]\n[4][5][6]\n[7][8][9]\n")
        time.sleep(3)
        print("Entering digits from 1-9 will put your piece on the board.\n\n\n\n")

        menu()

    if menu_choice == "p":
        time.sleep(0.5)
        game_choose = input("\nInput [1] to play against a bot, or [2] to play with a partner:   ")
        while game_choose not in ["1", "2"]:
            game_choose = input("\nInput [1] to play against a bot, or [2] to play with a partner:   ")
        game_choose = int(game_choose)

        if game_choose == 1:
            solo_game()
            time.sleep(5)
            menu()

        if game_choose == 2:
            multi_game()
            time.sleep(5)
            menu()


if __name__ == "__main__":
    menu()

