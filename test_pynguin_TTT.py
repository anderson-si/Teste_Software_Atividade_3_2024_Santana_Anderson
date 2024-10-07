
import pytest
import TTT as module_0

@pytest.fixture(autouse=True)
def reset_globals():
    module_0.keep_going = True
    module_0.s1 = "X"
    module_0.s2 = "O"
    module_0.place = ["-"] * 9  
    yield
    module_0.keep_going = True
    module_0.place = ["-"] * 9

def test_case_0():
    module_0.player_turn = lambda: None  
    module_0.bot_turn2()  
    assert module_0.place.count("O") == 1  

def test_case_1():
    module_0.place = ["X", "X", "-", "-", "-", "-", "-", "-", "-"] 
    module_0.bot_turn2() 
    assert module_0.place[2] == "O" 

def test_case_2():
    module_0.place = ["X", "X", "X", "-", "-", "-", "-", "-", "-"] 
    assert module_0.horizontal_win() is True 

def test_case_3():
    module_0.place = ["X", "-", "-", "X", "-", "-", "X", "-", "-"] 
    assert module_0.vertical_win() is True 
    module_0.place = ["X", "-", "-", "-", "X", "-", "-", "-", "X"] 
    assert module_0.diagonal_win() is True 

def test_case_4():
    module_0.keep_going = True
    module_0.place = ["X", "O", "X", "-", "-", "-", "-", "-", "-"]
    def mock_bot_turn():
        module_0.place[0] = "O"
    module_0.bot_turn2 = mock_bot_turn
    module_0.bot_turn2()
    assert module_0.place[0] == "X" 
    captured = capsys.readouterr()
    assert "Invalid move" in captured.out 


def test_case_5():
    module_0.place = ["-", "-", "-", "X", "X", "X", "-", "-", "-"]
    assert module_0.horizontal_win() is True 
    module_0.place = ["-", "-", "-", "-", "-", "-", "X", "X", "X"]
    assert module_0.horizontal_win() is True