from collections import deque

green_time = int(input())
free_time = int(input())

command = input()

horisontal, vertical = deque([]), deque([]) # queues to hold the characters of the cars of the horisontal and vertical roads
horisontal_passing = True
middle_char = " "
while command != "End":
    if command == "green":
        horisontal_passing = not horisontal_passing




