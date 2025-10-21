from snake.main import Game

def test_01_initialize_new_game_with_score_0():
    snake_game = Snake()
    assert(snake_game.current_score == 0)


