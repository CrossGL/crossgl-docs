# CrossGL Language

CrossGL is a unified, cross-platform shader language that simplifies
graphics development across APIs like Vulkan, DirectX, and Metal. It
allows developers to write once and compile to native shader languages,
ensuring optimal performance and compatibility 🚀.

```{=html}
<div class="large-text">Syntax Overview</div>
```
The syntax of CrossGL is designed to be intuitive and similar to
Shadertoy, making it easy for developers familiar with Shadertoy to
adapt. Below is an overview of the basic syntax and features.

```{=html}
<div class="large-text">Basic Structure</div>
```
A typical CrossGL shader consists of input, output, and the main
function.

``` python
shader main {
    input vec3 position;
    output vec4 color;

    void vertex main() {
        gl_Position = vec4(position, 1.0);
    }

    void fragment main() {
        color = vec4(position, 1.0);
    }
}
```

```{=html}
<div class="large-text">Data Types</div>
```
CrossGL supports various data types similar to other shader languages.
Below is a mapping of some common types:

  CrossGL              GLSL                 HLSL                     Metal
  -------------------- -------------------- ------------------------ ------------------------
  [vec2]{.title-ref}   [vec2]{.title-ref}   [float2]{.title-ref}     [float2]{.title-ref}
  [vec3]{.title-ref}   [vec3]{.title-ref}   [float3]{.title-ref}     [float3]{.title-ref}
  [vec4]{.title-ref}   [vec4]{.title-ref}   [float4]{.title-ref}     [float4]{.title-ref}
  [mat4]{.title-ref}   [mat4]{.title-ref}   [float4x4]{.title-ref}   [float4x4]{.title-ref}

```{=html}
<div class="large-text">Functions and Operations</div>
```
CrossGL provides built-in functions and operations for vector and matrix
manipulation, similar to other shader languages.

``` python
float3 customFunction(float3 random, float factor) {
    return random * factor;
}

void main() {
    float3 color = vec3(0.0, 0.0, 0.0);
    float factor = 1.0;

    if (texCoord.x > 0.5) {
        color = vec3(1.0, 0.0, 0.0);
    } else {
        color = vec3(0.0, 1.0, 0.0);
    }

    for (int i = 0; i < 3; i++) {
        factor = factor * 0.5;
        color = customFunction(color, factor);
    }

    if (length(color) > 1.0) {
        color = normalize(color);
    }

    fragColor = vec4(color, 1.0);
}
```
