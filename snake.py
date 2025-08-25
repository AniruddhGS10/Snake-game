from turtle import Turtle

# Constants for movement directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # List to store snake body segments
        self.snake_segments = []
        # Starting x-coordinate for initial snake creation
        self.x_axis = 0
        # Turtle drawing speed
        self.speed = 1
        # Initial number of segments
        self.new_segment = 3
        # Create the initial snake
        self.create_snake()
        # Reference to the snake's head (first segment)
        self.head = self.snake_segments[0]

    def create_snake(self):
        """Create the initial snake with a set number of segments."""
        for turtles in range(self.new_segment):
            self.add_segment(turtles)

    def add_segment(self, turtles):
        """Add a new segment to the snake body."""
        self.new_segment += 1
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.speed(self.speed)
        turtle.goto(x=self.x_axis, y=0)   # Place segment next to the previous one
        self.x_axis -= 20                 # Update x position for the next segment
        self.snake_segments.append(turtle)

    def extend(self):
        """Extend the snake by adding a new segment at the tail."""
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        """Move the snake forward by shifting each segment to the position of the one before it."""
        for segments in range(len(self.snake_segments)-1, 0, -1):
            new_x = self.snake_segments[segments-1].xcor()
            new_y = self.snake_segments[segments-1].ycor()
            self.snake_segments[segments].goto(new_x, new_y)
        self.head.forward(20)  # Move head forward

    def up(self):
        """Change direction: move up (if not currently moving down)."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction: move down (if not currently moving up)."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction: move left (if not currently moving right)."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction: move right (if not currently moving left)."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
