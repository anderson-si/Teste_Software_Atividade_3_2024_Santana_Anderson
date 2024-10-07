# TTT.py

from random import randrange
import time

# Variáveis globais
keep_going = True
# Símbolos para jogo solo
s1 = "X"
s2 = "O"
# Símbolos para jogo multiplayer
m1 = "U"
m2 = "N"
# Tabuleiro
place = ["-"] * 9


# Funções para o jogo solo

def solo_show():
    print("\n\n\n\n\n\n\n")
    print(f"[{place[0]}][{place[1]}][{place[2]}]")
    print(f"[{place[3]}][{place[4]}][{place[5]}]")
    print(f"[{place[6]}][{place[7]}][{place[8]}]\n\n\n")


def player_turn():
    global s1, keep_going
    pchoice = input("Your turn! Enter a number from 1 - 9 to take that slot!   ").strip()
    # Fool-proof
    while pchoice not in [str(i) for i in range(1, 10)]:
        pchoice = input("Please enter a valid number between 1 and 9 (inclusive):   ").strip()
    pchoice = int(pchoice)
    placement = pchoice - 1
    if place[placement] == "-":
        place[placement] = s1
        solo_show()
    else:
        print("Sorry, that spot is taken!")
        player_turn()


def bot_turn2():
    global keep_going
    # Bot offense
    offense_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontais
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticais
        (0, 4, 8), (2, 4, 6)              # Diagonais
    ]
    
    # Tentativa de ataque
    for pattern in offense_patterns:
        a, b, c = pattern
        if place[a] == place[b] == s2 and place[c] == "-":
            place[c] = s2
            solo_show()
            return
        if place[a] == place[c] == s2 and place[b] == "-":
            place[b] = s2
            solo_show()
            return
        if place[b] == place[c] == s2 and place[a] == "-":
            place[a] = s2
            solo_show()
            return
    
    # Tentativa de defesa
    for pattern in offense_patterns:
        a, b, c = pattern
        if place[a] == place[b] == s1 and place[c] == "-":
            place[c] = s2
            solo_show()
            return
        if place[a] == place[c] == s1 and place[b] == "-":
            place[b] = s2
            solo_show()
            return
        if place[b] == place[c] == s1 and place[a] == "-":
            place[a] = s2
            solo_show()
            return
    
    # Se não puder atacar ou defender, escolher posição aleatória
    empty_slots = [i for i, spot in enumerate(place) if spot == "-"]
    if empty_slots:
        resort = randrange(len(empty_slots))
        chosen_slot = empty_slots[resort]
        place[chosen_slot] = s2
        solo_show()


def horizontal_win():
    global keep_going
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == s1:
            keep_going = False
            print("You win!")
            return True
    return False


def vertical_win():
    global keep_going
    wins = [
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == s1:
            keep_going = False
            print("You win!")
            return True
    return False


def diagonal_win():
    global keep_going
    wins = [
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == s1:
            keep_going = False
            print("You win!")
            return True
    return False


def horizontal_loss():
    global keep_going
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == s2:
            keep_going = False
            print("You lose!")
            return True
    return False


def vertical_loss():
    global keep_going
    wins = [
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == s2:
            keep_going = False
            print("You lose!")
            return True
    return False


def diagonal_loss():
    global keep_going
    wins = [
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == s2:
            keep_going = False
            print("You lose!")
            return True
    return False


def solo_tie():
    global keep_going
    if "-" not in place:
        print("It's a tie!")
        keep_going = False
        return True
    return False


def solo_game():
    global keep_going, place
    keep_going = True
    place = ["-"] * 9

    print("\n\n\n\n\n\n\n\n\n")
    print("T I C   T A C   T O E - Single player")
    solo_show()

    while keep_going:
        time.sleep(1)
        player_turn()
        if horizontal_win() or vertical_win() or diagonal_win() or solo_tie():
            break
        if keep_going:
            time.sleep(1)
            bot_turn2()
            if horizontal_loss() or vertical_loss() or diagonal_loss() or solo_tie():
                break


# Funções para o jogo multiplayer

def multi_show():
    print("\n\n\n\n\n\n\n")
    print(f"[{place[0]}][{place[1]}][{place[2]}]")
    print(f"[{place[3]}][{place[4]}][{place[5]}]")
    print(f"[{place[6]}][{place[7]}][{place[8]}]\n\n\n")


def p1_turn():
    global m1
    while True:
        pchoice = input("[Player 1] Enter a number from 1 - 9 to take that slot!   ").strip()
        if pchoice in [str(i) for i in range(1, 10)]:
            placement = int(pchoice) - 1
            if place[placement] == "-":
                place[placement] = m1
                multi_show()
                break
            else:
                print("Sorry, that spot is taken!")
        else:
            print("Please enter a valid number between 1 and 9 (inclusive).")


def player2_turn():
    global m2
    while True:
        pchoice = input("[Player 2] Enter a number from 1 - 9 to take that slot!   ").strip()
        if pchoice in [str(i) for i in range(1, 10)]:
            placement = int(pchoice) - 1
            if place[placement] == "-":
                place[placement] = m2
                multi_show()
                break
            else:
                print("Sorry, that spot is taken!")
        else:
            print("Please enter a valid number between 1 and 9 (inclusive).")


def p1_hwin():
    global keep_going
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == m1:
            keep_going = False
            print("Player 1 wins!")
            return True
    return False


def p1_vwin():
    global keep_going
    wins = [
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == m1:
            keep_going = False
            print("Player 1 wins!")
            return True
    return False


def p1_dwin():
    global keep_going
    wins = [
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == m1:
            keep_going = False
            print("Player 1 wins!")
            return True
    return False


def p2_hwin():
    global keep_going
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == m2:
            keep_going = False
            print("Player 2 wins!")
            return True
    return False


def p2_vwin():
    global keep_going
    wins = [
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == m2:
            keep_going = False
            print("Player 2 wins!")
            return True
    return False


def p2_dwin():
    global keep_going
    wins = [
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in wins:
        if place[a] == place[b] == place[c] == m2:
            keep_going = False
            print("Player 2 wins!")
            return True
    return False


def multi_tie():
    global keep_going
    if "-" not in place:
        print("It's a tie!")
        keep_going = False
        return True
    return False


def multi_game():
    global m1, m2, keep_going, place
    keep_going = True
    place = ["-"] * 9
    print("\n\n\n\n\n\n\n\n\n T I C   T A C   T O E - Multiplayer \n\n\n")
    print("Player 1, what symbol would you like to use? \n")
    symbol_choose = input("Enter [O] or [X]:   ").strip().lower()

    while symbol_choose not in ["o", "x"]:
        symbol_choose = input("Enter [O] or [X]:   ").strip().lower()

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

    # Estabelecer tabuleiro
    multi_show()

    while keep_going:
        time.sleep(1)
        p1_turn()
        if p1_hwin() or p1_vwin() or p1_dwin() or multi_tie():
            break
        if keep_going:
            time.sleep(1)
            player2_turn()
            if p2_hwin() or p2_vwin() or p2_dwin() or multi_tie():
                break


# Função do menu

def show_tutorial():
    print("\n\n\n")
    print("This is how to play Tic-Tac-Toe!\n")
    time.sleep(3)
    print("The goal of the game is to get three in a row of your pieces (either X or O).")
    print("You can get three in a row horizontally, vertically, or diagonally.\n")
    time.sleep(7)
    print("[1][2][3]\n[4][5][6]\n[7][8][9]\n")
    time.sleep(3)
    print("Entering digits from 1-9 will put your piece on the board.\n\n\n\n")
    time.sleep(2)


def choose_game_mode():
    while True:
        game_choose = input("\nInput [1] to play against a bot, or [2] to play with a partner:   ").strip()
        if game_choose in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")
    if game_choose == "1":
        solo_game()
    elif game_choose == "2":
        multi_game()
    time.sleep(5)


def menu():
    global keep_going
    while True:
        print("\n -----======= T I C   T A C   T O E =======----- \n\n ")
        menu_choice = input("Input [P] to play, or [T] for the tutorial:   ").strip().lower()
        while menu_choice not in ["t", "p"]:
            menu_choice = input("Input [P] to play, or [T] for the tutorial:   ").strip().lower()

        if menu_choice == "t":
            show_tutorial()
            continue

        if menu_choice == "p":
            time.sleep(0.5)
            choose_game_mode()
            continue


# Função principal

def main():
    menu()


if __name__ == "__main__":
    main()
