#version 330

// Input vertex attributes (from vertex shader)
in vec2 fragTexCoord;
in vec4 fragColor;

uniform float time;
uniform vec2 boundingBox;
//uniform vec4 borderColor;
//uniform vec4 backgroundColor;

// Output fragment color
out vec4 finalColor;


float frequencySpectrum(float x, float time) {
    // Normalize x to be within [-1, 1]
    // Parabolic scaling function to emphasize the center
    float centerScale = pow(2.718, -pow(x * 1.1, 2));

    // Calculate the cycle time and apply an exponential ease-in-out
    float cycleTime = mod(2 * time, 4.0);  // 4-second loop
    float interp = fract(cycleTime);   // Interpolation factor within each stage

    // Exponential ease-in-out function
    interp = interp < 0.5 ? pow(interp * 2.0, 3.0) * 0.5 : 1.0 - pow((1.0 - interp) * 2.0, 3.0) * 0.5;

    // Define four configurations with decreased frequencies for each
    float frequencyA[] = float[5](10.0, 18.0, 8.0, 12.0, 1.0);
    float frequencyB[] = float[5](2.0, 9.0, 14.0, 20.0, 8.0);
    float frequencyC[] = float[5](3.0, 5.0, 10.0, 15.0, 6.0);
    float frequencyD[] = float[5](4.0, 6.0, 12.0, 16.0, 4.0);

    float amplitudeA[] = float[5](0.3, -0.5, 0.4, 0.35, -0.2);
    float amplitudeB[] = float[5](-0.1, 0.2, -0.3, 0.25, 0.6);
    float amplitudeC[] = float[5](0.4, -0.3, 0.2, -0.45, 0.5);
    float amplitudeD[] = float[5](-0.2, -0.4, 0.25, 0.3, 0.6);

    // Interpolate between the four stages based on the cycleTime
    float spectrum = 0.0;
    for (int i = 0; i < 5; i++) {
        float frequency, amplitude;

        // Select configurations based on the cycle stage and interpolate
        if (cycleTime < 1.0) { // Between A and B
                               frequency = mix(frequencyA[i], frequencyB[i], interp);
                               amplitude = mix(amplitudeA[i], amplitudeB[i], interp);
        } else if (cycleTime < 2.0) { // Between B and C
                                      frequency = mix(frequencyB[i], frequencyC[i], interp);
                                      amplitude = mix(amplitudeB[i], amplitudeC[i], interp);
        } else if (cycleTime < 3.0) { // Between C and D
                                      frequency = mix(frequencyC[i], frequencyD[i], interp);
                                      amplitude = mix(amplitudeC[i], amplitudeD[i], interp);
        } else { // Between D and A
                 frequency = mix(frequencyD[i], frequencyA[i], interp);
                 amplitude = mix(amplitudeD[i], amplitudeA[i], interp);
        }

        // Apply the scaling and sum up the contributions
        spectrum += amplitude * cos(x * frequency) * centerScale * 0.5 + centerScale * 0.2;
    }

    // Normalize and return the result in [0.0, 1.0] without clamping
    return spectrum;
}



vec4 drawBackground(vec2 uv) {

    vec4 fadePlaneTop = vec4(178.0, 0.0, 131.0, 255.0) / 255.0;
    vec4 fadePlaneBottom = vec4(27.0, 1.0, 63.0, 255.0) / 255.0;
    vec4 fadeBackgroundBottom = vec4(103.0, 3.0, 158.0, 255.0) / 255.0;
    vec4 fadeBackgroundTop = vec4(12.0, 2.0, 58.0, 255.0) / 255.0;

    float split = 0.1;

    return mix(
        mix(fadeBackgroundTop, fadeBackgroundBottom, (uv.y + 1) / (1 + split)),
        mix(fadePlaneTop, fadePlaneBottom, (uv.y - (split)) / (1 - split)),
        step(split, uv.y)
    );
}

// Function to draw a sun centered at (0.5, 0.333) with radius 0.2
vec4 drawSun(vec2 uv) {
    // Sun parameters
    vec2 sunCenter = - vec2(0, .4);
    float sunRadius = 0.4;

    // Calculate distance from the current fragment to the sun's center
    float dist = distance(uv, sunCenter);

    // Color inside the sun (yellowish), and outside the sun (sky color)
    vec4 sunColorTop = vec4(215, 0, 125, 255) / 255; // Soft yellow for the sun
    vec4 sunColorBottom = vec4(248, 253, 86, 255) / 255; // Soft yellow for the sun
    vec4 backgroundColor = vec4(0.0, 0.0, 0.0, 0.0); // Light blue for the sky


    vec2 pixels = boundingBox * fragTexCoord - vec2(1, 1);
    // If distance is less than the radius, we are inside the sun; otherwise, we are outside
    float heightPercentage = abs(uv.y - (sunCenter.y - sunRadius)) / (sunRadius * 2);
    int gapHeight = int( 20 * (1 - step(heightPercentage, 0.4)) + 10 * (1 - step(heightPercentage, 0.7)) + 20 * (1 - step(heightPercentage, 0.9)));
    return mix(
        backgroundColor,
        mix(sunColorTop, sunColorBottom, heightPercentage),
        (1 - step(sunRadius, dist)) * ( 1- step(int(pixels.y) % gapHeight, gapHeight / 2))
    );
}


void main()
{
    float res = boundingBox.x / boundingBox.y;
    vec2 pixels = boundingBox * fragTexCoord - vec2(1, 1);
    vec2 uv = (fragTexCoord - vec2(0.5, 0.5)) * vec2(2 * res, 2);
    float spec = frequencySpectrum(uv.x, time);
    finalColor = max(drawBackground(uv), drawSun(uv));
    if (uv.y < .1 && uv.y > -spec * 0.3) {
        finalColor = vec4(31, 1, 71, 255) / 255;

    }
}


