import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36)

questions = [
    {"question": "What is AI?", "options": ["A robot", "Machine intelligence", "A programming language"], "answer": 1}
]

def run_quiz():
    current_question = 0
    while True:
        screen.fill((255, 255, 255))
        question_text = font.render(questions[current_question]["question"], True, (0, 0, 0))
        screen.blit(question_text, (50, 50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()

if __name__ == "__main__":
    run_quiz()