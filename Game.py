import pygame

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Speed of the ball
ball_move_x = 1
ball_move_y = 1

# Position of the ball
ball_x = 500
ball_y = 350
ball_radius = 10


class Player(pygame.sprite.Sprite):
    """
    Create the paddles, set their initial positions, set their graphical representation
    and control their movements
    """

    def __init__(self, x, y, color=BLACK):
        super().__init__()

        # Paddles configuration - Size and color
        self.image = pygame.Surface([20, 100])
        self.image.fill(BLACK)

        # Paddles graphical representation - Rectangles
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_down(self, pixels):
        """
        Function that moves the paddle down

        :param pixels: The amount the paddle moves down
        :return: New location of the paddle
        """
        if self.rect.y + 100 >= 700:
            self.rect.y -= pixels
        else:
            self.rect.y += pixels

    def move_up(self, pixels):
        """
        Function that moves the paddle up

        :param pixels: The amount the paddle moves up
        :return: New location of the paddle
        """
        if self.rect.y - pixels <= 0:
            self.rect.y += pixels
        else:
            self.rect.y -= pixels


# Create the players - (x initial position, y initial position)
paddle_A = Player(50, 400)
paddle_B = Player(950, 400)

# List of all sprites in the game
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle_A)
all_sprites_list.add(paddle_B)

# Initialise pygame
pygame.init()
canvas = pygame.display.set_mode([1000, 700])
canvas.fill(WHITE)
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(120)

# Scores of Player1 and Player 2
Player1score = 0
Player2score = 0

# Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Moving the paddles up and down with UP, DOWN, W and S keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        paddle_A.move_up(1)
    if keys[pygame.K_DOWN]:
        paddle_A.move_down(1)
    if keys[pygame.K_w]:
        paddle_B.move_up(1)
    if keys[pygame.K_s]:
        paddle_B.move_down(1)

    # Boundaries for the ball against the 4 walls
    ball_x += ball_move_x
    ball_y += ball_move_y
    if ball_x <= 0:
        ball_move_x = +1
        Player2score += 1
    if ball_x >= 1000:
        ball_move_x = -1
        Player1score += 1
    if ball_y <= 0:
        ball_move_y = +1
    if ball_y >= 700:
        ball_move_y = -1

    # Collision detection between the ball and the paddles
    if ball_x <= paddle_A.rect.x + 20 and ball_x + ball_radius >= paddle_A.rect.x:
        if ball_y >= paddle_A.rect.y and ball_y + ball_radius <= paddle_A.rect.y + 100:
            ball_move_x = +1
    if ball_x + ball_radius >= paddle_B.rect.x and ball_x <= paddle_B.rect.x + 100:
        if ball_y >= paddle_B.rect.y and ball_y + ball_radius <= paddle_B.rect.y + 100:
            ball_move_y = -1

    # Scoring system for Player1 and Player2
    font = pygame.font.Font(None, 70)
    text = font.render(str(Player1score), 1, BLACK)
    canvas.blit(text, (450, 10))
    text = font.render(str(Player2score), 1, BLACK)
    canvas.blit(text, (550, 10))

    # Create the ball
    pygame.draw.circle(canvas, RED, (ball_x, ball_y), ball_radius)
    pygame.display.update()
    canvas.fill(WHITE)
    all_sprites_list.draw(canvas)

quit(pygame)
