#version 330

// Input vertex attributes (from vertex shader)
in vec2 fragTexCoord;
in vec4 fragColor;

uniform float time;
uniform vec2 boundingBox;
uniform vec4 borderColor;
uniform vec4 backgroundColor;
uniform vec4 foregroundColor;
uniform float opacity;
uniform sampler2D texture0;

// Output fragment color
out vec4 finalColor;

// consts
float threshold = 0.01;


void main()
{
    vec4 texelColor = texture(texture0, fragTexCoord)*fragColor;
    bool isBlack = (texelColor.x < threshold) && (texelColor.y < threshold) && (texelColor.z < threshold);
    if (isBlack) {
        finalColor = vec4(foregroundColor.rgb, foregroundColor.a * texelColor.a * opacity);
    } else {
        finalColor = vec4(backgroundColor.rgb, backgroundColor.a * texelColor.a * opacity);
    }
}

