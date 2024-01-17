import OpenGL.GL
import OpenGL_accelerate
import numpy as np

class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        self.vao = self.get_vao()
    def render(self):
        self.vao.render()
    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()
    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, 'f3', 'in_position')])
        return vao
    def get_vertex_data(self):
        vertex_data = [(-0.6, -0.8, 0.0), (0.6, -0.8, 0.0), (0.0, 0.8, 0.0)]
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data.astype('f4'))
        return vbo
    def get_shader_program(self, shader_name):
        # Read vertex shader
        with open(f'shaders/{shader_name}.vert') as f:
            vertex_shader = f.read()
        # Reads fragment shader
        with open(f'shaders/{shader_name}.frag') as f:
            fragment_shader = f.read()
        # Get the Vertex and Fragment shaders
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
