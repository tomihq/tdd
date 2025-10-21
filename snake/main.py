class Game:
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
    
    def cell_size(self):
        return 20
