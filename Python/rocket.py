import numpy as np


class Vector:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __str__(self):
        return "(" + str(self.x) + " " + str(self.y) + ")"

    def nul(self):
        self.x, self.y = 0.0, 0.0

    def dist(self, other):
        x_dist = self.x - other.x
        y_dist = self.y - other.y
        return np.sqrt(x_dist * x_dist + y_dist * y_dist)

    def tuple_int(self, offset=0.0):
        return int(self.x + offset), int(self.y + offset)

    @staticmethod
    def random():
        return Vector(np.random.uniform(0, 2.0) - 1.0, np.random.uniform(0, 2.0) - 1.0)


class Rocket:

    def __init__(self, length):

        self.location = Vector(700,100)
        self.acceleration = Vector()
        self.velocity = Vector()

        self.forces = []
        self.length = length

        self.is_alive = True

        for i in range(0, length):
            self.forces.append(Vector.random())

    def fitness(self, target):

        inv_dist_to_target = 1.0 / self.location.dist(target)

        fitness_rate = 1.0
        if not self.is_alive:
            fitness_rate = 0.000000000001

        return inv_dist_to_target * fitness_rate

    def crossover(self, other):

        child1 = Rocket(self.length)
        child2 = Rocket(self.length)

        midpoint = np.random.random_integers(1, other.length)

        for i in range(0, other.length):

            if i < midpoint:
                child1.forces[i] = other.forces[i]
                child2.forces[i] = self.forces[i]
            else:
                child1.forces[i] = self.forces[i]
                child2.forces[i] = other.forces[i]

        return child1,child2

    def mutate(self, mutation_rate):
        for i in range(0, self.length):
            rand_value = np.random.rand()
            if rand_value < mutation_rate:
                self.forces[i] = Vector.random()

    def apply_force(self, force):
        self.acceleration += force

    def apply_force_at(self, at):
        self.acceleration += self.forces[at]

    def update(self):
        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration.nul()
