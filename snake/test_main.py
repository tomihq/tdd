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

def test_09_game_starts_with_snake_looking_to_right():
    snake_game = Game()
    assert(snake_game.snake_orientation() == (1, 0))

def test_10_game_starts_with_snake_at_middle_of_screen():
    snake_game = Game()
    width = snake_game.width() // 2
    height = snake_game.height() // 2
    assert(snake_game.snake_position() == (width, height))

def test_11_food_should_be_in_a_valid_cell():
    snake_game = Game()
    food_x, food_y = snake_game.food_position()
    snake_position_x, snake_position_y = snake_game.snake_position()
    assert 0 <= food_x < snake_game.width()
    assert 0 <= food_y < snake_game.height()
    assert (food_x, food_y) != snake_game.snake_position()


#0 to 11 are initialization tests.

#snake size = score + 1
def test_12_snake_will_do_nothing_if_want_to_eat_being_in_other_position():
    snake_game = Game()
    snake_game.eat((10, 11), (12,13))
    assert(snake_game.score_points()+1 == 1)

def test_13_snake_size_will_grow_if_eats_food():
    snake_game = Game()
    snake_game.eat((11, 11), (11, 11))
    assert(snake_game.score_points()+1 == 2)

# movement
def test_14_snake_moves_right_one_cell():
    snake_game = Game()
    head_x, head_y = snake_game.snake_position()
    snake_game.move_snake()
    new_x, new_y = snake_game.snake_position()
    assert(new_x == head_x + 1)
    assert(new_y == head_y)

def test_15_snakes_moves_around_right_edge():
    snake_game = Game()
    snake_game._snake_position = (19, 10)
    snake_game.move_snake()
    new_x, new_y = snake_game._snake_position
    assert new_x == 0
    assert new_y == 10 
