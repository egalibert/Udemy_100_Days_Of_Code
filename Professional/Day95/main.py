import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants

WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
BULLET_SPEED = 7
ALIEN_SPEED = 2
ALIEN_COUNT = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Shooter")



# Load images
player_image = pygame.image.load("ship.png")
alien_image = pygame.image.load("invader.png")
bullet_image = pygame.image.load("bullet.png")

# Scale images
player_image = pygame.transform.scale(player_image, (50, 50))
alien_image = pygame.transform.scale(alien_image, (50, 50))
bullet_image = pygame.transform.scale(bullet_image, (10, 30))

# Game objects
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 70, 50, 50)
bullets = []
aliens = [pygame.Rect(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT // 2), 50, 50) for _ in range(ALIEN_COUNT)]

# Game loop
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and player.left > 0:
		player.x -= PLAYER_SPEED
	if keys[pygame.K_RIGHT] and player.right < WIDTH:
		player.x += PLAYER_SPEED



	# Shoot bullets
	if keys[pygame.K_SPACE]:
		bullet = pygame.Rect(player.centerx - 5, player.top, 10, 30)
		bullets.append(bullet)

	# Move bullets
	bullets = [bullet for bullet in bullets if bullet.move_ip(0, -BULLET_SPEED) and bullet.bottom > 0]

	# Move aliens
	for alien in aliens:
		alien.move_ip(0, ALIEN_SPEED)
		if alien.bottom > HEIGHT:
			alien.y = 0
			alien.x = random.randint(0, WIDTH - 50)

	# Check for collisions
	for bullet in bullets:
		for alien in aliens:
			if bullet.colliderect(alien):
				aliens.remove(alien)
				bullets.remove(bullet)
				aliens.append(pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50))



	# Draw everything
	screen.fill(WHITE)
	screen.blit(player_image, player)

	for alien in aliens:
		screen.blit(alien_image, alien)

	for bullet in bullets:
		screen.blit(bullet_image, bullet)

	pygame.display.flip()
	clock.tick(60)