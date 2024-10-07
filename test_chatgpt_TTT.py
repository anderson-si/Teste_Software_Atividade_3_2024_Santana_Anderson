# tests/test_TTT.py

import pytest
from unittest.mock import patch
from TTT import (
    place,
    keep_going,
    solo_show,
    player_turn,
    bot_turn2,
    horizontal_win,
    vertical_win,
    diagonal_win,
    horizontal_loss,
    vertical_loss,
    diagonal_loss,
    solo_tie,
    solo_game,
    multi_show,
    p1_turn,
    player2_turn,
    p1_hwin,
    p1_vwin,
    p1_dwin,
    p2_hwin,
    p2_vwin,
    p2_dwin,
    multi_tie,
    multi_game,
    show_tutorial,
    choose_game_mode,
    menu,
)

# Fixture para resetar o estado antes de cada teste
@pytest.fixture(autouse=True)
def reset_globals():
    global place, keep_going, s1, s2, m1, m2
    place[:] = ["-"] * 9
    keep_going = True
    s1 = "X"
    s2 = "O"
    m1 = "U"
    m2 = "N"


# Testes para player_turn
@patch('builtins.input', side_effect=['5'])
def test_player_turn_valid(mock_input, capsys):
    player_turn()
    assert place[4] == 'X'
    captured = capsys.readouterr()
    assert "[-][-][-]\n[-][X][-]\n[-][-][-]\n\n\n" in captured.out

@patch('builtins.input', side_effect=['10', '0', 'a', '3'])
def test_player_turn_invalid_then_valid(mock_input, capsys):
    player_turn()
    assert place[2] == 'X'
    captured = capsys.readouterr()
    assert "Please enter a valid number between 1 and 9 (inclusive):" in captured.out
    assert "[-][-][X]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out

@patch('builtins.input', side_effect=['1', '1', '2'])
def test_player_turn_spot_taken(mock_input, capsys):
    place[0] = 'X'
    player_turn()
    # The first input '1' is taken, it should prompt again for '2'
    assert place[1] == 'X'
    captured = capsys.readouterr()
    assert "Sorry, that spot is taken!" in captured.out
    assert "[X][X][-]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out

def test_bot_turn2_random(mock_randrange, capsys):
    # Sem oportunidades de ataque ou defesa, o bot escolhe aleatoriamente
    mock_randrange.return_value = 1  # Escolhe o segundo slot vazio (index 1)
    bot_turn2()
    assert place[1] == 'O'
    captured = capsys.readouterr()
    assert "[ -][O][-]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out or "[O][-][-]\n[-][-][-]\n[-][-][-]\n\n\n"

# Mock randrange para bot_turn2
@pytest.fixture
def mock_randrange(monkeypatch):
    return monkeypatch.setattr('TTT.randrange', lambda x: 0)

# Testes para funções de vitória
def test_horizontal_win_true():
    place[0] = place[1] = place[2] = 'X'
    assert horizontal_win() is True
    assert not keep_going

def test_horizontal_win_false():
    place[0] = place[1] = 'X'
    place[2] = 'O'
    assert horizontal_win() is False
    assert keep_going

def test_vertical_win_false():
    place[0] = place[3] = 'X'
    place[6] = 'O'
    assert vertical_win() is False
    assert keep_going

def test_diagonal_win_true():
    place[0] = place[4] = place[8] = 'X'
    assert diagonal_win() is True
    assert not keep_going

def test_diagonal_win_false():
    place[0] = place[4] = 'X'
    place[8] = 'O'
    assert diagonal_win() is False
    assert keep_going

def test_vertical_loss_true():
    place[0] = place[3] = place[6] = 'O'
    assert vertical_loss() is True
    assert not keep_going

def test_diagonal_loss_true():
    place[0] = place[4] = place[8] = 'O'
    assert diagonal_loss() is True
    assert not keep_going

def test_horizontal_loss_false():
    place[0] = place[1] = 'O'
    place[2] = 'X'
    assert horizontal_loss() is False
    assert keep_going

def test_solo_tie_false():
    place[0] = 'X'
    assert solo_tie() is False
    assert keep_going

def test_multi_tie_true(capsys):
    place[:] = ['U', 'N', 'U',
               'N', 'U', 'N',
               'N', 'U', 'N']
    assert multi_tie() is True
    assert not keep_going
    captured = capsys.readouterr()
    assert "It's a tie!" in captured.out

def test_multi_tie_false():
    place[0] = 'U'
    assert multi_tie() is False
    assert keep_going

# Testes para show_tutorial
def test_show_tutorial(capsys):
    show_tutorial()
    captured = capsys.readouterr()
    assert "This is how to play Tic-Tac-Toe!" in captured.out
    assert "The goal of the game is to get three in a row" in captured.out
    assert "[1][2][3]\n[4][5][6]\n[7][8][9]\n" in captured.out

# Testes para main (invoca menu)
@patch('TTT.menu')
def test_main(mock_menu):
    from TTT import main
    main()
    mock_menu.assert_called_once()
