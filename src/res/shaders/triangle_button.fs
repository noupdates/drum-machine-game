#version 330

// Input vertex attributes (from vertex shader)
in vec2 fragTexCoord;
in vec4 fragColor;

uniform float time;
uniform vec2 boundingBox;
uniform vec4 hoverColor;
uniform vec4 backgroundColor;
uniform vec4 actionColor;

uniform bool isHovering;
uniform bool isActing;
uniform bool reverse;

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
//    vec2 centeredPixelPos = ((fragTexCoord - vec2(1,1)) * boundingBox);
    vec2 leftAlignedCoords = (fragTexCoord - vec2(1,1.5))*vec2(1,2);

    if (reverse) {
        leftAlignedCoords -= vec2(1,0);
    }

    finalColor = mix(vec4(0, 0, 0, 0), getStateColor(), step(abs(leftAlignedCoords.y), abs(leftAlignedCoords.x)));
}
