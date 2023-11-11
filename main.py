import pygame

from simulation import Simulation

if __name__ == "__main__":
    pygame.init()
    simulation = Simulation((64, 48))
    simulation.start()
