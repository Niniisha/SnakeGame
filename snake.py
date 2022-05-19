from turtle import Turtle
STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270      # Setting CONSTANTS for starting position, distance, up, down, left, right
LEFT = 180
RIGHT = 0


class Snake:   # Setting snake class
    def __init__(self):  # Attributes
        self.segments = []
        self.create_snake() # Adding create_snake function, so it will be initialized when game start
        self.head = self.segments[0]   # Setting head segment to be 1st item in segments list

    def create_snake(self): # Function for creating snake at beggining
        for position in STARTING_POSITION:
            self.add_segment(position)  # Appending our segments in attribute

    def add_segment(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    # Add additional segment when eats the food
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Snake movements when we press keys
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

