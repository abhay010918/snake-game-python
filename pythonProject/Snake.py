from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # Initialize the snake with an empty list of segments and create the initial snake
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create the initial snake by adding segments at predefined positions
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        # Add a new segment to the snake at a specified position
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Extend the snake by adding a new segment at the last position
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake by updating the positions of its segments
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Change the snake's direction to upward if it's not currently moving downward
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to downward if it's not currently moving upward
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the snake's direction to leftward if it's not currently moving rightward
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the snake's direction to rightward if it's not currently moving leftward
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
