import pygame
from utilities import load_png

class Cactus(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('../assets/Cactus.png')
		self.rect = self.rect.inflate(-32, -32)

		self.x = 1080
		self.y = 415
		self.rect.x = 1080
		self.rect.y = 415

		self.v = 4 #Velocity
		self.move = True

		screen = pygame.display.get_surface()
		self.area = screen.get_rect()

	def reinit(self):
		'''Moves Cactus to position'''
		self.x = 1080
		self.y = 415
		self.rect.x = 1080
		self.rect.y = 415
		self.v = 4
		self.move = True

	def freezeCact(self):
		'''Stops cactus in collision'''
		self.move = False

	def draw(self, screen):
		'''Speeds up cactus'''
		if self.move:
			if self.rect.x < -50:
				self.rect.x = 1080
			self.rect.x -= self.v
			self.v += 1/500

		screen.blit(self.image, (self.rect.x, self.rect.y))