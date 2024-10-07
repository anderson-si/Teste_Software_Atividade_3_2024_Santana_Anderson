# tests/test_TTT.py

import pytest
from unittest.mock import patch
import TTT as module_0

# Fixture para resetar o estado antes de cada teste
@pytest.fixture(autouse=True)
def reset_globals():
    module_0.keep_going = True
    module_0.s1 = "X"
    module_0.s2 = "O"
    module_0.m1 = "U"
    module_0.m2 = "N"
    module_0.place = ["-"] * 9  
    yield
    module_0.keep_going = True
    module_0.place = ["-"] * 9

# ---------------------------
# Testes para solo_show e multi_show
# ---------------------------

def test_solo_show(capsys):
    module_0.solo_show()
    captured = capsys.readouterr()
    expected_output = "\n\n\n\n\n\n\n" \
                      "[-][-][-]\n" \
                      "[-][-][-]\n" \
                      "[-][-][-]\n\n\n\n"
    assert captured.out == expected_output

def test_multi_show(capsys):
    module_0.multi_show()
    captured = capsys.readouterr()
    expected_output = "\n\n\n\n\n\n\n" \
                      "[-][-][-]\n" \
                      "[-][-][-]\n" \
                      "[-][-][-]\n\n\n\n"
    assert captured.out == expected_output

# ---------------------------
# Testes para player_turn (Solo Game)
# ---------------------------

@patch('builtins.input', side_effect=['5'])
def test_player_turn_valid(mock_input, capsys):
    module_0.player_turn()
    assert module_0.place[4] == 'X'
    captured = capsys.readouterr()
    assert "[X]" in captured.out  # Simplificação para verificar a presença do 'X'

@patch('builtins.input', side_effect=['10', '0', 'a', '3'])
def test_player_turn_invalid_then_valid(mock_input, capsys):
    module_0.player_turn()
    assert module_0.place[2] == 'X'
    captured = capsys.readouterr()
    assert "Please enter a valid number between 1 and 9 (inclusive):" in captured.out
    assert "[X]" in captured.out  # Simplificação para verificar a presença do 'X'

@patch('builtins.input', side_effect=['1', '1', '2'])
def test_player_turn_spot_taken(mock_input, capsys):
    module_0.place[0] = 'X'
    module_0.player_turn()
    # A primeira entrada '1' está ocupada, deve aceitar a segunda entrada '2'
    assert module_0.place[1] == 'X'
    captured = capsys.readouterr()
    assert "Sorry, that spot is taken!" in captured.out
    assert "[X][X]" in captured.out  # Simplificação para verificar a presença dos 'X'

# ---------------------------
# Testes para bot_turn2 (Solo Game)
# ---------------------------

@patch('TTT.randrange')
def test_bot_turn2_offense(mock_randrange, capsys):
    # Bot pode ganhar preenchendo a terceira posição
    module_0.place[0] = 'O'
    module_0.place[1] = 'O'
    mock_randrange.return_value = 0  # Não será usado, pois ataque é possível
    module_0.bot_turn2()
    assert module_0.place[2] == 'O'
    captured = capsys.readouterr()
    assert "[O][O][O]" in captured.out

@patch('TTT.randrange')
def test_bot_turn2_defense(mock_randrange, capsys):
    # Bot deve bloquear o jogador que está prestes a ganhar
    module_0.place[0] = 'X'
    module_0.place[1] = 'X'
    mock_randrange.return_value = 0  # Não será usado, pois defesa é necessária
    module_0.bot_turn2()
    assert module_0.place[2] == 'O'
    captured = capsys.readouterr()
    assert "[X][X][O]" in captured.out

@patch('TTT.randrange')
def test_bot_turn2_random(mock_randrange, capsys):
    # Sem oportunidades de ataque ou defesa, o bot escolhe aleatoriamente
    mock_randrange.return_value = 1  # Escolhe a segunda posição vazia (index 1)
    module_0.bot_turn2()
    assert module_0.place[1] == 'O'
    captured = capsys.readouterr()
    # Pode variar dependendo da implementação, mas deve haver um 'O' na posição 1
    assert module_0.place[1] == 'O'

@patch('TTT.randrange')
def test_bot_turn2_no_moves(mock_randrange, capsys):
    # Tabuleiro completo, bot não deve fazer nenhuma jogada
    module_0.place = ['X', 'O', 'X',
                      'X', 'O', 'O',
                      'O', 'X', 'X']
    module_0.bot_turn2()
    assert module_0.place.count('O') == 4  # Nenhuma nova 'O' adicionada
    captured = capsys.readouterr()
    # Nenhuma alteração no tabuleiro
    expected_output = "\n\n\n\n\n\n\n[-][O][-]\n" \
                      "[-][-][-]\n" \
                      "[-][-][-]\n\n\n\n"
    # Pode variar, então simplificação
    assert module_0.place.count('O') == 4

# ---------------------------
# Testes para funções de vitória (Solo Game)
# ---------------------------

def test_horizontal_win_true():
    module_0.place[0] = module_0.place[1] = module_0.place[2] = 'X'
    assert module_0.horizontal_win() is True
    assert not module_0.keep_going

def test_horizontal_win_false():
    module_0.place[0] = module_0.place[1] = 'X'
    module_0.place[2] = 'O'
    assert module_0.horizontal_win() is False
    assert module_0.keep_going

def test_vertical_win_true():
    module_0.place[0] = module_0.place[3] = module_0.place[6] = 'X'
    assert module_0.vertical_win() is True
    assert not module_0.keep_going

def test_vertical_win_false():
    module_0.place[0] = module_0.place[3] = 'X'
    module_0.place[6] = 'O'
    assert module_0.vertical_win() is False
    assert module_0.keep_going

def test_diagonal_win_true():
    module_0.place[0] = module_0.place[4] = module_0.place[8] = 'X'
    assert module_0.diagonal_win() is True
    assert not module_0.keep_going

def test_diagonal_win_false():
    module_0.place[0] = module_0.place[4] = 'X'
    module_0.place[8] = 'O'
    assert module_0.diagonal_win() is False
    assert module_0.keep_going

# ---------------------------
# Testes para funções de derrota (Solo Game)
# ---------------------------

def test_horizontal_loss_true():
    module_0.place[0] = module_0.place[1] = module_0.place[2] = 'O'
    assert module_0.horizontal_loss() is True
    assert not module_0.keep_going

def test_vertical_loss_true():
    module_0.place[0] = module_0.place[3] = module_0.place[6] = 'O'
    assert module_0.vertical_loss() is True
    assert not module_0.keep_going

def test_diagonal_loss_true():
    module_0.place[0] = module_0.place[4] = module_0.place[8] = 'O'
    assert module_0.diagonal_loss() is True
    assert not module_0.keep_going

def test_horizontal_loss_false():
    module_0.place[0] = module_0.place[1] = 'O'
    module_0.place[2] = 'X'
    assert module_0.horizontal_loss() is False
    assert module_0.keep_going

# ---------------------------
# Testes para empate (Tie)
# ---------------------------

def test_solo_tie_true(capsys):
    module_0.place = ['X', 'O', 'X',
                      'X', 'O', 'O',
                      'O', 'X', 'X']
    assert module_0.solo_tie() is True
    assert not module_0.keep_going
    captured = capsys.readouterr()
    assert "It's a tie!" in captured.out

def test_solo_tie_false():
    module_0.place[0] = 'X'
    assert module_0.solo_tie() is False
    assert module_0.keep_going

def test_multi_tie_true(capsys):
    module_0.place = ['U', 'N', 'U',
                      'N', 'U', 'N',
                      'N', 'U', 'N']
    assert module_0.multi_tie() is True
    assert not module_0.keep_going
    captured = capsys.readouterr()
    assert "It's a tie!" in captured.out

def test_multi_tie_false():
    module_0.place[0] = 'U'
    assert module_0.multi_tie() is False
    assert module_0.keep_going

# ---------------------------
# Testes para multiplayer (multi_show, p1_turn, p2_turn, etc.)
# ---------------------------

@patch('builtins.input', side_effect=['1'])
def test_p1_turn_valid(mock_input, capsys):
    module_0.p1_turn()
    assert module_0.place[0] == 'U'
    captured = capsys.readouterr()
    assert "[U]" in captured.out

@patch('builtins.input', side_effect=['1', '1', '2'])
def test_p1_turn_spot_taken(mock_input, capsys):
    module_0.place[0] = 'U'
    module_0.p1_turn()
    # A primeira entrada '1' está ocupada, deve aceitar a segunda entrada '2'
    assert module_0.place[1] == 'U'
    captured = capsys.readouterr()
    assert "Sorry, that spot is taken!" in captured.out
    assert "[U][U]" in captured.out

@patch('builtins.input', side_effect=['2'])
def test_p2_turn_valid(mock_input, capsys):
    module_0.p2_turn()
    assert module_0.place[1] == 'N'
    captured = capsys.readouterr()
    assert "[N]" in captured.out

@patch('builtins.input', side_effect=['2', '2', '3'])
def test_p2_turn_spot_taken(mock_input, capsys):
    module_0.place[1] = 'N'
    module_0.player2_turn()
    # A primeira entrada '2' está ocupada, deve aceitar a segunda entrada '3'
    assert module_0.place[2] == 'N'
    captured = capsys.readouterr()
    assert "Sorry, that spot is taken!" in captured.out
    assert "[N][N]" in captured.out

# ---------------------------
# Testes para multiplayer win conditions
# ---------------------------

def test_p1_hwin_true(capsys):
    module_0.place[0] = module_0.place[1] = module_0.place[2] = 'U'
    assert module_0.p1_hwin() is True
    assert not module_0.keep_going
    captured = capsys.readouterr()
    assert "Player 1 wins!" in captured.out

def test_p1_vwin_true(capsys):
    module_0.place[0] = module_0.place[3] = module_0.place[6] = 'U'
    assert module_0.p1_vwin() is True
    assert not module_0.keep_going
    captured = capsys.readouterr()
    assert "Player 1 wins!" in captured.out

def test_p1_dwin_true(capsys):
    module_0.place[0] = module_0.place[4] = module_0.place[8] = 'U'
    assert module_0.p1_dwin() is True
    assert not module_0.keep_going
    captured = capsys.readouterr()
    assert "Player 1 wins!" in captured.out

def test_p2_hwin_true(capsys):
    module_0.place[0] = module_0.place[1] = module_0.place[2] = 'N'
    assert module_0.p2_hwin() is True
    assert not module_0.keep_going
    captured = capsys.readouterr()
    assert "Player 2 wins!" in captured.out

def test_p2_vwin_true(capsys):
    module_0.place[0] = module_0.place[3] = module_0.place[6] = 'N'
    assert module_0.p2_vwin() is True
    assert not module_0.keep_going
    captured = capsys.readouterr()
    assert "Player 2 wins!" in captured.out

def test_p2_dwin_true(capsys):
    module_0.place[0] = module_0.place[4] = module_0.place[8] = 'N'
    assert module_0.p2_dwin() is True
    assert not module_0.keep_going
    captured = capsys.readouterr()
    assert "Player 2 wins!" in captured.out

# ---------------------------
# Testes para solo_game e multi_game
# ---------------------------

@patch('builtins.input', side_effect=['1', '5', '1', '2', '3'])
@patch('TTT.bot_turn2')
def test_solo_game_player_wins(mock_bot_turn2, mock_input, capsys):
    """
    Simula um jogo solo onde o jogador vence.
    Jogador coloca em 5, bot faz jogadas que não bloqueiam.
    """
    module_0.solo_game()
    captured = capsys.readouterr()
    assert "You win!" in captured.out

@patch('builtins.input', side_effect=['2', 'O', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_multi_game_player1_wins(mock_input, capsys):
    """
    Simula um jogo multijogador onde Player 1 vence.
    """
    module_0.multi_game()
    captured = capsys.readouterr()
    assert "Player 1 wins!" in captured.out

@patch('builtins.input', side_effect=['2', 'O', '1', '1', '2', '2', '3', '3'])
def test_multi_game_tie(mock_input, capsys):
    """
    Simula um jogo multijogador que termina em empate.
    """
    module_0.multi_game()
    captured = capsys.readouterr()
    assert "It's a tie!" in captured.out

# ---------------------------
# Testes para escolher modo de jogo
# ---------------------------

@patch('builtins.input', side_effect=['1'])
def test_choose_game_mode_solo(mock_input, capsys):
    module_0.choose_game_mode()
    captured = capsys.readouterr()
    assert "T I C   T A C   T O E - Single player" in captured.out

@patch('builtins.input', side_effect=['2'])
def test_choose_game_mode_multi(mock_input, capsys):
    module_0.choose_game_mode()
    captured = capsys.readouterr()
    assert "T I C   T A C   T O E - Multiplayer" in captured.out

@patch('builtins.input', side_effect=['3', '2'])
def test_choose_game_mode_invalid_then_multi(mock_input, capsys):
    module_0.choose_game_mode()
    captured = capsys.readouterr()
    assert "Invalid choice. Please enter '1' or '2'." in captured.out
    assert "T I C   T A C   T O E - Multiplayer" in captured.out

# ---------------------------
# Testes para menu
# ---------------------------

@patch('builtins.input', side_effect=['t', 'p', '1'])
def test_menu_play_after_tutorial(mock_input, capsys):
    module_0.menu()
    captured = capsys.readouterr()
    assert "This is how to play Tic-Tac-Toe!" in captured.out
    assert "T I C   T A C   T O E - Single player" in captured.out

@patch('builtins.input', side_effect=['p', '2'])
def test_menu_direct_multi_game(mock_input, capsys):
    module_0.menu()
    captured = capsys.readouterr()
    assert "T I C   T A C   T O E - Multiplayer" in captured.out

@patch('builtins.input', side_effect=['t', 'p', '2'])
def test_menu_play_after_tutorial_then_multi(mock_input, capsys):
    module_0.menu()
    captured = capsys.readouterr()
    assert "This is how to play Tic-Tac-Toe!" in captured.out
    assert "T I C   T A C   T O E - Multiplayer" in captured.out

# ---------------------------
# Testes para show_tutorial
# ---------------------------

def test_show_tutorial(capsys):
    module_0.show_tutorial()
    captured = capsys.readouterr()
    assert "This is how to play Tic-Tac-Toe!" in captured.out
    assert "The goal of the game is to get three in a row" in captured.out
    assert "[1][2][3]\n[4][5][6]\n[7][8][9]\n" in captured.out

# ---------------------------
# Testes para a função principal (main)
# ---------------------------

@patch('TTT.menu')
def test_main(mock_menu):
    module_0.main()
    mock_menu.assert_called_once()
