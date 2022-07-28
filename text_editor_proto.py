import pygame
from Button import Button

pygame.init()
screen = pygame.display.set_mode((500,500))
bgc = [128, 137, 150]
color = pygame.Color('black')
input_box = pygame.Rect(10,10,480,480)
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
pygame.display.set_caption("text editor")
screen.fill(bgc)
pygame.display.flip()
text = ''

running = True


run_button = Button(400,420,pygame.image.load('exit_btn.png').convert_alpha(), 0.3)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    max_width -= 7
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


while running:
	screen.fill(bgc)
	run_button.on_screen(screen)
	for event in pygame.event.get():
		if run_button.draw(screen):
			exec(text)
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				text += '\n'
			elif event.key == pygame.K_BACKSPACE:
				text = text[:-1]
			elif event.key == pygame.K_TAB:
				text += '    '
			else:
				text += event.unicode
	# Render the current text.
	txt_surface = font.render(text, True, color)
	# text_rect = txt_surface.get_rect()
	# Resize the box if the text is too long.

	# width = max(200, txt_surface.get_width()+10)
	# input_box.w = width
	# Blit the text.
	blit_text(screen, text,(input_box.x+5, input_box.y+5), font)
	#screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
	# Blit the input_box rect.
	pygame.draw.rect(screen, color, input_box, 2)

	pygame.display.flip()
	clock.tick(30)
