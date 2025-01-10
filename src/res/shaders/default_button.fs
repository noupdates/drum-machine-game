#version 330

// Input vertex attributes (from vertex shader)
in vec2 fragTexCoord;
in vec4 fragColor;

uniform float time;
uniform vec2 boundingBox;
uniform vec4 hoverColor;
uniform vec4 backgroundColor;
uniform vec4 actionColor;
uniform float opacity;

uniform bool isHovering;
uniform bool isActing;

uniform sampler2D texture0;
uniform vec4 colDiffuse;

// Output fragment color
out vec4 finalColor;

// NOTE: Add here your custom variables
float threshold = 0.01;

vec4 getStateColor() {
    return (isActing ? actionColor : (isHovering ? hoverColor : backgroundColor));
}

void main()
{
    // Texel color fetching from texture sampler
    vec4 texelColor = texture(texture0, fragTexCoord)*fragColor;
    finalColor = texelColor * vec4(getStateColor().rgb, opacity);
}
