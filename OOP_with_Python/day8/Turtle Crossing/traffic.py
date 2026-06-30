from car import Car
import random


class Traffic:
    def __init__(self):

        colors = ["blue", "red", "black", "brown", "dark blue",
                  "black", "purple", "yellow", "dark blue", "black"]

        self.cars = []

        y = 300

        for color in colors:
            x = random.randint(-300, 300)

            car = Car(color)
            car.goto(x, y)
            car.car2.goto(x + 200, y)
            self.cars.append(car)

            y -= 60


    def select_speed(self):
        return random.choice([ 0.9,1,1.2,1.5])


    def move(self):
        for car in self.cars:

            dist = self.select_speed()
            car.forward(dist)
            car.car2.forward(dist)

            if car.car2.xcor() < -370:
                y = car.ycor()
                car.goto(360, y)
                car.car2.goto(360+200, y)

    def collision(self, player):

        player_x = player.xcor()
        player_y = player.ycor()

        for i in self.cars:
            if (i.xcor() - 40 <= player_x <= i.xcor() + 40 and
                i.ycor() - 10 <= player_y <= i.ycor() + 10):
                return True

            if (i.car2.xcor() - 40 <= player_x <= i.car2.xcor() + 40 and
                i.car2.ycor() - 10 <= player_y <= i.car2.ycor() + 10):
                return True

        return False