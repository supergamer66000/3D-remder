import sys
import pygame
import OpenGL
import OpenGL_accelerate
import moderngl as mgl
from model import *

class GraphicsEngine:
    __version__ = 0.1
    def __init__(self, win_size=(854, 480)):
        # init pygame and OpenGL
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        #  create an object to help tack time
        self.clock = pygame.time.Clock()
        # Set Vars
        pygame.display.set_mode(win_size, flags=pygame.OPENGL | pygame.DOUBLEBUF)  # Set window size and Initializes OpenGL for pygame
        # Detect and use existing OpenGL content
        self.ctx = mgl.create_context()
        # scene
        self.scene = Triangle(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.K_ESCAPE):
                self.scene.destroy()
                pygame.quit()
                sys.exit()

    def render(self):
        # Clears Frame buffer
        self.ctx.clear(color=(0, 0, 255))
        # render scene
        self.scene.render()
        # Swaps Buffers
        pygame.display.flip()
    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()