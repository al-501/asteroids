import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	
	Player.containers = updateable, drawable
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	shots = pygame.sprite.Group()
	Shot.containers = shots, updateable, drawable
	
	asteroids = pygame.sprite.Group()
	Asteroid.containers = updateable, drawable, asteroids

	AsteroidField.containers = (updateable)
	Asteroid_field = AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for obj in updateable:
			obj.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game Over!")
				sys.exit()
			
		for bullet in shots:
			for asteroid in asteroids:
				if asteroid.collision(bullet):
					bullet.kill()
					asteroid.split()

		screen.fill((0,0,0))

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000
		



if __name__ == "__main__":
	main()
