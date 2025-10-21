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

def test_04_game_width_should_be_square():
    snake_game = Game()
    assert(snake_game.width() == snake_game.height())

def test_05_game_width_should_be_positive():
    snake_game = Game()
    assert(snake_game.width() > 0)
    assert(snake_game.height() > 0)

def test_06_game_screen_dimensions_should_be_20x20_by_default():
    snake_game = Game()
    assert(snake_game.width() == 20)
    assert(snake_game.height() == 20)

def test_07_game_cells_dimensions_should_be_20x20_by_default():
    snake_game = Game()
    assert(snake_game.cell_size() == 20)

def test_08_game_screen_should_be_correct_based_on_cell_size_and_measures():
    snake_game = Game()
    width = snake_game.width()
    height = snake_game.height()
    cell_size = snake_game.cell_size()
    assert(snake_game.screen_width() == width * cell_size)
    assert(snake_game.screen_height() == height * cell_size)


def test_0_game_starts_with_snake_looking_to_right():
    snake_game = Game()
    assert(snake_game.snake_orientation() == (1, 0))

def test_0_game_starts_with_snake_at_middle_of_screen():
    snake_game = Game()
    width = snake_game.screen_width()
    height = snake_game.screen_height()
    screen_mid = width / height
    assert(snake_game.snake_position() == screen_mid)
