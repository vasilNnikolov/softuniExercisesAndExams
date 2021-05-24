from collections import deque
from datetime import timedelta


class Robot:
    def __init__(self, name, time_to_process):
        self.name = name
        self.time_to_process = time_to_process
        self.free = True
        self.task_start_time = None

    def add_task(self, task_start_time, product):
        if self.free:
            self.free = False
            self.task_start_time = task_start_time
            time = "{:0>8}".format(str(timedelta(seconds=task_start_time % (24*3600))))
            print(f"{self.name} - {product} [{time}]")


    def update_robot(self, current_time):
        if not self.free and current_time >= self.task_start_time + self.time_to_process:
            self.free = True


# get robot data
robot_data = input().split(";")

robots = []
for data in robot_data:
    name, time = data.split("-")
    time = int(time)
    robots.append(Robot(name, time))

# get start time
start_time = input()
h, m, s = start_time.split(":")
start_time = int(s) + int(m)*60 + int(h)*3600

# get product data
products = deque([])
command = input()
while command != "End":
    products.appendleft(command)
    command = input()

current_time = start_time + 1
while len(products) > 0:
    for r in robots:
        if r.free:
            r.add_task(current_time, products[-1])
            products.pop()
            break
    else: # no free robot
        products.appendleft(products[-1])
        products.pop()

    current_time += 1
    for r in robots:
        r.update_robot(current_time)

