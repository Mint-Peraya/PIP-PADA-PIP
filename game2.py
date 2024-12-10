import random
import time
import turtle


class FastOrNot:
    def __init__(self):
        self.sr = turtle.Screen()
        self.sr.bgcolor('black')
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.sr.tracer(0)

        self.player = turtle.Turtle()
        self.score = 0
        self.start_time = time.time()
        self.target = None
        self.obstacles = []

        self.init_player()
        self.border()
        self.create_target()
        self.create_obstacles(15)

    def border(self):
        border_turtle = turtle.Turtle()
        border_turtle.hideturtle()
        border_turtle.speed(0)
        border_turtle.penup()
        border_turtle.goto(-self.canvas_width, -self.canvas_height)
        border_turtle.pendown()
        border_turtle.color("light yellow")
        border_turtle.pensize(3)

        for _ in range(2):
            border_turtle.forward(self.canvas_width * 2)
            border_turtle.left(90)
            border_turtle.forward(self.canvas_height * 2)
            border_turtle.left(90)

    def init_player(self):
        self.player.penup()
        self.player.shape('turtle')
        self.player.color("white")

        self.sr.listen()
        self.sr.onkeypress(self.go, "space")
        self.sr.onkeypress(self.up, "Up")
        self.sr.onkeypress(self.down, "Down")
        self.sr.onkeypress(self.left, "Left")
        self.sr.onkeypress(self.right, "Right")

    def create_target(self):
        if self.target:
            self.target.hideturtle()

        self.target = turtle.Turtle()
        self.target.penup()
        self.target.color("light green")
        self.target.shape("square")
        self.target.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.target.goto(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                         random.randint(-self.canvas_height + 20, self.canvas_height - 20))

    def create_obstacles(self, count):
        for obstacle in self.obstacles:
            obstacle.hideturtle()
        self.obstacles.clear()

        for _ in range(count):
            obstacle = turtle.Turtle()
            obstacle.penup()
            obstacle.color("red")
            obstacle.shape("circle")
            obstacle.shapesize(stretch_wid=1.5, stretch_len=1.5)
            obstacle.goto(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                          random.randint(-self.canvas_height + 20, self.canvas_height - 20))
            self.obstacles.append(obstacle)

    def check_collisions(self):
        # Check collision with the target
        if self.target.distance(self.player) < 20:
            self.score += 1
            self.create_target()
            self.create_obstacles(int(15 + self.score))  # Increase obstacles as score increases

        # Check collision with obstacles
        for obstacle in self.obstacles:
            if obstacle.distance(self.player) < 5:
                self.score -= 0.5

    def display_score(self):
        print(f"Score: {self.score}")

    def game_over(self):
        self.sr.clear()
        self.sr.bgcolor("black")
        end_message = turtle.Turtle()
        end_message.hideturtle()
        end_message.penup()
        end_message.color("dark red")
        end_message.goto(0, 50)
        end_message.write("GAME END", align="center", font=("Courier", 36, "bold"))

        end_message.goto(0, -50)
        end_message.color("pink")
        end_message.write(f"Level Pass: {self.score}",
                          align="center", font=("Courier", 24, "normal"))

        self.sr.listen()
        self.sr.exitonclick()

    def run(self):
        self.create_obstacles(int(5 + self.score))
        while self.score < 10:
            self.sr.update()
            self.check_collisions()

            elapsed_time = time.time() - self.start_time
            if elapsed_time > 60:  # End game after 60 seconds
                break

        self.game_over()

    def go(self):
        self.player.forward(10)

    def up(self):
        self.player.setheading(90)

    def down(self):
        self.player.setheading(270)

    def right(self):
        self.player.setheading(0)

    def left(self):
        self.player.setheading(180)

# game = FastOrNot()
# game.run()
# turtle.done()
