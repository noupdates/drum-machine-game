#version 330

// Input vertex attributes (from vertex shader)
in vec2 fragTexCoord;
in vec4 fragColor;

uniform float time;
uniform vec2 boundingBox;
uniform vec4 borderColor;
uniform vec4 backgroundColor;

// Output fragment color
out vec4 finalColor;

// consts
float threshold = 0.01;


void main()
{
    vec2 pixelPos = (fragTexCoord * boundingBox);

    bool isBlack = (fragColor.x < threshold) && (fragColor.y < threshold) && (fragColor.z < threshold);

    if (isBlack) {
        // Do something if fragColor is black
        finalColor = borderColor;
    } else {
        finalColor = backgroundColor;
    }
}

