import pygame
import Planet

class Level:
    def __init__(self, targetNumber, attempts, asteroidPos, planetColors, planetPoses, planetRads):
        self.planetColors = planetColors
        self.planetPoses = planetPoses
        self.asteroidPos = asteroidPos
        self.planetRads = planetRads
        self.targetNumber = targetNumber
        self.attempts = attempts
    
    def get_planets(self):
        planets = []

        for i in range(len(self.planetPoses)):
            planets.append(Planet.Planet(self.planetColors[i], self.planetPoses[i], self.planetRads[i]))

        return planets

    def get_asteroid_pos(self):
        return self.asteroidPos

    def get_target_number(self):
        return self.targetNumber

    def get_attempt_amount(self):
        return self.attempts