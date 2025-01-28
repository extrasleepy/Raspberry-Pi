import pygame
import subprocess
import threading
import queue
import textwrap
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TinyLLama in Pygame")

# Fonts and colors
FONT = pygame.font.Font(None, 28)
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
INPUT_BOX_COLOR = (50, 50, 50)

# Input box
input_box = pygame.Rect(50, 500, 700, 32)
input_text = ""
response_text = ""

# Queue to handle TinyLLama responses
response_queue = queue.Queue()

# Function to interact with TinyLLama
def run_tinyllama(question):
    try:
        process = subprocess.Popen(
            ["ollama", "run", "tinyllama"],  # Replace with your TinyLLama executable or command
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, _ = process.communicate(input=question)
        response_queue.put(output.strip())
    except Exception as e:
        response_queue.put(f"Error: {e}")

# Function to wrap text for rendering
def wrap_text(text, font, max_width):
    lines = []
    for line in text.splitlines():
        lines.extend(textwrap.wrap(line, width=max_width))
    return lines

# Main loop variables
clock = pygame.time.Clock()
running = True
waiting_for_response = False

# Main Pygame loop
while running:
    screen.fill(BG_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not waiting_for_response:
                # Send question to TinyLLama
                waiting_for_response = True
                response_text = ""  # Clear the old response
                threading.Thread(target=run_tinyllama, args=(input_text,)).start()
                input_text = ""  # Clear the input box
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Check for TinyLLama response
    if waiting_for_response and not response_queue.empty():
        response_text = response_queue.get()
        waiting_for_response = False

    # Draw input box
    pygame.draw.rect(screen, INPUT_BOX_COLOR, input_box, border_radius=5)
    text_surface = FONT.render(input_text, True, TEXT_COLOR)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Draw wrapped response text
    if response_text:
        wrapped_lines = wrap_text(response_text, FONT, 80)  # Adjust width as needed
        y_offset = 30
        for line in wrapped_lines:
            response_surface = FONT.render(line, True, TEXT_COLOR)
            screen.blit(response_surface, (30, y_offset))
            y_offset += 30

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
