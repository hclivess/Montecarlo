import cairo
from random import randrange
import math

pi = math.pi


class Rectangle:
    def __init__(self):
        self.x_start = 700
        self.x_end = 250
        self.y_start = 700
        self.y_end = 250

    def paint_rectangle(self, ctx):
        ctx.rectangle(self.x_start, self.y_start, self.x_end, self.y_end)
        ctx.set_source_rgb(0.8, 0.8, 1)
        ctx.set_line_width(5)
        ctx.stroke()

    def is_in_rectangle(self, point):
        """determines whether random number is within range of the rectangle"""
        try:
            assert point.x > self.x_start
            assert point.y > self.y_start

            assert point.x < self.x_start + self.x_end
            assert point.y < self.y_start + self.y_end
            return True
        except:
            return False


class Circle:
    def __init__(self):
        self.radius = 250
        self.offset_x = 275
        self.offset_y = 275

    def is_in_circle(self, point):
        """if (x-center_x)**2 + (y-center_y)**2 <= radius**2"""
        if (point.x - self.offset_x) ** 2 + (
            point.y - self.offset_y
        ) ** 2 <= self.radius**2:
            return True
        else:
            return False

    def paint_circle(self, ctx):
        ctx.arc(self.offset_x, self.offset_y, self.radius, 0, 2 * math.pi)

        ctx.set_source_rgb(1, 0, 0)
        ctx.set_line_width(5)
        ctx.stroke()

        ctx.fill()


def random_location_y(plane):
    y = randrange(plane.y_start, plane.y_end)
    return y


def random_location_x(plane):
    x = randrange(plane.x_start, plane.x_end)

    return x


class Ball:
    def __init__(self):
        self.x = None
        self.y = None
        self.is_in_circle = False
        self.is_in_rectangle = False

    def spill(self, plane):
        self.x = random_location_x(plane)
        self.y = random_location_y(plane)

    def paint_ball(self, ctx):
        ctx.set_source_rgb(1, 1, 0)
        ctx.move_to(self.x, self.y)
        ctx.arc(self.x, self.y, 4, 0, 2 * math.pi)
        ctx.fill()


class Balls:
    def __init__(self, count, plane):
        self.ball_count = count
        self.all_balls = []

    def gather_balls(self):
        for b in range(self.ball_count):
            ball = Ball()
            ball.spill(plane)
            self.all_balls.append(ball)


class Plane:
    def __init__(self):
        self.x_start = 0
        self.x_end = 1000
        self.y_start = 0
        self.y_end = 1000


class Counter:
    def __init__(self):
        self.in_rectangle = 0
        self.in_circle = 0
        self.in_plane = 0

    def get_ratio(self):
        return self.in_circle / self.in_rectangle


if __name__ == "__main__":
    plane = Plane()
    rectangle = Rectangle()
    circle = Circle()
    counter = Counter()

    balls = Balls(plane=plane, count=50)
    balls.gather_balls()

    for ball in balls.all_balls:
        if circle.is_in_circle(ball):
            ball.is_in_circle = True
        if rectangle.is_in_rectangle(ball):
            ball.is_in_rectangle = True

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, plane.x_end, plane.y_end)
    ctx = cairo.Context(surface)

    rectangle.paint_rectangle(ctx)
    circle.paint_circle(ctx)
    for ball in balls.all_balls:
        ball.paint_ball(ctx)

    for ball in balls.all_balls:
        if ball.is_in_rectangle:
            counter.in_rectangle += 1
        elif ball.is_in_circle:
            counter.in_circle += 1
        else:
            counter.in_plane += 1

    print(f"In plane: {counter.in_plane}")
    print(f"In circle: {counter.in_circle}")
    print(f"In rectangle: {counter.in_rectangle}")
    print(f"Ratio: {counter.get_ratio()}")

    surface.write_to_png("montecarlo.png")
