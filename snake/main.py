import random
class Game:
    
    def __init__(self):
        self._score_points = 0
        self._current_state = "running"
        self._game_over = False
        self._cell_size = 20
        self._width = 20
        self._height = 20
        self._snake_orientation = (1, 0)
        self._snake_position = (10, 10)
        self._screen_width = 400
        self._screen_height = 400
        self._food_position = self.spawn_food() 

    def score_points(self):
        return 0

    def current_state(self):
        return self._current_state

    def game_over(self):
        return self._game_over

    def width(self):
        return self._width

    def height(self):
        return self._height

    def screen_width(self):
        return self._width * self._cell_size
    
    def screen_height(self):
        return self._height * self._cell_size

    def snake_orientation(self):
        return self._snake_orientation
    
    def snake_position(self):
        return self._snake_position

    def cell_size(self):
        return self._cell_size

    def food_position(self):
        return self._food_position

    def spawn_food(self):
        food_x = random.randint(0, self._width - 1)
        food_y = random.randint(0, self._height - 1)
        while True:
            if (food_x, food_y) != self._snake_position:
                return (food_x, food_y)
                
        
