"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    for i in range(NUM_LIVES):
        while True:
            if graphics.rows == 0:
                break
            pause(FRAME_RATE)
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.check_ball()
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width:
                current_dx = graphics.get_dx()
                graphics.set_dx(-current_dx)
            if graphics.ball.y > graphics.window.height-graphics.brick_spacing-graphics.paddle.height:
                break
        graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
        graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2
        graphics.set_dy(0)
        graphics.set_dx(0)







    # Add animation loop here!


if __name__ == '__main__':
    main()
