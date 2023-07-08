import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Player dimensions
PLAYER_SIZE = 50

# Projectile dimensions
PROJECTILE_SIZE = 10

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blue Square Player")

# Player coordinates
player_x = WIDTH // 2
player_y = HEIGHT // 2

# Player speed
player_speed = 0.5

# Projectile coordinates
projectile_x = None
projectile_y = None

# Projectile speed
projectile_speed = 10

# Projectile direction
projectile_direction = None

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire projectile
                    projectile_x = player_x
                    projectile_y = player_y
                    projectile_direction = pygame.key.get_pressed()

    # Get the keys currently being pressed
    keys = pygame.key.get_pressed()

    # Update player position based on keys pressed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Update projectile position
    if projectile_x is not None and projectile_y is not None:
        if projectile_direction[pygame.K_w]:
            projectile_y -= projectile_speed
        if projectile_direction[pygame.K_s]:
            projectile_y += projectile_speed
        if projectile_direction[pygame.K_a]:
            projectile_x -= projectile_speed
        if projectile_direction[pygame.K_d]:
            projectile_x += projectile_speed

    # Fill the window with a white background
    window.fill((255, 255, 255))

    # Draw the player
    pygame.draw.rect(window, BLUE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    # Draw the projectile
    if projectile_x is not None and projectile_y is not None:
        pygame.draw.rect(window, RED, (projectile_x, projectile_y, PROJECTILE_SIZE, PROJECTILE_SIZE))

    # Update the display
    pygame.display.flip()

# Quit the game
