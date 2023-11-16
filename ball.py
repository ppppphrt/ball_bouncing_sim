import turtle
import random


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        self.xpos = random.randint(ball_radius, canvas_width - ball_radius)
        self.ypos = random.randint(ball_radius, canvas_height - ball_radius)
        self.vx = random.randint(1, 0.01 * canvas_width)
        self.vy = random.randint(1, 0.01 * canvas_height)
        self.radius = ball_radius
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move_circle(self, canvas_width, canvas_height):
        # update the x, y coordinates of the ball with velocity
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (canvas_width - self.radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (canvas_height - self.radius):
            self.vy = -self.vy