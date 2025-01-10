#version 330

out vec4 colorOut;

uniform float time;
in uniform vec3 fragPosition;


void main()
{
    colorOut = vec4(fragPosition, 1.0);
}