from turtle import *

# draw the perimeter
for _ in range(4):
    forward(100)
    right(60)
    forward(100)
    right(60)

#draw diagonals
right(60)
for _ in range(2):
    forward(200)
    right(120)
    forward(100)
    right(120)
forward(200)

done()