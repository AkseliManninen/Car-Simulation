import unittest
import math

from car import Car
from city import City
from coordinates import Coordinates
from square import Square

class Test(unittest.TestCase):

    def testCityAddCar(self):
        city = City(100, 100)
        car = Car(city, (100, 100), (600, 600))
        city.add_car(car)
        self.assertTrue(len(city.cars) ==1)

    def testCityAddWall(self):
        city = City(100, 100)
        city.add_wall(Coordinates(30,30), 30, 30)
        city.add_wall(Coordinates(40,40), 40, 40)
        self.assertTrue(len(city.walls)==2)

    def testCarGetLocation(self):
        city = City(100, 100)
        car = Car(city, (100, 100), (600, 600))
        self.assertEqual(car.get_location(), (100, 100))

    def testCarSetNewGoalClose(self):
        city = City(100, 100)
        car = Car(city, (520, 520), (500, 500))
        self.assertEqual(car.goal, (500, 500))
        car.set_new_goal()
        self.assertNotEqual(car.goal, (500, 500))

    def testCarSetNewGoalFar(self):
        city = City(100, 100)
        car = Car(city, (200, 200), (500, 500))
        self.assertEqual(car.goal, (500, 500))
        car.set_new_goal()
        self.assertEqual(car.goal, (500, 500))

    def testCarRotate(self):
        city = City(100, 100)
        car = Car(city, (200, 200), (500, 500))
        self.assertEqual(car.rotate(), "zero_velocity")
        car.velocity_y = 2
        self.assertEqual(car.rotate(), 90)
        car.velocity_x = 1
        self.assertEqual(car.rotate(), math.atan(2 / 1) * (180 / math.pi))

    def testCarUpdateVelocity(self):
        city = City(100, 100)
        car = Car(city, (200, 200), (500, 100))
        self.assertEqual(car.velocity_y, 0)
        self.assertEqual(car.velocity_x, 0)
        car.update_velocity()
        v_x1 = car.velocity_x
        v_y1 = car.velocity_y
        self.assertGreater(car.velocity_x, 0)
        self.assertLess(car.velocity_y, 0)
        car.update_velocity()
        self.assertGreater(car.velocity_x, v_x1)
        self.assertLess(car.velocity_y, v_y1)

    def testCarFindClosestObstacle(self):
        city = City(100, 100)
        car = Car(city, (200, 200), (500, 500))
        car.velocity_x = 1
        car.velocity_y = 1
        self.assertTrue(car.find_closest_obstacle((200+1*2), (200+1*2), (200+1), (200+1)) == None)
        city.add_wall(Coordinates(10, 10), 10, 10)
        self.assertTrue(car.find_closest_obstacle((200+1*2), (200+1*2), (200+1), (200+1)) == None)
        city.add_wall(Coordinates(28, 28), 28, 28)
        self.assertTrue(car.find_closest_obstacle((200 + 1 * 2), (200 + 1 * 2), (200 + 1), (200 + 1)) == city.walls[1])
        city.add_wall(Coordinates(27, 27), 27, 27)
        self.assertTrue(car.find_closest_obstacle((200 + 1 * 2), (200 + 1 * 2), (200 + 1), (200 + 1)) == city.walls[2])


    def testCarAvoidCollision(self):
        city = City(100, 100)
        car = Car(city, (200, 200), (500, 500))
        car.velocity_x = 1
        car.velocity_y = 1
        city.add_wall(Coordinates(27, 27), 27, 27)
        car.avoid_collision()
        self.assertTrue(car.velocity_y < 1)
        self.assertTrue(car.velocity_x < 1)

    def testCarEvadeCars(self):
        city = City(100, 100)
        car = Car(city, (200, 200), (500, 500))
        car.velocity_x = 2
        car.velocity_y = 2
        car2 = Car(city, (400, 400), (500, 500))
        city.add_car(car)
        city.add_car(car2)
        car.evade_cars()
        self.assertTrue(car.velocity_x == 2)
        car3 = Car(city, (430, 430), (500, 500))
        city.add_car(car3)
        car2.velocity_x = 3
        car2.velocity_y = 3
        car2.evade_cars()
        car3.velocity_x = 3
        car3.velocity_y = 3
        car3.evade_cars()
        self.assertTrue(car2.velocity_x < 3)
        self.assertTrue(car2.velocity_y < 3)
        self.assertTrue(car3.velocity_x > 3)
        self.assertTrue(car3.velocity_y > 3)


    def testSquareSetWall(self):
        square = Square()
        self.assertFalse(square.is_wall_square())
        square.set_wall()
        self.assertTrue(square.is_wall_square())

    def testCoordinates(self):
        coor = Coordinates(10, 10)
        self.assertTrue(coor.get_x() == 10 and coor.get_y() == 10)

if __name__ == "__main__":
    unittest.main()