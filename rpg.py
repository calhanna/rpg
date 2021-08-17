import pygame, pytmx
from player import Player

WIDTH = 640
HEIGHT = 640

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))	# Init pygame window

clock = pygame.time.Clock()

def load_map(path_to_file):
	map = pytmx.load_pygame(path_to_file)

	return map

def setup(level):
	sprites = pygame.sprite.Group()

	player = Player()

	sprites.add(player)

	game_map = load_map('maps/' + level + '.tmx')

	return sprites, player, game_map, game_map.tilewidth, game_map.tileheight

sprites, player, game_map, tilewidth, tileheight = setup('test_level')

def handle_event(event):	# Function to handle pygame events, trying to keep the main loop tidy
	if event.type == pygame.QUIT:
		pygame.quit()
		return True
	return False

def draw():
	screen.fill((255,255,255))

	for x, y, gid in game_map.get_layer_by_name("Floor"):
		screen.blit(game_map.get_tile_image_by_gid(gid), (x * tilewidth, y * tileheight))

	sprites.draw(screen)

	pygame.display.flip()

done = False
while not done:
	for event in pygame.event.get():
		done = handle_event(event) # If we quit, this function evaluates to True, quitting the game

	if done: break

	sprites.update() # Every sprite has an update class. The player's moves itself.

	draw()

	clock.tick(60)	# lock to 60fps
	pygame.display.update()
