import random
import math


class Car():

    def __init__(self, city, location: tuple, goal: tuple):  # Add max speed?

        self.location = location  # (x,y)

        # Current velocity is vector [x,y]

        self.velocity_x = 0
        self.velocity_y = 0
        self.goal = goal             # (x,y) coordinates of goal
        self.max_speed = 6
        self.slowing_distance = 40
        self.city = city
        self.max_steering_force = 1
        self.avoid_radius = 80
        self.max_see_ahead = 2

    # Returns the location of a car
    def get_location(self):
        return self.location

    # Function for updating a car's velocity - Craig Reynolds' formulas
    def update_velocity(self):

        target_offset_x = self.goal[0] - self.location[0] # The length of x we need to drive
        target_offset_y = self.goal[1] - self.location[1] # The length of y we need to drive

        distance = math.sqrt(target_offset_x**2+target_offset_y**2)

        ramped_speed = self.max_speed * (distance / self.slowing_distance)
        clipped_speed = min(ramped_speed, self.max_speed)

        desired_velocity_x = (clipped_speed / distance) * target_offset_x # What is distance is 0?
        desired_velocity_y = (clipped_speed / distance) * target_offset_y

        steering_x = desired_velocity_x - self.velocity_x
        steering_y = desired_velocity_y - self.velocity_y

        if steering_x > 0:
            self.velocity_x += min(steering_x, self.max_steering_force)
        else:
            self.velocity_x += max(steering_x, -self.max_steering_force)

        if steering_y > 0:
            self.velocity_y += min(steering_y, self.max_steering_force)
        else:
            self.velocity_y += max(steering_y, -self.max_steering_force)

        self.evade_cars()

        self.avoid_collision()

        self.set_new_goal()

    # Function for avoiding walls
    def avoid_collision(self):

        ahead_x   = self.location[0] + self.velocity_x * self.max_see_ahead
        ahead_y   = self.location[1] + self.velocity_y * self.max_see_ahead

        ahead_x2 = self.location[0] + self.velocity_x * self.max_see_ahead * 0.5
        ahead_y2 = self.location[1] + self.velocity_y * self.max_see_ahead * 0.5

        closestObstacle = self.find_closest_obstacle(ahead_x, ahead_y, ahead_x2, ahead_y2)

        avoidance_x = 0
        avoidance_y = 0

        if closestObstacle != None:

            avoidance_x = (ahead_x - (closestObstacle[0]*8+4))
            avoidance_y = (ahead_y - (closestObstacle[1]*8+4))

            if avoidance_x >= 0:
                steering_x = min(avoidance_x, self.max_steering_force*3)
                self.velocity_x = min(self.velocity_x + steering_x, self.max_speed)
            else:
                steering_x = max(avoidance_x, -self.max_steering_force*3)
                self.velocity_x = max(self.velocity_x + steering_x, -self.max_speed)

            if avoidance_y >= 0:
                steering_y = min(avoidance_y, self.max_steering_force*3)
                self.velocity_y = min(self.velocity_y + steering_y, self.max_speed)
            else:
                steering_y = max(avoidance_y, -self.max_steering_force*3)
                self.velocity_y = max(self.velocity_y + steering_y, -self.max_speed)


    # Function for finding the closest obstacle
    def find_closest_obstacle(self, ahead_x, ahead_y, ahead_x2, ahead_y2):
        closestObstacle = None

        for obstacle in self.city.walls:
            collision = self.line_intersects_circle(obstacle, ahead_x, ahead_y, ahead_x2, ahead_y2)

            if collision and (closestObstacle == None or self.distance(obstacle) < self.distance(closestObstacle)):
                closestObstacle = obstacle

        return closestObstacle

    # Euclidean distance between obstacle and car
    def distance(self, obstacle):
        return math.sqrt((self.location[0] - (obstacle[0]* 8)) ** 2 + (self.location[1] - (obstacle[1] * 8 )) ** 2)

    # Checks if ahead vector intersects circle around the obstacle
    def line_intersects_circle(self, obstacle, ahead_x, ahead_y, ahead_x2, ahead_y2):
        d1 = math.sqrt((ahead_x - (obstacle[0]*8+4)) ** 2 + (ahead_y - (obstacle[1] *8+4)) ** 2)
        d2 = math.sqrt((ahead_x2 - (obstacle[0]*8+4)) ** 2 + (ahead_y2 - (obstacle[1] *8+4)) ** 2)
        return d1 < 4*10 or d2 < 4*10

    # Function for evading other cars
    def evade_cars(self):
        for car in self.city.cars:
            if car != self:
                d_x = car.location[0] - self.location[0]  # The length of x we need to drive
                d_y = car.location[1] - self.location[1]  # The length of y we need to drive

                distance = math.sqrt(d_x ** 2 + d_y ** 2)
                if distance < self.avoid_radius:
                    ramped_speed = self.max_speed * (distance / self.slowing_distance)
                    clipped_speed = min(ramped_speed, self.max_speed)

                    desired_velocity_x = -(clipped_speed / distance) * d_x  # What is distance is 0?
                    desired_velocity_y = -(clipped_speed / distance) * d_y

                    steering_x = desired_velocity_x - self.velocity_x
                    steering_y = desired_velocity_y - self.velocity_y

                    if steering_x > 0:
                        self.velocity_x += min(steering_x, self.max_steering_force*3)
                    else:
                        self.velocity_x += max(steering_x, -self.max_steering_force*3)

                    if steering_y > 0:
                        self.velocity_y += min(steering_y, self.max_steering_force*3)
                    else:
                        self.velocity_y += max(steering_y, -self.max_steering_force*3)

    # Function for setting a new goal
    def set_new_goal(self):
        # If car is close enough to the current goal, new goal is set
        if abs(self.goal[0] - self.location[0]) < 30 and abs(self.goal[1] - self.location[1]) < 30:
            x = random.randint(0, 800)
            y = random.randint(0, 800)
            # If the new goal is too close to a wall, new random goal is set
            def new_rand():
                nonlocal x, y
                x = random.randint(0, 800)
                y = random.randint(0, 800)
                for wall_location in self.city.walls:
                    wall_x, wall_y = wall_location
                    if abs(wall_x*8 - x) < 30 and abs(wall_y*8 - y) < 30:
                        new_rand()
            new_rand()
            self.goal = (x, y)

    # Rotates car to the direction it is going
    def rotate(self):
        if self.velocity_x == 0 and self.velocity_y == 0:
            return "zero_velocity"
        elif self.velocity_x == 0 and self.velocity_y < 0:
            return 270
        elif self.velocity_x == 0 and self.velocity_y > 0:
            return 90
        else:
            if self.velocity_x > 0:
                return (math.atan(self.velocity_y / self.velocity_x) * (180 / math.pi))
            else:
                return (180 + math.atan(self.velocity_y / self.velocity_x) * (180 / math.pi))