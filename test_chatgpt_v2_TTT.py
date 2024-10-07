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
    m1,
    m2,
    s1,
    s2,
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


# Testes para funções de exibição (solo_show e multi_show)
def test_solo_show(capsys):
    solo_show()
    captured = capsys.readouterr()
    expected_output = "\n\n\n\n\n\n\n[-][-][-]\n[-][-][-]\n[-][-][-]\n\n\n"
    assert captured.out == expected_output


def test_multi_show(capsys):
    multi_show()
    captured = capsys.readouterr()
    expected_output = "\n\n\n\n\n\n\n[-][-][-]\n[-][-][-]\n[-][-][-]\n\n\n"
    assert captured.out == expected_output


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


# Mock randrange para bot_turn2
@pytest.fixture
def mock_randrange(monkeypatch):
    return monkeypatch.setattr('TTT.randrange', lambda x: 0)


# Testes para bot_turn2
@patch('TTT.randrange', return_value=2)
def test_bot_turn2_offense(mock_randrange_func, capsys):
    # Bot pode ganhar preenchendo a terceira posição
    place[0] = 'O'
    place[1] = 'O'
    bot_turn2()
    assert place[2] == 'O'
    captured = capsys.readouterr()
    assert "[O][O][O]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out


@patch('TTT.randrange', return_value=2)
def test_bot_turn2_defense(mock_randrange_func, capsys):
    # Bot deve bloquear o jogador que está prestes a ganhar
    place[0] = 'X'
    place[1] = 'X'
    bot_turn2()
    assert place[2] == 'O'
    captured = capsys.readouterr()
    assert "[X][X][O]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out


@patch('TTT.randrange', return_value=1)
def test_bot_turn2_random(mock_randrange_func, capsys):
    # Sem oportunidades de ataque ou defesa, o bot escolhe aleatoriamente
    bot_turn2()
    assert place[1] == 'O'
    captured = capsys.readouterr()
    # Pode variar dependendo da escolha aleatória
    expected_outputs = [
        "[-][O][-]\n[-][-][-]\n[-][-][-]\n\n\n",
        "[O][-][-]\n[-][-][-]\n[-][-][-]\n\n\n",
        "[-][-][-]\n[O][-][-]\n[-][-][-]\n\n\n",
        "[-][-][-]\n[-][O][-]\n[-][-][-]\n\n\n",
        "[-][-][-]\n[-][-][-]\n[-][O][-]\n\n\n",
        "[-][-][-]\n[-][-][-]\n[-][-][O]\n\n\n",
    ]
    assert captured.out in expected_outputs


# Testes para funções de vitória
@pytest.mark.parametrize("positions, expected", [
    (['X', 'X', 'X', '-', '-', '-', '-', '-', '-'], True),
    (['X', 'X', 'O', '-', '-', '-', '-', '-', '-'], False),
    (['X', '-', '-', 'X', '-', '-', 'X', '-', '-'], True),
    (['X', '-', '-', 'X', '-', '-', 'O', '-', '-'], False),
    (['X', '-', '-', '-', 'X', '-', '-', '-', 'X'], True),
    (['X', '-', '-', '-', 'X', '-', '-', '-', 'O'], False),
])
def test_victory_conditions(positions, expected):
    for idx, val in enumerate(positions):
        place[idx] = val
    if 'X' in positions:
        result = (horizontal_win() or vertical_win() or diagonal_win())
        assert result == expected
        if expected:
            assert not keep_going
        else:
            assert keep_going


# Testes para funções de derrota
@pytest.mark.parametrize("positions, expected", [
    (['O', 'O', 'O', '-', '-', '-', '-', '-', '-'], True),
    (['O', 'O', 'X', '-', '-', '-', '-', '-', '-'], False),
    (['O', '-', '-', 'O', '-', '-', 'O', '-', '-'], True),
    (['O', '-', '-', 'O', '-', '-', 'X', '-', '-'], False),
    (['O', '-', '-', '-', 'O', '-', '-', '-', 'O'], True),
    (['O', '-', '-', '-', 'O', '-', '-', '-', 'X'], False),
])
def test_defeat_conditions(positions, expected):
    for idx, val in enumerate(positions):
        place[idx] = val
    if 'O' in positions:
        result = (horizontal_loss() or vertical_loss() or diagonal_loss())
        assert result == expected
        if expected:
            assert not keep_going
        else:
            assert keep_going


# Testes para empate (solo_tie e multi_tie)
@pytest.mark.parametrize("board, expected", [
    (['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X'], True),
    (['U', 'N', 'U', 'N', 'U', 'N', 'N', 'U', 'N'], True),
    (['X', 'O', 'X', 'X', 'O', '-', 'O', 'X', 'X'], False),
    (['U', 'N', 'U', 'N', 'U', '-', 'N', 'U', 'N'], False),
])
def test_tie_conditions(board, expected):
    for idx, val in enumerate(board):
        place[idx] = val
    if 'X' in board or 'U' in board:
        result = solo_tie() if 'X' in board else multi_tie()
        assert result == expected
        if expected:
            assert not keep_going
        else:
            assert keep_going


# Testes para as funções de empate
def test_solo_tie_true(capsys):
    place[:] = ['X', 'O', 'X',
               'X', 'O', 'O',
               'O', 'X', 'X']
    assert solo_tie() is True
    assert not keep_going
    captured = capsys.readouterr()
    assert "It's a tie!" in captured.out


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


# Testes para choose_game_mode
@patch('builtins.input', side_effect=['1'])
def test_choose_game_mode_solo(mock_input, capsys):
    choose_game_mode()
    captured = capsys.readouterr()
    assert "T I C   T A C   T O E - Single player" in captured.out


@patch('builtins.input', side_effect=['2'])
def test_choose_game_mode_multi(mock_input, capsys):
    choose_game_mode()
    captured = capsys.readouterr()
    assert "T I C   T A C   T O E - Multiplayer" in captured.out


@patch('builtins.input', side_effect=['3', '2'])
def test_choose_game_mode_invalid_then_multi(mock_input, capsys):
    choose_game_mode()
    captured = capsys.readouterr()
    assert "Invalid choice. Please enter '1' or '2'." in captured.out
    assert "T I C   T A C   T O E - Multiplayer" in captured.out


@patch('builtins.input', side_effect=['4', '1'])
def test_choose_game_mode_invalid_then_solo(mock_input, capsys):
    choose_game_mode()
    captured = capsys.readouterr()
    assert "Invalid choice. Please enter '1' or '2'." in captured.out
    assert "T I C   T A C   T O E - Single player" in captured.out


# Testes para menu
@patch('builtins.input', side_effect=['t', 'p', '1'])
def test_menu_play_after_tutorial(mock_input, capsys):
    menu()
    captured = capsys.readouterr()
    assert "This is how to play Tic-Tac-Toe!" in captured.out
    assert "T I C   T A C   T O E - Single player" in captured.out


@patch('builtins.input', side_effect=['p', '2'])
def test_menu_direct_multi_game(mock_input, capsys):
    menu()
    captured = capsys.readouterr()
    assert "T I C   T A C   T O E - Multiplayer" in captured.out


@patch('builtins.input', side_effect=['x', 't', 'p', '1'])
def test_menu_invalid_then_tutorial_then_play(mock_input, capsys):
    menu()
    captured = capsys.readouterr()
    assert "Input [P] to play, or [T] for the tutorial:" in captured.out
    assert "Invalid choice. Please enter '1' or '2'." not in captured.out  # Since menu handles 't' and 'p'
    assert "This is how to play Tic-Tac-Toe!" in captured.out
    assert "T I C   T A C   T O E - Single player" in captured.out


# Testes para multi_game
@patch('builtins.input', side_effect=[
    '1',  # Player 1 chooses to play against bot
    '1',  # Player 1 places at position 1
    '2',  # Bot places at position 2
    '3',  # Player 1 places at position 3 -> Player 1 wins horizontally
])
def test_multi_game_player1_wins(mock_input, capsys):
    multi_game()
    captured = capsys.readouterr()
    assert "You win!" in captured.out


@patch('builtins.input', side_effect=[
    '2',  # Player 1 chooses to play multiplayer
    'O',  # Player 1 selects 'O'
    '1',  # Player 1 places at position 1
    '2',  # Player 2 places at position 2
    '3',  # Player 1 places at position 3 -> Player 1 wins horizontally
])
def test_multi_game_player1_wins_multiplayer(mock_input, capsys):
    multi_game()
    captured = capsys.readouterr()
    assert "Player 1 wins!" in captured.out


@patch('builtins.input', side_effect=[
    '2',  # Player 1 chooses to play multiplayer
    'X',  # Player 1 selects 'X'
    '1',  # Player 1 places at position 1
    '1',  # Player 2 tries to place at position 1 (taken)
    '2',  # Player 2 places at position 2
    '3',  # Player 1 places at position 3 -> Player 1 wins horizontally
])
def test_multi_game_player2_invalid_move_then_valid(mock_input, capsys):
    multi_game()
    captured = capsys.readouterr()
    assert "Sorry, that spot is taken!" in captured.out
    assert "Player 1 wins!" in captured.out


@patch('builtins.input', side_effect=[
    '1',  # Solo game
    '1',  # Player places at 1
    '2',  # Bot places at 2
    '3',  # Player places at 3 -> Player wins
])
def test_solo_game_player_wins(mock_input, capsys):
    solo_game()
    captured = capsys.readouterr()
    assert "You win!" in captured.out


@patch('builtins.input', side_effect=[
    '1',  # Solo game
    '1',  # Player places at 1
    '3',  # Bot places at 3
    '2',  # Player places at 2
    '5',  # Bot places at 5
    '4',  # Player places at 4
    '7',  # Bot places at 7
    '6',  # Player places at 6
    '8',  # Bot places at 8
    '9',  # Player places at 9 -> Tie
])
def test_solo_game_tie(mock_input, capsys):
    solo_game()
    captured = capsys.readouterr()
    assert "It's a tie!" in captured.out


@patch('builtins.input', side_effect=[
    '2',  # Multiplayer
    'X',  # Player 1 selects 'X'
    '1',  # Player 1 places at 1
    '2',  # Player 2 places at 2
    '3',  # Player 1 places at 3 -> Player 1 wins
])
def test_multi_game_player1_wins_x_symbol(mock_input, capsys):
    multi_game()
    captured = capsys.readouterr()
    assert "Player 1 wins!" in captured.out


@patch('builtins.input', side_effect=[
    '2',  # Multiplayer
    'O',  # Player 1 selects 'O'
    '1',  # Player 1 places at 1
    '2',  # Player 2 places at 2
    '3',  # Player 1 places at 3 -> Player 1 wins
])
def test_multi_game_player1_wins_o_symbol(mock_input, capsys):
    multi_game()
    captured = capsys.readouterr()
    assert "Player 1 wins!" in captured.out


# Testes para a função main
@patch('TTT.menu')
def test_main(mock_menu):
    from TTT import main
    main()
    mock_menu.assert_called_once()


# Testes para funções auxiliares de vitória e derrota
def test_p1_hwin():
    place[0] = place[1] = place[2] = m1
    assert p1_hwin() is True
    assert not keep_going


def test_p1_vwin():
    place[0] = place[3] = place[6] = m1
    assert p1_vwin() is True
    assert not keep_going


def test_p1_dwin():
    place[0] = place[4] = place[8] = m1
    assert p1_dwin() is True
    assert not keep_going


def test_p2_hwin():
    place[0] = place[1] = place[2] = m2
    assert p2_hwin() is True
    assert not keep_going


def test_p2_vwin():
    place[0] = place[3] = place[6] = m2
    assert p2_vwin() is True
    assert not keep_going


def test_p2_dwin():
    place[0] = place[4] = place[8] = m2
    assert p2_dwin() is True
    assert not keep_going


# Testes para p1_turn e player2_turn
@patch('builtins.input', side_effect=['1'])
def test_p1_turn_valid(mock_input, capsys):
    p1_turn()
    assert place[0] == m1
    captured = capsys.readouterr()
    assert "[U][-][-]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out


@patch('builtins.input', side_effect=['1', '2'])
def test_player2_turn_valid(mock_input, capsys):
    p1_turn()  # Player 1 takes position 1
    player2_turn()
    assert place[1] == m2
    captured = capsys.readouterr()
    assert "[U][N][-]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out


@patch('builtins.input', side_effect=['1', '1', '2'])
def test_p1_turn_spot_taken(mock_input, capsys):
    place[0] = m1
    p1_turn()
    assert place[1] == m1
    captured = capsys.readouterr()
    assert "Sorry, that spot is taken!" in captured.out
    assert "[U][U][-]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out


@patch('builtins.input', side_effect=['2', '2'])
def test_player2_turn_spot_taken(mock_input, capsys):
    place[1] = m2
    p1_turn()  # Player 1 places at position 2
    player2_turn()
    assert place[1] == m2  # Should prompt again and place at position 2
    captured = capsys.readouterr()
    assert "Sorry, that spot is taken!" in captured.out
    assert "[ -][N][-]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out


# Adicionando testes para ensure all branches são cobertas

# Teste quando o bot não pode atacar ou defender e escolhe a última posição
@patch('TTT.randrange', return_value=8)
def test_bot_turn2_last_position(mock_randrange_func, capsys):
    # Fill all positions except the last one
    place[:8] = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    bot_turn2()
    assert place[8] == 'O'
    captured = capsys.readouterr()
    assert "[-][-][-]\n[-][-][-]\n[-][-][O]\n\n\n" in captured.out


# Teste para bot_turn2 quando não há posições vazias
@patch('TTT.randrange', return_value=0)
def test_bot_turn2_no_empty_positions(mock_randrange_func, capsys):
    place[:] = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    bot_turn2()
    # Nenhuma mudança deve ocorrer
    assert place == ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    captured = capsys.readouterr()
    # Nenhum novo print deve ocorrer, pois não há posições vazias
    assert captured.out == ""


# Teste para menu com várias iterações
@patch('builtins.input', side_effect=['t', 't', 'p', '1'])
def test_menu_multiple_tutorials_then_play(mock_input, capsys):
    menu()
    captured = capsys.readouterr()
    assert "This is how to play Tic-Tac-Toe!" in captured.out
    assert "T I C   T A C   T O E - Single player" in captured.out


# Teste para choose_game_mode com múltiplas entradas inválidas
@patch('builtins.input', side_effect=['a', 'b', '1'])
def test_choose_game_mode_multiple_invalid_then_solo(mock_input, capsys):
    choose_game_mode()
    captured = capsys.readouterr()
    assert "Invalid choice. Please enter '1' or '2'." in captured.out
    assert "T I C   T A C   T O E - Single player" in captured.out


# Teste para p1_turn com entradas inválidas
@patch('builtins.input', side_effect=['a', '10', '3'])
def test_p1_turn_invalid_then_valid(mock_input, capsys):
    p1_turn()
    assert place[2] == m1
    captured = capsys.readouterr()
    assert "Please enter a valid number between 1 and 9 (inclusive):" in captured.out
    assert "[ -][-][U]\n[-][-][-]\n[-][-][-]\n\n\n" in captured.out


# Teste para player2_turn com entradas inválidas
@patch('builtins.input', side_effect=['a', '10', '5'])
def test_player2_turn_invalid_then_valid(mock_input, capsys):
    player2_turn()
    assert place[4] == m2
    captured = capsys.readouterr()
    assert "Please enter a valid number between 1 and 9 (inclusive):" in captured.out
    assert "[ -][-][-]\n[-][N][-]\n[-][-][-]\n\n\n" in captured.out

