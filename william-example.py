
from turtle import *

TOP = (1 << 0)
MIDDLE = (1 << 1)
BOTTOM = (1 << 2)

TOP_RIGHT = (1 << 3)
TOP_LEFT = (1 << 4)
BOTTOM_RIGHT = (1 << 5)
BOTTOM_LEFT = (1 << 6)

ZERO = (TOP | TOP_LEFT | TOP_RIGHT | BOTTOM_RIGHT | BOTTOM_LEFT | BOTTOM)
ONE = (BOTTOM_RIGHT | TOP_RIGHT)
TWO = (TOP | TOP_RIGHT | MIDDLE | BOTTOM_LEFT | BOTTOM)
THREE = (TOP | TOP_RIGHT | MIDDLE | BOTTOM_RIGHT | BOTTOM)
FOUR = (TOP_LEFT | TOP_RIGHT | MIDDLE | BOTTOM_RIGHT)
FIVE = (TOP | TOP_LEFT | MIDDLE | BOTTOM_RIGHT | BOTTOM)
SIX = (TOP | TOP_LEFT | MIDDLE | BOTTOM_RIGHT | BOTTOM_LEFT | BOTTOM)
SEVEN = (TOP | BOTTOM_RIGHT | TOP_RIGHT)
EIGHT = (TOP | TOP_LEFT | TOP_RIGHT | MIDDLE | BOTTOM_RIGHT | BOTTOM_LEFT | BOTTOM)
NINE = (TOP | TOP_LEFT | TOP_RIGHT | MIDDLE | BOTTOM_RIGHT | BOTTOM)

A = (TOP | TOP_LEFT | TOP_RIGHT | MIDDLE | BOTTOM_RIGHT | BOTTOM_LEFT)
B = (TOP_LEFT | MIDDLE | BOTTOM_RIGHT | BOTTOM_LEFT | BOTTOM)
C = (TOP | TOP_LEFT | BOTTOM | BOTTOM_LEFT)
D = (TOP_RIGHT | MIDDLE | BOTTOM_RIGHT | BOTTOM_LEFT | BOTTOM)
E = (TOP | TOP_LEFT | MIDDLE | BOTTOM_LEFT | BOTTOM)
F = (TOP | TOP_LEFT | MIDDLE | BOTTOM_LEFT)
G = NINE
H = (TOP_LEFT | TOP_RIGHT | MIDDLE | BOTTOM_LEFT | BOTTOM_RIGHT)
I = (TOP_LEFT | BOTTOM_LEFT)
J = (TOP_RIGHT | BOTTOM | BOTTOM_RIGHT | BOTTOM_LEFT)
K = H
L = (TOP_LEFT | BOTTOM | BOTTOM_LEFT)
M = (TOP | BOTTOM_LEFT | BOTTOM_RIGHT)
N = (MIDDLE | BOTTOM_RIGHT | BOTTOM_LEFT)
O = ZERO
P = (TOP | TOP_LEFT | TOP_RIGHT | MIDDLE | BOTTOM_LEFT)
Q = (TOP | TOP_LEFT | TOP_RIGHT | MIDDLE | BOTTOM_RIGHT)
R = (MIDDLE | BOTTOM_LEFT)
S = FIVE
T = (TOP_LEFT | MIDDLE | BOTTOM_LEFT | BOTTOM)
U = (TOP_LEFT | TOP_RIGHT | BOTTOM_RIGHT | BOTTOM_LEFT | BOTTOM)
V = (BOTTOM_RIGHT | BOTTOM_LEFT | BOTTOM)
W = (TOP_LEFT | TOP_RIGHT | BOTTOM)
X = H
Y = (TOP_RIGHT | BOTTOM | BOTTOM_RIGHT | TOP_LEFT | MIDDLE)
Z = TWO

SPACE = 0
UNDEFINED = (MIDDLE)

LINE_LENGTH = 40
SEGMENT_SPACING = 80

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

drawAngle = 0


letters = [A, B, C, D, E, F, G, H, I, J, K, L, M, 
        N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 
        ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, 
        SPACE, UNDEFINED]

def reset_position():
    goto(0, 0)


def move(length, direction):
    setheading(direction + drawAngle)
    forward(length)

def draw_line(length, direction):
    pendown()
    move(length, direction)
    penup()


def draw_segment(segment):

    for i in range(7):
        bit = segment & (1 << i)

        draw_segment_bit(bit)

def draw_segment_bit(segmentBit):
    if segmentBit == TOP:
        draw_line(LINE_LENGTH, RIGHT)
        move(LINE_LENGTH, LEFT)

    if segmentBit == MIDDLE:
        move(LINE_LENGTH, DOWN)
        draw_line(LINE_LENGTH, RIGHT)
        move(LINE_LENGTH, LEFT)
        move(LINE_LENGTH, UP)

    if segmentBit == BOTTOM:
        move(LINE_LENGTH, DOWN)
        move(LINE_LENGTH, DOWN)
        draw_line(LINE_LENGTH, RIGHT)
        move(LINE_LENGTH, LEFT)
        move(LINE_LENGTH, UP)
        move(LINE_LENGTH, UP)

    if segmentBit == TOP_RIGHT:
        move(LINE_LENGTH, RIGHT)
        draw_line(LINE_LENGTH, DOWN)
        move(LINE_LENGTH, UP)
        move(LINE_LENGTH, LEFT)

    if segmentBit == TOP_LEFT:
        draw_line(LINE_LENGTH, DOWN)
        move(LINE_LENGTH, UP)

    if segmentBit == BOTTOM_RIGHT:
        move(LINE_LENGTH, RIGHT)
        move(LINE_LENGTH, DOWN)
        draw_line(LINE_LENGTH, DOWN)
        move(LINE_LENGTH, UP)
        move(LINE_LENGTH, UP)
        move(LINE_LENGTH, LEFT)

    if segmentBit == BOTTOM_LEFT:
        move(LINE_LENGTH, DOWN)
        draw_line(LINE_LENGTH, DOWN)
        move(LINE_LENGTH, UP)
        move(LINE_LENGTH, UP)

def draw_text(text):

    indexs = []

    for i in range(len(text)):
        indexs.append(ord(text[i]) - ord('a'))

    for i in range(len(text)):
        index = indexs[i]

        reset_position()
        move(SEGMENT_SPACING * i, RIGHT)
        draw_segment(letters[index])


color('red', 'yellow')
speed('fastest')

for i in range(4):

    reset_position()
    penup()
    draw_segment(W)
    draw_text("william")
    drawAngle = drawAngle + 90