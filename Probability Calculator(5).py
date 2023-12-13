import copy
import random
#These modules will be used for creating copies of objects and generating random numbers, respectively
class Hat: #collection of colored balls
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball] * count)
    #list of string that represent the ball in the hat
    def draw(self, num_balls):
        balls_to_draw = min(num_balls, len(self.contents))
        drawn_balls = random.sample(self.contents, balls_to_draw)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls
#draw method use random sample, so it selects randomly and removes a specified number of ball from the hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1

        success = True
        for ball, count in expected_balls.items():
            if drawn_balls_dict.get(ball, 0) < count:
                success = False
                break

        if success:
            num_successful_experiments += 1

    return num_successful_experiments / num_experiments
#experiment function calculate the probability of drawing a specific group of balls from the hat
#it calculates it by diving the number of successfull experiments by the total number of experiments
#Example
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat, expected_balls={"red": 1, "green": 2}, num_balls_drawn=4, num_experiments=1000)
print(probability)
