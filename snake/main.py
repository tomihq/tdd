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
        self._food_position = self.spawn_food() 

    def score_points(self):
        return 0

    def current_state(self):
        return "running"

    def game_over(self):
        return False

    def width(self):
        return 20

    def height(self):
        return 20

    def screen_width(self):
        return 400
    
    def screen_height(self):
        return 400

    def snake_orientation(self):
        return (1, 0)
    
    def snake_position(self):
        return (10, 10)

    def cell_size(self):
        return 20

    def food_position(self):
        return self._food_position

    def spawn_food(self):
        food_x = random.randint(0, self._width - 1)
        food_y = random.randint(0, self._height - 1)
        while True:
            if (food_x, food_y) != self._snake_position:
                return (food_x, food_y)
                
        
