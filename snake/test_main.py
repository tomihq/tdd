from snake.main import Game

def test_01_initialize_new_game_with_score_0():
    snake_game = Game()
    assert(snake_game.score_points() == 0)

def test_02_state_on_new_game_initialization_is_set_to_running():
    snake_game = Game()
    assert(snake_game.current_state() == "running")

def test_03_game_over_flag_on_initialization_is_set_to_false():
    snake_game = Game()
    assert(snake_game.game_over() == False)
