"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS
        self.ball_radius = BALL_RADIUS
        self.brick_width = BRICK_WIDTH
        self.brick_height = BRICK_HEIGHT
        self.paddle_offset = PADDLE_OFFSET
        self.brick_offset = BRICK_OFFSET
        self.brick_spacing = BRICK_SPACING

        self.rows = self.brick_rows*self.brick_cols

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) -
                                                 brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-self.paddle.width)/2,
                        y=(self.window_height-self.paddle_offset-self.paddle.height))

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-self.ball.width)/2,
                        y=(self.window_height-self.ball.height)/2)

        # Draw bricks.
        self.draw_bricks()

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0



        # Initialize our mouse listeners.
        onmouseclicked(self.set_up_ball)
        onmousemoved(self.set_up_paddle)

        self.check_ball()

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self,new_dx):
        self.__dx = new_dx

    def set_dy(self,new_dy):
        self.__dy = new_dy




    def check_ball(self):
            self.moving_ball_1 = self.window.get_object_at(self.ball.x, self.ball.y)
            self.moving_ball_2 = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y)
            self.moving_ball_3 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2)
            self.moving_ball_4 = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2)
            if self.moving_ball_1 or self.moving_ball_2 or self.moving_ball_3 or self.moving_ball_4 is not None:
                self.check_bricks()
                self.check_paddle()

    def check_bricks(self):
        if self.ball.y <= self.brick_offset + self.brick_height * self.brick_rows + \
                self.brick_spacing * (self.brick_rows - 1):
            self.__dy = -self.__dy
            if self.moving_ball_1 is not None:
                self.window.remove(self.moving_ball_1)
                self.rows -= 1
            if self.moving_ball_2 is not None:
                self.window.remove(self.moving_ball_2)
                self.rows -= 1
            if self.moving_ball_3 is not None:
                self.window.remove(self.moving_ball_3)
                self.rows -= 1
            if self.moving_ball_4 is not None:
                self.window.remove(self.moving_ball_4)
                self.rows -= 1

    def check_paddle(self):
        if self.window_height - self.paddle_offset - self.paddle.height > self.ball.y > self.brick_offset + \
                self.brick_height * self.brick_rows + self.brick_spacing * (self.brick_rows - 1) - \
                self.ball_radius * 2:
            self.__dy = -self.__dy

    def set_up_ball(self, event):
        if self.ball.x == (self.window_width-self.ball.width)/2 and \
                self.ball.y == (self.window_height-self.ball.height)/2:
            self.set_ball_velocity()


    def draw_bricks(self):
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                self.window.add(self.brick, x=j*(self.brick_width+self.brick_spacing),
                                y=i*(self.brick_height+self.brick_spacing)+self.brick_offset)
                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'
                if i == 2 or i == 3:
                    self.brick.fill_color = 'orange'
                if i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'
                if i == 6 or i == 7:
                    self.brick.fill_color = 'green'
                if i == 8 or i == 9:
                    self.brick.fill_color = 'blue'

    def set_up_paddle(self, event):
        if event.x <= 0:
            self.paddle.x = 0
        elif event.x-self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x-self.paddle.width/2
        self.paddle.y = self.window.height-self.paddle_offset


    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx








