# CrossTL

CrossTL is a universal shader translation language and toolchain. Write shaders once in CrossGL's unified language and compile to HLSL, Metal, GLSL, and more. It also supports bidirectional translation between platform-specific shader languages.

## Installation

```bash
pip install crosstl
```

## Core Features

- **Streamlined Shader Conversion** — Translates shaders directly into target languages or IR, bypassing unnecessary steps.
- **Consistent Multi-Platform Support** — A unified AST supports multiple graphics APIs, so you write once and deploy everywhere.
- **Tailored Code Optimization** — Generated code is optimized per target backend for peak performance.

## Translator Pipeline

The translator processes CrossGL shader code through five stages:

1. **Lexical Analysis (Lexer)** — Tokenizes the input shader code into keywords, operators, identifiers, and literals.
2. **Syntax Analysis (Parser)** — Parses tokens into an Abstract Syntax Tree (AST) representing the shader's structure.
3. **AST Construction** — Builds a tree of nodes (functions, variables, operations) with type and relationship information.
4. **Optimization** — Applies constant folding, dead code elimination, loop unrolling, and expression simplification.
5. **Code Generation** — Traverses the optimized AST and emits platform-specific shader code (HLSL, Metal, GLSL).

## Bidirectional Translation

CrossGL supports two-way conversion. You can convert CrossGL to HLSL/Metal/GLSL and also convert existing platform-specific shaders back into CrossGL. This lets you:

- Standardize shaders across platforms into a single maintainable format
- Re-translate from CrossGL to any supported backend with per-platform optimizations

## Example

A typical CrossGL shader has input, output, and a main function:

**`shader.cgl`**

```python
shader main
{
    vertex
    {
        input vec3 position;
        output vec4 color;

        void main()
        {
            color = vec4(position, 1.0);
        }
    }

    fragment {
        input vec4 color;
        output vec4 fragColor;

        void main()
        {
            fragColor = color;
        }
    }
}
```

**Translate to a backend:**

```python
import crosstl

metal_code = crosstl.translate('shader.cgl', backend='metal')
hlsl_code = crosstl.translate('shader.cgl', backend='directx')
opengl_code = crosstl.translate('shader.cgl', backend='opengl')
```

### HLSL to CrossGL

```hlsl
struct VS_INPUT {
float3 position : POSITION;
};

struct PS_INPUT {
float4 position : SV_POSITION;
float2 uv : TEXCOORD0;
};

PS_INPUT VSMain(VS_INPUT input) {
PS_INPUT output;
output.position = float4(input.position, 1.0);
output.uv = input.position.xy * 10.0;
return output;
}

float4 PSMain(PS_INPUT input) : SV_TARGET {
return float4(input.uv, 0.0, 1.0);
}
```

```python
import crosstl
crossgl_code = crosstl.translate('shader.hlsl', backend='cgl')
```

### Metal to CrossGL

```python
#include <metal_stdlib>
using namespace metal;

struct VertexInput {
    float3 position [[attribute(0)]];
};

struct VertexOutput {
    float4 position [[position]];
    float2 uv;
};

vertex VertexOutput vertexShader(VertexInput in [[stage_in]]) {
    VertexOutput out;
    out.position = float4(in.position, 1.0);
    out.uv = in.position.xy * 10.0;
    return out;
}

fragment float4 fragmentShader(VertexOutput in [[stage_in]]) {
    return float4(in.uv, 0.0, 1.0);
}
```

```python
import crosstl
crossgl_code = crosstl.translate('shader.metal', backend='cgl')
```

### CrossGL to HLSL

```python
import crosstl
hlsl_code = crosstl.translate('shader.cgl', backend='hlsl')
```

### CrossGL to Metal

```python
import crosstl
metal_code = crosstl.translate('shader.cgl', backend='metal')
```

## Supported Platforms

| Platform | Description |
|---|---|
| **DirectX (HLSL)** | Windows graphics and multimedia |
| **Metal (MSL)** | macOS and iOS, low-overhead GPU access |
| **OpenGL (GLSL)** | Cross-platform (Windows, macOS, Linux) |
