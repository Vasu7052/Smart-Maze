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

    def __init__(self, loc_x, loc_y, population_size=100, mutation_rate=0.1, obstacles=[]):
        # initialize all variables
        self.target_location = Vector(loc_x, loc_y)
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = []
        self.best_child = Rocket(FPS)
        self.obstacles = obstacles

        # initialize the rockets at random values
        for i in range(0, self.population_size):
            self.population.append(Rocket(FPS))

    # implementation of the genetic algorithm
    def _next_gen(self):

        # define aux variables for genetic algirthm
        fitness_list = []
        new_generation = []

        for member in self.population:

            # calculate the fitness for every member from the population
            fitness = (member.fitness(self.target_location)) * 1000
            fitness_list.append((fitness,member))

        new_list = sorted(fitness_list, key=lambda rkt: rkt[0])

        child1,child2 = new_list[len(new_list)-1][1].crossover(new_list[len(new_list)-2][1])

        # the child will suffer a mutation according to the probability of the mutation rate
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


    def simulate_with_graphics(self, title="Rockets", width=800, height=600, iteratons=300):

        # initialize pygame
        pygame.init()
        game_display = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # get the clock module for handling FPS
        clock = pygame.time.Clock()

        # set an exit flag
        game_exit = False

        # set a counter for handling genetic algorithm steps at given moments
        counter = 0

        # iteration counter
        iter_cnt = 0

        # start the main loop
        while not game_exit and iter_cnt < iteratons:

            # handle input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

            # clear the playground
            game_display.fill(BLACK)

            if counter == FPS:

                # reset the counter to 0
                counter = 0

                # increment iter
                iter_cnt += 1

                # compute the newer generation of the population
                self._next_gen()

            for member in self.population:

                # check if rocket did not collide before
                if member.is_alive:

                    # calculate the new position for every rocket
                    member.apply_force_at(counter)

                    # update the rocket's position
                    member.update()

                    # check member's collision with the obstacles
                    for obs in self.obstacles:
                        if obs[0] <= member.location.x <= obs[0]+obs[2] and obs[1] <= member.location.y <= obs[1]+obs[3]:
                            member.is_alive = False
                        elif member.location.x <= 0 or member.location.x >= 800 or member.location.y <= 0 or member.location.y >= 600 :
                            member.is_alive = False


                # display the rockets
                pygame.draw.circle(game_display, WHITE, member.location.tuple_int(), 3)

            counter += 1

            # display the target position
            pygame.draw.circle(game_display, RED, self.target_location.tuple_int(), 3)

            # draw the obstacles
            for obs in self.obstacles:
                pygame.draw.rect(game_display, WHITE, obs)

            # display iteration number to the screen
            font = pygame.font.SysFont("monospace", 20)
            label = font.render("Generation: " + str(iter_cnt+1), 1, (255, 255, 255))
            game_display.blit(label, (200, 10))
            label = font.render("Max Fitness: " + str(self.best_child.fitness(self.target_location)), 1, (255, 255, 255))
            game_display.blit(label, (200, 30))
            label = font.render("Distance: " + str(self.best_child.location.dist(self.target_location)), 1, (255, 255, 255))
            game_display.blit(label, (200, 50))

            # update the display
            pygame.display.update()

            # sleep the mainloop for achieving the preset FPS value
            clock.tick(60)

        # print statistics for the best child when the main loop is finished
        self.print_stats()

    # display stats for the best child
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
