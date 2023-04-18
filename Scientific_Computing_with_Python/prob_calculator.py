import copy
import random

"""First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify 
the number of balls of each color that are in the hat.A hat will always be created with at least one ball. 
The arguments passed into the hat object upon creation should be converted to a contents instance variable. 
Contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a 
color name representing a single ball of that color. 
For example, if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].
"""
class Hat:
    def __init__(self, **kvargs):
        arguments = dict(kvargs)

        self.contents = []

        for key in arguments:
            color_counter = 0
            while color_counter < arguments[key]:
                self.contents.append(key)
                color_counter += 1


    """ The draw method accepts an argument indicating the number of balls to draw from the hat.  
    This method should remove balls at random from contents and return those balls as a list of strings. 
    The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. 
    If the number of balls to draw exceeds the available quantity, return all the balls.
    """

    def draw(self, number_to_draw):
        number_to_draw = number_to_draw
        available_quantity = len(self.contents)
        drawn_colors = []

        if number_to_draw >= available_quantity:
            drawn_colors = self.contents
            return drawn_colors
        else:
            draw_counter = 0
            while draw_counter < number_to_draw:
                random_draw = random.choice(self.contents)
                drawn_colors.append(random_draw)
                self.contents.remove(random_draw)
                draw_counter += 1

            return drawn_colors


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiment_counter = 0
    match_counter = 0

    while experiment_counter < num_experiments:
        hat_copy = copy.deepcopy(hat)
        drawn_color_list = hat_copy.draw(num_balls_drawn)

        drawn_color_dic = {}
        for color in drawn_color_list:
            if color in drawn_color_dic:
                drawn_color_dic[color] += 1
            else:
                drawn_color_dic[color] = 1

        drawn_color_compare = {}
        for x in drawn_color_dic:
            if x in expected_balls and drawn_color_dic[x] >= expected_balls[x]:
                drawn_color_compare[x] = expected_balls[x]

        if drawn_color_compare == expected_balls:
            match_counter += 1

        experiment_counter += 1

    return match_counter/experiment_counter
