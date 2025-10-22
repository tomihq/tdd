import random
class Game:

    def __init__(self):
        self.food_position = self.spawn_food() 

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
        return food_position

    def spawn_food(self):
        food_x = random.randint(0, self.width - 1)
        food_y = random.randint(0, self.height - 1)
        
