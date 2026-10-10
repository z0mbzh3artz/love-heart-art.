import turtle
import math
import random

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor(”#090914”)
screen.title(“I Love You ❤️”)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

messages = [
“I love you”, “Te amo”, “Je t’aime”, “Ich liebe dich”,
“Ti amo”, “愛してる”, “사랑해”, “Я тебя люблю”,
“Eu te amo”, “我爱你”, “أحبك”, “मैं तुमसे प्यार करता हूँ”,
“Ik hou van jou”, “Kocham cię”, “Seni seviyorum”,
“Σ’ αγαπώ”, “Mahal kita”, “ฉันรักคุณ”, “Nakupenda”,
“Aishiteru”
]

screen.tracer(0)

for i in range(220):
t = i * 0.17
x = 16 * math.sin(t)**3
y = (13 * math.cos(t) - 5 * math.cos(2t)
- 2 * math.cos(3t) - math.cos(4*t))

pen.goto(x * 15, y * 15)
pen.color(random.choice([
    "#ff4fa3", "#ff78c8", "#ffb6e6",
    "#ffffff", "#c084fc"
]))
pen.write(
    random.choice(messages),
    align="center",
    font=("Arial", 8, "bold")
)

screen.update()
turtle.done()
