#version 330 core

layout (location=0) in vec2 vertexPos;
layout (location=1) in vec2 vertexTexCoord;

out vec2 uv;

void main()
{
    gl_Position = vec4(vertexPos, 0.0, 1.0);
    uv = vertexTexCoord;
}