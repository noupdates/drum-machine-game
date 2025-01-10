#version 330

// Input vertex attributes
in vec3 vertexPosition;
in vec2 vertexTexCoord;
in vec3 vertexNormal;
in vec4 vertexColor;

// Input uniform values
uniform mat4 mvp;
uniform mat4 matModel;
uniform mat4 matView;
uniform mat4 matProjection;
uniform mat4 matNormal;

uniform float time;

// Output vertex attributes (to fragment shader)
out vec3 fragPosition;
out vec2 fragTexCoord;
out vec3 fragNormal;
out float height;

void main()
{
    // Displace vertex position
    vec3 displacedPosition = vec3(vertexPosition.x, vertexPosition.y, 0);

    // Send vertex attributes to fragment shader
    fragPosition = vec3(1.0,0,0);
    fragTexCoord = vertexTexCoord;
    fragNormal = normalize(vec3(matNormal*vec4(vertexNormal, 1.0)));
    height = displacedPosition.y * 0.2; // send height to fragment shader for coloring

    // Calculate final vertex position
    gl_Position = mvp*vec4(displacedPosition , 1.0);
}