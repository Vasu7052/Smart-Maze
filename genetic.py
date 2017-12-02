from rocket import Rocket, Vector
import numpy as np
import pygame
import heapq

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bright_red = (255,128,0)
bright_green = (0,255,128)

FPS = 500


class Genetic:

    def __init__(self, title, width, height, iteratons , loc_x, loc_y, population_size=100, mutation_rate=0.1, obstacles=[]):
        # initialize all variables
        self.title = title
        self.width = width
        self.height = height
        self.iteratons = iteratons
        self.target_location = Vector(loc_x, loc_y)
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = []
        self.best_child = Rocket(FPS)
        self.obstacles = obstacles

        for i in range(0, self.population_size):
            self.population.append(Rocket(FPS))

    def _next_gen(self):

        fitness_list = []
        new_generation = []

        for member in self.population:

            fitness = (member.fitness(self.target_location)) * 1000
            fitness_list.append((fitness,member))

        new_list = sorted(fitness_list, key=lambda rkt: rkt[0])

        child1,child2 = new_list[len(new_list)-1][1].crossover(new_list[len(new_list)-2][1])

        child1.mutate(self.mutation_rate)
        child2.mutate(self.mutation_rate)

        for member in self.population:
            if ((member.fitness(self.target_location)) * 1000) == new_list[0][0] :
                new_generation.append(child1)
            elif ((member.fitness(self.target_location)) * 1000) == new_list[1][0] :
                new_generation.append(child2)
            else :
                temp = Rocket(FPS)
                temp.forces = member.forces
                new_generation.append(temp)

        self.population = []
        self.population = new_generation

        self.best_child = new_list[len(new_list)-1][1]


    def simulate_with_graphics(self):

        pygame.init()
        game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        clock = pygame.time.Clock()

        game_exit = False
        counter = 0
        iter_cnt = 0

        while not game_exit and iter_cnt < self.iteratons:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

            game_display.fill(WHITE)

            if counter == FPS:
                counter = 0
                iter_cnt += 1
                self._next_gen()

            for member in self.population:

                if member.is_alive:

                    member.apply_force_at(counter)

                    member.update()

                    for obs in self.obstacles:
                        if obs[0] <= member.location.x <= obs[0]+obs[2] and obs[1] <= member.location.y <= obs[1]+obs[3]:
                            member.is_alive = False

                    if member.location.x <= 10 or member.location.x >= 800 or member.location.y <= 10 or member.location.y >= 600 :
                            member.is_alive = False

                pygame.draw.circle(game_display, green, member.location.tuple_int(),10 )

            counter += 1

            pygame.draw.circle(game_display, RED, self.target_location.tuple_int(), 25)
            font = pygame.font.SysFont("monospace", 20)
            label = font.render("Target", 1, (0, 0, 0))
            game_display.blit(label, (67, 125))

            for obs in self.obstacles:
                pygame.draw.rect(game_display, blue, obs)

            label = font.render("Generation: " + str(iter_cnt+1), 1, (0, 0, 0))
            game_display.blit(label, (10, 512))
            label = font.render("Best Fitness: " + str(self.best_child.fitness(self.target_location)), 1, (0, 0, 0))
            game_display.blit(label, (10, 540))
            label = font.render("Distance: " + str(self.best_child.location.dist(self.target_location)), 1, (0, 0, 0))
            game_display.blit(label, (10, 570))

            pygame.display.update()

            clock.tick(FPS)

        self.print_stats()

    def print_stats(self):
        print("--------------------------------")
        print("Best member from the population:")
        print("Fitness value: ", self.best_child.fitness(self.target_location))
        print("Final location: ", self.best_child.location)
        print("Distance from the target: ", self.best_child.location.dist(self.target_location))
        print("Forces:")
        for f in self.best_child.forces:
            print(f)
        print("--------------------------------")
