import copy
from User_system import Account
import csv
import turtle
import random
import game1
import game2


# To add other person manually
# name = Account(username,email,password)
# User_data.append(name.all_information())


s = turtle.Screen()
s.title('PIP PADA PIP')


class Start:
    def __init__(self):
        turtle.tracer(0)
        turtle.speed(0)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        turtle.bgcolor('black')
        turtle.colormode(255)
        print(self.canvas_width, self.canvas_height)
        turtle.penup()

    def run(self):
        self.star()
        self.button()
        turtle.listen()
        turtle.onscreenclick(self.signup_in, 1)

    def signup_in(self, x, y):
        if -75 < x < 75 and 30 < y < 80:
            print('start')
            name = turtle.textinput("Sign Up", "Input username")
            email = turtle.textinput("Sign Up", "Input email")
            password = turtle.textinput("Sign Up", "Input password")
            watashino = Account(name, email, password)
            User_data.append(watashino.all_information())
            dee = copy.deepcopy(User_data)
            print(User_data)
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(dee)

        if -75 < x < 75 and -30 < y < 20:
            name_or_mail = turtle.textinput("Sign In", "Input username or email")
            password = turtle.textinput("Sign In", "Input password")
            print(name_or_mail, password)
            for i in range(len(User_data)):
                if (User_data[i][1] == name_or_mail or User_data[i][2] == name_or_mail) and User_data[i][3] == password:
                    turtle.clear()
                    select = Mainchoose(i)
                    select.choosepage()
                elif i == len(User_data):
                    print("Incorrect username or password")

    def star(self):
        for i in range(random.randint(100, 250)):
            x = random.randint(-500, 500)
            y = random.randint(-400, 300)
            turtle.color((random.randint(100, 255), random.randint(0, 100), random.randint(0, 225)))
            turtle.penup()
            turtle.goto(x, y)
            turtle.dot(random.randint(1, 10))

    def button(self):
        # Project Name
        turtle.goto(0, 300)
        turtle.color("pink")
        turtle.write("Pip pada Pip", move=True, align="center", font=('Courier', 30, 'normal'))
        turtle.color("deep pink")
        # Sign Up
        turtle.goto(-75, 30)
        self.drawsquare(150, 50)
        turtle.goto(0, 45)
        turtle.write('Sign Up', move=True, align="center", font=('Courier', 20, 'normal'))
        # Sign In
        turtle.goto(-75, -30)
        self.drawsquare(150, 50)
        print(turtle.position())
        turtle.goto(0, -15)
        turtle.write('Sign In', move=True, align="center", font=('Courier', 20, 'normal'))

    def drawsquare(self, width, height):
        turtle.pendown()
        for i in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.left(90)
        turtle.penup()


class Mainchoose:
    def __init__(self, i):
        self.index = i
        turtle.tracer(0)
        turtle.speed(0)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        turtle.bgcolor('black')
        turtle.colormode(255)
        print(self.canvas_width, self.canvas_height)
        turtle.penup()

    def choosepage(self):
        # heading
        turtle.goto(0, 300)
        turtle.color("deep pink")
        turtle.write(f"Welcome {User_data[self.index][1]}", move=True, align="center", font=('Courier', 22, 'normal'))
        turtle.goto(450, 300)
        turtle.write(f"Score:{User_data[self.index][4]}", move=True, align="center", font=('Courier', 20, 'normal'))

        omg = Start()
        omg.star()
        turtle.color("light blue")
        # left
        turtle.goto(-300, 200)
        omg.drawsquare(200, 50)
        turtle.goto(-200, 215)
        turtle.write("Flappy Turtle", move=True, align="center", font=('Courier', 20, 'normal'))
        # right
        turtle.goto(100, 200)
        omg.drawsquare(200, 50)
        turtle.goto(200, 215)
        turtle.write("Turtle to go", move=True, align="center", font=('Courier', 20, 'normal'))
        # select
        s = turtle.Screen()
        s.onscreenclick(self.selectgame)

    def selectgame(self, x, y):
        if -300 < x < -100 and 200 < y < 250:
            turtle.clearscreen()
            d = game1.FlappyTurtle()
            d.run()
            sc = d.player.score
            User_data[self.index][4] += sc
            dee = copy.deepcopy(User_data)
            print(User_data)
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(dee)
        elif 150 < x < 300 and 200 < y < 250:
            turtle.clearscreen()
            d = game2.FastOrNot()
            d.run()
            sc = d.score
            dee = copy.deepcopy(User_data)
            print(User_data)
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(dee)



user1 = Account("Alice", "alice@gmail.com", "Madonna", score=1001)
user2 = Account("Bob", "bobby999@gmail.com", "MoreandMoreMoney", score=999)
user3 = Account("Handsome", "pomlorsudkrub@hotmail.com", "Maimeekraideetaopom", score=1111)

User_data = [['account number', 'username', 'email', 'password', "score"]]
csv_file_path = 'user.csv'
User_data.append(user1.all_information())
User_data.append(user2.all_information())
User_data.append(user3.all_information())

ww = Start()
ww.run()
turtle.done()
