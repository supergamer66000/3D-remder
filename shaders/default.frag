#version 330 core

layout (location = 0) out vec4 fragcolor;

void main() {
    vec3 color = vec3(1.0, 0.0, 0.0);
    fragcolor = vec4(color, 1.0);
}