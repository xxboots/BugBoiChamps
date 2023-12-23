import random
import pygame


class Particle:
    def __init__(self):
        self.particles = []

    def emit(self, screen):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(screen,
                                   random.choice([pygame.Color('White'),
                                                  pygame.Color('Red'),
                                                  pygame.Color('Orange')]),
                                   particle[0],
                                   particle[1])

    def add_particles(self, x, y):
        for index in range(0, 25):
            pos_x = x
            pos_y = y
            radius = 6
            direction_x = random.randint(-4, 4)
            direction_y = random.randint(-4, 4)
            particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
            self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy


particles = Particle()
