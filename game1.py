import turtle
import time
import random
 

class FlappyTurtle:
    def __init__(self):
        self.sr = turtle.Screen()
        self.sr.tracer(0)
        self.sr.bgcolor('light blue')
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.sr.setup(width=self.canvas_width * 2, height=self.canvas_height * 2)

        self.player = turtle.Turtle()
        self.bb = turtle.Turtle()

        self.gravity = -0.2
        self.is_game_over = False
        self.pen = turtle.Turtle()
        self.pen.hideturtle()

    def run(self):
        # self.border()
        self.setup_player()
        self.setup_bubble()

        # Create pipes
        self.block_manager = Block(num_pipes=3)  # Adjust number of pipe pairs here
        self.block_manager.setup()

        self.sr.listen()
        self.sr.onkeypress(self.flappy_jump, "space")

        self.player.score = 0
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(0, self.canvas_height - 40)
        self.pen.write(f"Score: {self.player.score}", align="center", font=('Courier', 20, 'normal'))

        while not self.is_game_over:
            self.update_player()
            self.update_bubble()
            self.block_manager.update_blocks()
            self.check_collisions()

            self.sr.update()
            time.sleep(0.02)

        self.end_game()

    def setup_player(self):
        self.player.speed(0)
        self.player.penup()
        self.player.color("dark green")
        self.player.shape("turtle")
        self.player.goto(-self.canvas_width / 2, 0)
        self.player.dy = 0

    def update_player(self):
        self.player.dy += self.gravity
        y = self.player.ycor() + self.player.dy

        # Prevent player from going out of bounds
        if y <= -self.canvas_height:
            y = -self.canvas_height
            self.is_game_over = True
        elif y >= self.canvas_height:
            y = self.canvas_height
            self.is_game_over = True

        self.player.sety(y)

    def flappy_jump(self):
        self.player.dy = 5

    def setup_bubble(self):
        self.bb.penup()
        self.bb.speed(0)
        self.bb.color("dark blue")
        self.bb.shape("circle")
        self.reset_bubble()

    def update_bubble(self):
        speed = random.randint(7, 15)
        x = self.bb.xcor() - speed
        self.bb.setx(x)

        if x < -self.canvas_width:
            self.reset_bubble()

    def reset_bubble(self):
        self.bb.goto(self.canvas_width, random.randint(-self.canvas_height, self.canvas_height))

    def check_collisions(self):
        # Check collision with pipes
        for upper, lower in self.block_manager.pipes:
            if self.is_collision(self.player, upper) or self.is_collision(self.player, lower):
                self.is_game_over = True

        # Check collision with bubble
        if self.is_collision(self.player, self.bb):
            self.player.score += 3  # Bonus points for hitting the bubble
            self.pen.clear()
            self.pen.write(f"Score: {self.player.score}",
                           align="center", font=('Courier', 20, 'normal'))
            self.reset_bubble()

        # Check if player passes a pipe
        for upper, lower in self.block_manager.pipes:
            if upper.xcor() + 30 < self.player.xcor() - 10 and upper.value == 1:
                self.player.score += 1
                upper.value = 0  # Prevent double scoring
                self.pen.clear()
                self.pen.write(f"Score: {self.player.score}",
                               align="center", font=('Courier', 20, 'normal'))

    @staticmethod
    def is_collision(t1, t2):
        # Get bounds considering shapesize
        t1_width = 10 * t1.shapesize()[1]
        t1_height = 10 * t1.shapesize()[0]
        t2_width = 10 * t2.shapesize()[1]
        t2_height = 10 * t2.shapesize()[0]

        return (
                    abs(t1.xcor() - t2.xcor()) < (t1_width + t2_width) / 2 and
                    abs(t1.ycor() - t2.ycor()) < (t1_height + t2_height) / 2
            )

    def end_game(self):
        self.sr.clearscreen()
        self.sr.bgcolor("black")
        end_pen = turtle.Turtle()
        end_pen.hideturtle()
        end_pen.penup()
        end_pen.color("white")
        end_pen.write("GAME OVER", align="center", font=('Courier', 36, 'normal'))
        end_pen.goto(0, -40)
        end_pen.write(f"Score: {self.player.score}", align="center", font=('Courier', 24, 'normal'))

        self.sr.listen()
        self.sr.exitonclick()


class Block:
    def __init__(self, num_pipes=3):
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.num_pipes = num_pipes
        self.pipes = []

    def setup(self):
        spacing = self.canvas_width * 2 // self.num_pipes

        for i in range(self.num_pipes):
            upper = turtle.Turtle()
            lower = turtle.Turtle()

            for pipe in [upper, lower]:
                pipe.penup()
                pipe.speed(0)
                pipe.shape("square")
                pipe.color("light yellow")
                pipe.shapesize(stretch_wid=10, stretch_len=3)
                pipe.dx = -4
                pipe.value = 1

            x_position = self.canvas_width + i * spacing
            upper.goto(x_position, random.randint(50, self.canvas_height))
            lower.goto(x_position, upper.ycor() - 200)

            self.pipes.append((upper, lower))

    def update_blocks(self):
        for upper, lower in self.pipes:
            for pipe in [upper, lower]:
                x = pipe.xcor() + pipe.dx
                pipe.setx(x)

                if x < -self.canvas_width:
                    new_x = self.canvas_width + random.randint(0, 200)
                    pipe.setx(new_x)
                    pipe.value = 1


# game = FlappyTurtle()
# game.run()
# turtle.done()
