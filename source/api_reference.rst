DirectX Code Generation API Reference
=====================================

This document provides an overview of the DirectX code generation functionality in CrossGL, specifically focusing on the `HLSLCodeGen` class. This class is responsible for converting the abstract syntax tree (AST) of CrossGL shaders into HLSL code.

.. raw:: html

   <div class="large-text">HLSLCodeGen</div>

HLSLCodeGen is responsible for generating HLSL code from the AST nodes.

.. raw:: html

   <div class="large-text">Attributes</div>

- **current_shader** (`ShaderNode`) – The current shader node being processed.

.. raw:: html

   <div class="large-text">Methods</div>

``__init__(self)``
    Initializes the code generator.

``generate(self, ast)``
    Generates HLSL code from the AST.

    - **Parameters**:
      - `ast` (`ShaderNode`) – The abstract syntax tree of the shader.
    - **Returns**: `str` – The generated HLSL code.

``generate_shader(self, node)``
    Generates the HLSL code for the shader.

    - **Parameters**:
      - `node` (`ShaderNode`) – The shader node of the AST.
    - **Returns**: `str` – The generated HLSL code.

``generate_function(self, node)``
    Generates the HLSL code for a function.

    - **Parameters**:
      - `node` (`FunctionNode`) – The function node of the AST.
    - **Returns**: `str` – The generated HLSL code.

``generate_statement(self, stmt, indent=0, is_vs_input=False)``
    Generates the HLSL code for a statement.

    - **Parameters**:
      - `stmt` (`ASTNode`) – The statement node of the AST.
      - `indent` (`int`) – The indentation level.
      - `is_vs_input` (`bool`) – Whether the statement is in the vertex shader input.
    - **Returns**: `str` – The generated HLSL code.

``generate_assignment(self, node, is_vs_input=False)``
    Generates the HLSL code for an assignment statement.

    - **Parameters**:
      - `node` (`AssignmentNode`) – The assignment node of the AST.
      - `is_vs_input` (`bool`) – Whether the assignment is in the vertex shader input.
    - **Returns**: `str` – The generated HLSL code.

``generate_if(self, node, indent, is_vs_input=False)``
    Generates the HLSL code for an if statement.

    - **Parameters**:
      - `node` (`IfNode`) – The if statement node of the AST.
      - `indent` (`int`) – The indentation level.
      - `is_vs_input` (`bool`) – Whether the if statement is in the vertex shader input.
    - **Returns**: `str` – The generated HLSL code.

``generate_for(self, node, indent, is_vs_input=False)``
    Generates the HLSL code for a for loop statement.

    - **Parameters**:
      - `node` (`ForNode`) – The for loop node of the AST.
      - `indent` (`int`) – The indentation level.
      - `is_vs_input` (`bool`) – Whether the for loop is in the vertex shader input.
    - **Returns**: `str` – The generated HLSL code.

``generate_expression(self, expr, is_vs_input=False)``
    Generates the HLSL code for an expression.

    - **Parameters**:
      - `expr` (`ASTNode`) – The expression node of the AST.
      - `is_vs_input` (`bool`) – Whether the expression is in the vertex shader input.
    - **Returns**: `str` – The generated HLSL code.

``translate_expression(self, expr, is_vs_input)``
    Translates an expression from CrossGL syntax to HLSL syntax.

    - **Parameters**:
      - `expr` (`str`) – The expression in CrossGL syntax.
      - `is_vs_input` (`bool`) – Whether the expression is in the vertex shader input.
    - **Returns**: `str` – The translated expression.

``map_type(self, vtype)``
    Maps CrossGL types to HLSL types.

    - **Parameters**: `vtype` (`str`) – The CrossGL type.
    - **Returns**: `str` – The corresponding HLSL type.

``map_operator(self, op)``
    Maps CrossGL operators to HLSL operators.

    - **Parameters**: `op` (`str`) – The CrossGL operator.
    - **Returns**: `str` – The corresponding HLSL operator.


.. raw:: html

   <div class="large-text">Example</div>

Here's an example usage of the `HLSLCodeGen` class to generate HLSL code from a CrossGL shader:

.. code-block:: python

    from compiler.lexer import Lexer
    from compiler.parser import Parser

    code = """
    shader main {
        input vec3 position;
        input vec2 texCoord;
        input mat2 depth;
        output vec4 fragColor;
        output float depth;
        vec3 customFunction(vec3 random, float factor) {
            return random * factor;
        }

        void main() {
            vec3 color = vec3(position.x,position.y, 0.0);
            float factor = 1.0;

            if (texCoord.x > 0.5) {
                color = vec3(1.0, 0.0, 0.0);
            } else {
                color = vec3(0.0, 1.0, 0.0);
            }

            for (int i = 0; i < 3; i = i + 1) {
                factor = factor * 0.5;
                color = customFunction(color, factor);
            }

            if (length(color) > 1.0) {
                color = normalize(color);
            }

            fragColor = vec4(color, 1.0);
        }
    }
    """
    lexer = Lexer(code)
    parser = Parser(lexer.tokens)
    ast = parser.parse()

    codegen = HLSLCodeGen()
    hlsl_code = codegen.generate(ast)
    print(hlsl_code)


.. raw:: html

   <div class="large-text">Returns</div>

``str`` – The generated HLSL code as a string.
