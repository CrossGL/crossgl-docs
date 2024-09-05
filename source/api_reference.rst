.. role:: raw-latex(raw)
   :format: latex
..

API References For CrossGL To DirectX , Metal And OpenGL
----------------------------------------------------------------

DirectX Code Generation
-----------------------

The `HLSLCodeGen` class within the CrossGL framework is pivotal in
translating CrossGL shader abstract syntax trees (AST) into HLSL
(High-Level Shader Language) code, which is essential for DirectX
applications. This class systematically converts the AST (representing
the logical structure of a shader) into corresponding HLSL code that
can be executed in DirectX environments.


* Attributes 
   - current_shader (ShaderNode) : The current shader node being processed.

Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **__init__(self) :**
      
   Initializes the code generator.

---

- **generate(self, ast)**  
   Generates HLSL code from the AST.  
   
   - **Parameters:**  
      - `ast (ShaderNode)` – The abstract syntax tree of the shader.
   
   - **Returns:**  
      - `str` – The generated HLSL code.

---

- **generate_shader(self, node)**  
   Generates the HLSL code for the shader.  
   
   - **Parameters:**  
      - `node (ShaderNode)` – The shader node of the AST.
   
   - **Returns:**  
      - `str` – The generated HLSL code.

---

**check_gl_position(self, node)**  
   Checks if the `gl_Position` output is assigned within the vertex shader.

   - **Parameters:**  
      - `node (ASTNode)` – The current node being processed in the AST.
   
   - **Returns:**  
      - `None`

---

**generate_intermidiate(self, node, shader_type)**  
   Generates intermediate shader code by processing a sequence of statements.

   - **Parameters:**  
      - `node (list[ASTNode])` – A list of AST nodes representing the statements to be processed.  
      - `shader_type (str)` – The type of shader (e.g., vertex, fragment) for which the code is being generated.
   
   - **Returns:**  
      - `str` – The generated intermediate shader code as a string.

---

**generate_main(self, node, shader_type)**  
   Generates the main function code for a shader, tailored to the specified shader type.

   - **Parameters:**  
      - `node (FunctionNode)` – The function node of the AST containing the body of the main function.  
      - `shader_type (str)` – The type of shader (e.g., "vertex" or "fragment") for which the main function code is being generated.
   
   - **Returns:**  
      - `str` – The generated main function code as a string.

---

**generate_function(self, node)**  
   Generates the HLSL code for a function.

   - **Parameters:**  
      - `node (FunctionNode)` – The function node of the AST.
   
   - **Returns:**  
      - `str` – The generated HLSL code.

---

**generate_statement(self, stmt, indent=0, is_vs_input=False)**  
   Generates the HLSL code for a statement.

   - **Parameters:**  
      - `stmt (ASTNode)` – The statement node of the AST.  
      - `indent (int)` – The indentation level.  
      - `is_vs_input (bool)` – Whether the statement is in the vertex shader input.
   
   - **Returns:**  
      - `str` – The generated HLSL code.

---

**generate_assignment(self, node, is_vs_input=False)**  
   Generates the HLSL code for an assignment statement.

   - **Parameters:**  
      - `node (AssignmentNode)` – The assignment node of the AST.  
      - `is_vs_input (bool)` – Whether the assignment is in the vertex shader input.
   
   - **Returns:**  
      - `str` – The generated HLSL code.

---

**generate_if(self, node, indent, is_vs_input=False)**  
   Generates the HLSL code for an if statement.

   - **Parameters:**  
      - `node (IfNode)` – The if statement node of the AST.  
      - `indent (int)` – The indentation level.  
      - `is_vs_input (bool)` – Whether the if statement is in the vertex shader input.
   
   - **Returns:**  
      - `str` – The generated HLSL code.

---

**generate_for(self, node, indent, is_vs_input=False)**  
   Generates the HLSL code for a for loop statement.

   - **Parameters:**  
      - `node (ForNode)` – The for loop node of the AST.  
      - `indent (int)` – The indentation level.  
      - `is_vs_input (bool)` – Whether the for loop is in the vertex shader input.
   
   - **Returns:**  
     - `str` – The generated HLSL code.

---

**generate_expression(self, expr, is_vs_input=False)**  
   Generates the HLSL code for an expression.

   - **Parameters:**  
      - `expr (ASTNode)` – The expression node of the AST.  
      - `is_vs_input (bool)` – Whether the expression is in the vertex shader input.
   
   - **Returns:**  
     - `str` – The generated HLSL code.

---

**translate_expression(self, expr, is_vs_input)**  
   Translates an expression from CrossGL syntax to HLSL syntax.

   - **Parameters:**  
      - `expr (str)` – The expression in CrossGL syntax.  
      - `is_vs_input (bool)` – Whether the expression is in the vertex shader input.
   
   - **Returns:**  
     - `str` – The translated expression.

---

**map_type(self, vtype)**  
   Maps CrossGL types to HLSL types.

   - **Parameters:**  
     - `vtype (str)` – The CrossGL type.
   
   - **Returns:**  
     - `str` – The corresponding HLSL type.

---

**map_operator(self, op)**  
   Maps CrossGL operators to HLSL operators.

   - **Parameters:**  
     - `op (str)` – The CrossGL operator.
   
   - **Returns:**  
     - `str` – The corresponding HLSL operator.

---

Example

Here’s an example usage of the HLSLCodeGen class to generate HLSL code
from a CrossGL shader:

.. code:: python

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

Metal Codegen
-------------

The MetalCodeGen class in the CrossGL framework plays a crucial role in
converting the abstract syntax tree (AST) of CrossGL shaders into Metal
shading language (MSL) code, optimized for Apple’s Metal API. This class
ensures that CrossGL shaders are efficiently translated into MSL,
enabling their execution on Apple platforms, including macOS, iOS, and
iPadOS.

* Attributes 
   - current_shader (ShaderNode) : The current shader node being processed.

Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**__init__(self)**  
   Initializes the code generator.

---

**generate(self, ast)**  
   Generates the complete shader code from the given abstract syntax tree (AST).

   - **Parameters:**  
     - `ast (ASTNode)` – The root node of the AST, typically a ShaderNode, representing the entire shader.
   
   - **Returns:**  
     - `str` – The generated shader code as a string, or an empty string if the AST is not a ShaderNode.

---

**generate_shader(self, node)**  
   Generates the complete Metal shading language (MSL) code for a shader from its abstract syntax tree (AST).

   - **Parameters:**  
     - `node (ShaderNode)` – The root node of the AST representing the entire shader, including its global inputs, outputs, and shader stages (vertex and fragment).
   
   - **Returns:**  
     - `str` – The generated MSL code as a string.

---

**check_gl_position(self, node)**  
   Generates intermediate shader code by processing a sequence of statements.

   - **Parameters:**  
      - `node (list[ASTNode])` – A list of AST nodes representing the statements to be processed.
      - `shader_type (str)` – The type of shader (e.g., vertex, fragment) for which the code is being generated.
   
   - **Returns:**  
     - `str` – The generated intermediate shader code as a string.

---

**generate_intermidiate(self, node, shader_type)**  
   Generates intermediate shader code by processing a sequence of statements.

   - **Parameters:**  
      - `node (list[ASTNode])` – A list of AST nodes representing the statements to be processed.
      - `shader_type (str)` – The type of shader (e.g., vertex, fragment) for which the code is being generated.
   
   - **Returns:**  
     - `str` – The generated intermediate shader code as a string.

---

**generate_function(self, node, shader_type)**  
   Generates shader function code based on the function nodes and shader type.

   - **Parameters:**  
      - `node (list[FunctionNode] | FunctionNode)` – A list of function nodes or a single function node, depending on the shader type.
      - `shader_type (str)` – The type of shader (e.g., “vertex”, “fragment”, “global”) for which the function code is being generated.
   
   - **Returns:**  
     - `str` – The generated shader function code as a string.

---

**generate_main(self, node, shader_type)**  
   Generates the main function code for the specified shader type.

   - **Parameters:**  
      - `node (FunctionNode)` – The function node representing the main function in the shader’s AST.
      - `shader_type (str)` – The type of shader (“vertex” or “fragment”) for which the main function code is being generated.
   
   - **Returns:**  
     - `str` – The generated main function code as a string.

---

**generate_statement(self, stmt, indent=0, shader_type=None)**  
   Generates code for a given statement, with support for different statement types and optional indentation.

   - **Parameters:**  
      - `stmt (ASTNode)` – The statement node to be converted to code.
      - `indent (int, optional)` – The indentation level for the generated code. Defaults to 0.
      - `shader_type (str, optional)` – The type of shader (e.g., vertex, fragment), used for context-specific code generation.
   
   - **Returns:**  
     - `str` – The generated code for the statement as a string.

---

**generate_assignment(self, node, shader_type=None)**  
   Generates the code for an assignment statement.

   - **Parameters:**  
      - `node (AssignmentNode)` – The assignment node containing the variable name and the value to be assigned.
      - `shader_type (str, optional)` – The type of shader (e.g., vertex, fragment), which influences how the assignment is generated.
   
   - **Returns:**  
     - `str` – The generated assignment code as a string.

---

**generate_if(self, node, indent, shader_type=None)**  
   Generates code for an if statement, including optional else body.

   - **Parameters:**  
      - `node (IfNode)` – The IfNode containing the condition, if body statements, and optionally else body statements.
      - `indent (int)` – The indentation level for the generated code.
      - `shader_type (str, optional)` – The type of shader (e.g., vertex, fragment), used for context-specific code generation.
   
   - **Returns:**  
     - `str` – The generated if statement code as a string.

---

**generate_for(self, node, indent, shader_type=None)**  
   Generates code for a for loop statement.

   - **Parameters:**  
      - `node (ForNode)` – The ForNode containing initialization, condition, update expressions, and the loop body.
      - `indent (int)` – The indentation level for the generated code.
      - `shader_type (str, optional)` – The type of shader (e.g., vertex, fragment), used for context-specific code generation.
   
   - **Returns:**  
     - `str` – The generated for loop code as a string.

---

**generate_expression(self, expr, shader_type=None)**  
   Generates code for an expression, handling various types of expression nodes.

   - **Parameters:**  
      - `expr (ASTNode)` – The expression node to be converted into code.
      - `shader_type (str, optional)` – The type of shader (e.g., vertex, fragment), used for context-specific code generation.
   
   - **Returns:**  
     - `str` – The generated expression code as a string.

---

**translate_expression(self, expr, shader_type)**  
   Translates an expression to its corresponding shader code representation, based on the shader type.

   - **Parameters:**  
      - `expr (str)` – The expression to be translated.
      - `shader_type (str)` – The type of shader (e.g., vertex, fragment), used for context-specific translation.
   
   - **Returns:**  
     - `str` – The translated expression code as a string.

---

**map_type(self, vtype)**  
   Maps a type identifier to its corresponding shader type representation.

   - **Parameters:**  
     - `vtype (str)` – The type identifier to be mapped.
   
   - **Returns:**  
     - `str` – The mapped shader type representation.

---

**map_operator(self, op)**  
   Maps an operator identifier to its corresponding shader code representation.

   - **Parameters:**  
     - `op (str)` – The operator identifier to be mapped.
   
   - **Returns:**  
     - `str` – The mapped shader operator representation.

---

Example

Here’s an example usage of the MetalCodeGen class to generate Metal code
from a CrossGL shader:

.. code:: python

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

   codegen = MetalCodeGen()
   Metal_code = codegen.generate(ast)
   print(Metal_code)

OpenGL Codegen
--------------

The `OpenGLCodeGen` class in the CrossGL framework is essential for
translating the abstract syntax tree (AST) of CrossGL shaders into
OpenGL Shading Language (GLSL) code. This class is responsible for
converting CrossGL shaders into GLSL, ensuring compatibility with OpenGL
implementations across various platforms. By generating optimized GLSL
code, the `OpenGLCodeGen` class enables the efficient execution of
shaders on systems that support OpenGL, including Windows, macOS, and
Linux environments.

* Attributes 
   - current_shader (ShaderNode) : The current shader node being processed.

Methods
~~~~~~~

**__init__(self)**  
   Initializes the code generator.

---

**generate(self, ast)**  
   Generates the shader code from the given abstract syntax tree (AST).

   - **Parameters:**  
     - `ast (ASTNode)` – The abstract syntax tree node representing the shader.
   
   - **Returns:**  
     - `str` – The generated shader code.

---

**generate_shader(self, node)**  
   Generates the shader code from its abstract syntax tree (AST).

   - **Parameters:**  
     - `node (ShaderNode)` – The shader node containing global inputs, outputs, and shader sections.
   
   - **Returns:**  
     - `str` – The generated shader code.

---

**generate_function(self, node, shader_type)**  
   Generates function code for the given function node and shader type.

   - **Parameters:**  
      - `node (FunctionNode)` – The function node containing return type, name, parameters, and body.
      - `shader_type (str)` – The type of shader ("vertex", "fragment", or "global").
   
   - **Returns:**  
     - `str` – The generated function code.

---

**generate_main(self, node, shader_type)**  
   Generates the main function code for the given function node and shader type.

   - **Parameters:**  
      - `node (FunctionNode)` – The function node containing return type, name, parameters, and body.
      - `shader_type (str)` – The type of shader ("vertex" or "fragment").
   
   - **Returns:**  
     - `str` – The generated main function code.

---

**generate_statement(self, stmt, indent=0, shader_type=None)**  
   Generates code for a given statement, handling different types of statements based on their node type.

   - **Parameters:**  
      - `stmt (ASTNode)` – The statement node to generate code for.
      - `indent (int)` – The level of indentation for the statement.
      - `shader_type (str)` – The type of shader ("vertex" or "fragment").
   
   - **Returns:**  
     - `str` – The generated code for the statement.

---

**generate_intermediate(self, node, shader_type)**  
   Generates intermediate code from a list of statements.

   - **Parameters:**  
      - `node (list of ASTNode)` – The list of intermediate statements to generate code for.
      - `shader_type (str)` – The type of shader ("vertex" or "fragment").
   
   - **Returns:**  
     - `str` – The generated intermediate code.

---

**generate_assignment(self, node, shader_type=None)**  
   Generates the code for an assignment statement.

   - **Parameters:**  
      - `node (AssignmentNode)` – The assignment node containing the variable and the value to assign.
      - `shader_type (str)` – The type of shader ("vertex" or "fragment").
   
   - **Returns:**  
     - `str` – The generated assignment code.

---

**generate_if(self, node, indent, shader_type=None)**  
   Generates the code for an `if` statement.

   - **Parameters:**  
      - `node (IfNode)` – The node representing the `if` statement with its condition and bodies.
      - `indent (int)` – The level of indentation for the generated code.
      - `shader_type (str)` – The type of shader ("vertex" or "fragment").
   
   - **Returns:**  
     - `str` – The generated `if` statement code.

---

**generate_for(self, node, indent, shader_type=None)**  
   Generates the code for a `for` loop.

   - **Parameters:**  
      - `node (ForNode)` – The node representing the `for` loop with initialization, condition, update, and body.
      - `indent (int)` – The level of indentation for the generated code.
      - `shader_type (str)` – The type of shader ("vertex" or "fragment").
   
   - **Returns:**  
     - `str` – The generated `for` loop code.

---

**generate_expression(self, expr, shader_type=None)**  
   Generates the code for an expression based on its type.

   - **Parameters:**  
      - `expr (ASTNode)` – The expression node, which could be a string, `VariableNode`, `BinaryOpNode`, `FunctionCallNode`, `UnaryOpNode`, `TernaryOpNode`, or `MemberAccessNode`.
      - `shader_type (str)` – The type of shader ("vertex" or "fragment").
   
   - **Returns:**  
     - `str` – The generated code for the expression.

---

**translate_expression(self, expr, shader_type)**  
   Translates the expression based on its type and shader type.

   - **Parameters:**  
      - `expr (str)` – The expression to translate.
      - `shader_type (str)` – The type of shader ("vertex" or "fragment").
   
   - **Returns:**  
     - `str` – The translated expression, or the original expression if no translation is found.

---

**map_type(self, vtype)**  
   Maps the given type to its corresponding shader type.

   - **Parameters:**  
     - `vtype (str)` – The type to be mapped.
   
   - **Returns:**  
     - `str` – The mapped shader type.

---

**map_operator(self, op)**  
   Maps the given operator to its corresponding shader operator.

   - **Parameters:**  
     - `op (str)` – The operator to be mapped.
   
   - **Returns:**  
     - `str` – The mapped shader operator.

---

Example

Here’s an example usage of the OpenGLCodeGen class to generate OpenGL
code from a CrossGL shader:

.. code:: python

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

   codegen = OpenGLCodeGen()
   opengl_code = codegen.generate(ast)
   print(opengl_code)

Vulkan Codegen
--------------

The `VulkanCodeGen` class in the CrossGL framework is pivotal for
translating the abstract syntax tree (AST) of CrossGL shaders into
SPIR-V compatible code, used by the Vulkan API. This class ensures that
CrossGL shaders are converted into Vulkan Shading Language (GLSL for
Vulkan) or directly into SPIR-V, providing compatibility with
Vulkan-based applications across various platforms. By generating
optimized SPIR-V code, the `VulkanCodeGen` class enables efficient
execution of shaders on systems that support Vulkan, including Windows,
macOS, Linux, and Android environments, ensuring high performance and
flexibility in rendering tasks.

* Attributes 
   - current_shader (ShaderNode) : The current shader node being processed.

Methods
~~~~~~~

**__init__(self)**  
   Initializes the code generator.

---

**generate(self, ast)**  

Generates shader code from the given abstract syntax tree (AST).

- **Parameters:**  
  - `ast (ShaderNode)` – The abstract syntax tree node representing the shader.
  
- **Returns:**  
  - `str` – The generated shader code, or an empty string if the AST is not a `ShaderNode`.

---

**generate_shader(self, node)**  

Generates the SPIR-V code for a Vulkan shader based on the provided shader node.

- **Parameters:**  
  - `node (ShaderNode)` – The node representing the shader, containing inputs, outputs, functions, and other shader components.
  
- **Returns:**  
  - `str` – The generated SPIR-V code, including SPIR-V header information, entry points, decorations, type declarations, global variables, constants, function declarations, and function definitions.

---

**declare_types(self)**  

Declares the necessary data types for the Vulkan SPIR-V shader.

- **Parameters:**  
  - None
  
- **Returns:**  
  - `str` – The SPIR-V code string that includes type declarations for `void`, `boolean`, `float`, `integer`, and `unsigned integer` types. It also dynamically generates vector types based on the shader’s input and output variables, assigning them unique IDs.

---

**declare_global_variables(self)**  

Declares global variables for shader inputs and outputs in the SPIR-V code.

- **Parameters:**  
  - None
  
- **Returns:**  
  - `str` – The SPIR-V code string that declares pointers to the input and output variables. It assigns unique IDs to these variables and stores them in `self.variable_ids`. The function handles both input and output variables, generating the appropriate `OpTypePointer` and `OpVariable` instructions for each.

---

**declare_constants(self)** 

Declares constants used in the shader within the SPIR-V code.

- **Parameters:**  
  - None
  
- **Returns:**  
  - `str` – The SPIR-V code string that defines commonly used constants such as `0` and `1` for both `float` and `int` types, as well as `3` for the `int` type. Each constant is represented with an `OpConstant` instruction, associating the value with a type (`float` or `int`). These constants can then be referenced within the shader code.

---

**declare_function(self, node)**

Declares a function type in SPIR-V code based on the given function node.

- **Parameters:**  
  - `node (FunctionNode)` – The function node representing the function declaration in the shader.
  
- **Returns:**  
  - `str` – The SPIR-V code string that defines the function type. It includes the function’s return type and parameter types, and assigns a unique ID to this function type. The function type is represented with an `OpTypeFunction` instruction, specifying the return type and the types of parameters the function accepts.

---

**generate_function(self, node)**

Generates the SPIR-V code for a function based on the given function node.

- **Parameters:**  
  - `node (FunctionNode)` – The function node representing the function definition in the shader.
  
- **Returns:**  
  - `str` – The SPIR-V code string for the function. This includes the function declaration with its type, parameter declarations, function body, and function end. The function code is defined using `OpFunction`, `OpFunctionParameter`, `OpLabel`, `OpReturn`, `OpUnreachable`, and `OpFunctionEnd` instructions. The function is assigned a unique ID and the function parameters are mapped to SPIR-V function parameters. The body of the function is generated by translating each statement into SPIR-V code.

---

**generate_statement(self, stmt)**  

Generates the SPIR-V code for a given statement node.

- **Parameters:**  
  - `stmt (ASTNode)` – The statement node representing a specific type of statement in the shader code.
  
- **Returns:**
   - `str` – The SPIR-V code string for the statement. The function translates different types of statements into corresponding SPIR-V instructions: 
      - For `AssignmentNode`, it generates code using `OpStore`.
      - For `IfNode`, it generates conditional branches using `OpBranchConditional`.
      - For `ForNode`, it generates code for the initialization, condition, and update steps, and loops through the body.
      - For `ReturnNode`, it generates a return statement with `OpReturnValue` or `OpReturn` if there is no return value.
      - For other statements, it generates SPIR-V code for expressions.

---

**generate_assignment(self, node)** 

Generates the SPIR-V code for an assignment statement.

- **Parameters:**  
  - `node (AssignmentNode)` – The assignment node containing the variable being assigned to and the value being assigned.
  
- **Returns:**  
   - `str` – The SPIR-V code string for the assignment operation. The function handles assignments in two cases:
      - If the variable being assigned to is a shader output, it uses the `OpStore` instruction to store the value directly to the output variable.
      - For other variables, it generates a temporary variable of the function type, assigns the value to it, and then stores the value to the temporary variable. This is useful for intermediate variables within functions.

---

**generate_if(self, node)**  

Generates SPIR-V code for an `if` statement.

- **Parameters:**  
  - `node (IfNode)` – The if-node containing the condition, the body of statements to execute if the condition is true, and optionally the body of statements to execute if the condition is false.

- **Returns:**  
   - `str` – The SPIR-V code string for the `if` statement. The function handles the following :
      - **Condition Evaluation:** Evaluates the condition expression and generates the necessary label IDs for the `then`, `else`, and `merge` blocks.
      - **Branching:** Uses the `OpSelectionMerge` and `OpBranchConditional` instructions to branch to the appropriate labels based on the condition.
      - **Then Block:** Executes the statements within the `if` body, then branches to the merge block.
      - **Else Block:** If there is an `else` body, it executes those statements and then branches to the merge block.
      - **Merge Block:** The merge block that consolidates the control flow from both the `then` and `else` blocks.

---

**generate_for(self, node)**  

Generates SPIR-V code for a `for` loop.

- **Parameters:**  
  - `node (ForNode)` – The for-node containing initialization, condition, update, and body of the loop.

- **Returns:**  
   - `str` – The SPIR-V code string for the `for` loop. The function handles the following :
      - **Initialization:** Executes the initialization statement.
      - **Loop Header:** Creates labels for the loop header, body, continue, and merge blocks.
      - **Loop Merge:** Uses `OpLoopMerge` to define the loop structure, specifying the merge and continue labels.
      - **Condition Check:** Uses `OpBranchConditional` to branch to the loop body if the condition is true or to the merge label if false.
      - **Body Execution:** Executes the statements in the loop body and then branches to the continue label.
      - **Update and Repeat:** Executes the update statement, then branches back to the loop header for the next iteration.
      - **Merge Block:** The merge block that follows the end of the loop, consolidating the control flow.

---

**generate_expression(self, expr)**  

Generates SPIR-V code for the given expression.

- **Parameters:**  
  - `expr (ExpressionNode)` – The expression node to be converted into SPIR-V code. This can be a string, `VariableNode`, `BinaryOpNode`, `FunctionCallNode`, `MemberAccessNode`, or other types of expression nodes.

- **Returns:**  
   - `str` – The SPIR-V code string for the expression. The function handles the following cases :
      - **String:** Translates a simple string expression directly.
      - **VariableNode:** Translates the variable name to its corresponding SPIR-V identifier.
      - **BinaryOpNode:** Generates code for binary operations. This involves:
      - Generating SPIR-V IDs for the left and right operands.
      - Mapping the operator to its SPIR-V representation.
      - Constructing the appropriate SPIR-V instruction using `OpBinaryOp`.
      - **FunctionCallNode:** Handles function calls, including:
      - **Vector Constructors:** For built-in functions like `vec2`, `vec3`, and `vec4`, constructs the vector using `OpCompositeConstruct`.
      - **Regular Function Calls:** Calls functions with `OpFunctionCall`, handling both void and non-void return types.
      - **MemberAccessNode:** Generates code to access a member of a composite type using `OpCompositeExtract`.
      - **Default Case:** Returns the string representation of the expression for any other cases.

---

**translate_expression(self, expr)** 

Translates an expression into SPIR-V code.

- **Parameters:**  
  - `expr (str)` – The expression to be translated. This can be a variable name, a vector constructor, or a constant value.

- **Returns:**  
   - `str` – The SPIR-V code string for the given expression. The function handles the following cases :
      - **Variable Names:** If the expression is a variable name that exists in `self.variable_ids`, it returns the corresponding SPIR-V identifier.
      - **Vector Constructors:** If the expression is a vector constructor (e.g., `vec3(1.0, 2.0, 3.0)`), it translates the components into SPIR-V code using `OpCompositeConstruct`. It splits the vector components, translates each component, and constructs the vector.
      - **Constant Values:** If the expression is a numeric value, it attempts to convert it to a float and generates a constant using `OpConstant` with type `%float`.
      - **Unhandled Expressions:** For any other expressions, it returns a comment indicating that the expression is unhandled.

---

**map_type(self, vtype)**  

Maps a given type to its corresponding SPIR-V type.

- **Parameters:**  
  - `vtype (str)` – The type to be mapped, which may include types like `"void"`, `"bool"`, `"int"`, `"float"`, and various vector and matrix types.

- **Returns:**  
   - `str` – The SPIR-V type corresponding to the input type. The function uses a mapping dictionary to translate common GLSL types to SPIR-V types :   
      - `"void"` -> `"void"`
      - `"bool"` -> `"bool"`
      - `"int"` -> `"int"`
      - `"float"` -> `"float"`
      - `"vec2"` -> `"v2float"`
      - `"vec3"` -> `"v3float"`
      - `"vec4"` -> `"v4float"`
      - `"mat2"` -> `"mat2v2float"`
      - `"mat3"` -> `"mat3v3float"`
      - `"mat4"` -> `"mat4v4float"`

  - If `vtype` is not in the dictionary, it returns `vtype` unchanged. This allows for custom or unsupported types to pass through without modification.

---

**map_operator(self, op)**  

Maps a given operator to its corresponding SPIR-V opcode.

- **Parameters:**  
   - `op (str)` – The operator to be mapped. This might include operators such as `"PLUS"`, `"MINUS"`, `"MULTIPLY"`, `"DIVIDE"`, `"LESS_THAN"`, and so on.

- **Returns:**  
   - `str` – The SPIR-V opcode corresponding to the input operator. The function uses a dictionary to translate common operators to their SPIR-V opcodes:   
      - `"PLUS"` -> `"OpFAdd"`
      - `"MINUS"` -> `"OpFSub"`
      - `"MULTIPLY"` -> `"OpFMul"`
      - `"DIVIDE"` -> `"OpFDiv"`
      - `"LESS_THAN"` -> `"OpFOrdLessThan"`
      - `"GREATER_THAN"` -> `"OpFOrdGreaterThan"`
      - `"LESS_EQUAL"` -> `"OpFOrdLessThanEqual"`
      - `"GREATER_EQUAL"` -> `"OpFOrdGreaterThanEqual"`
      - `"EQUAL"` -> `"OpFOrdEqual"`
      - `"NOT_EQUAL"` -> `"OpFOrdNotEqual"`
      - `"AND"` -> `"OpLogicalAnd"`
      - `"OR"` -> `"OpLogicalOr"`

  - If `op` is not found in the dictionary, it returns `op` unchanged, allowing for unhandled or custom operators to pass through without modification.

---

**get_id(self)** 

Generates a unique identifier for use in the SPIR-V code.

- **Returns:**  
  - `int` – The current value of `self.id_counter`, which serves as a unique identifier in the generated SPIR-V code. After returning the current value, the method increments `self.id_counter` by 1 to ensure that the next call to `get_id` produces a new unique identifier.

AST (Abstract Syntax Tree)
---------------------------

**UniformNode(ASTNode) Class**

Represents a uniform variable in the abstract syntax tree (AST) of
shader code. This node is used to define uniform variables, which are
global variables passed to the shader from the application.

-  **Attributes**:

   -  vtype (str): The type of the uniform variable (e.g., `int`,
      `float`, `vec3`).
   -  name (str): The name of the uniform variable.

-  **Methods**:

   -  __repr__():

      -  **Purpose**: Provides a detailed string representation of the
         `UniformNode` instance for debugging purposes.
      -  **Returns**: A string in the format
         `"UniformNode(vtype=<vtype>, name=<name>)"`.

   -  __str__():

      -  **Purpose**: Provides a string representation of the uniform
         declaration as it would appear in shader code.
      -  **Returns**: A string in the format :

      .. code:: python

         "uniform <vtype> <name>;"

-  **Example**:

   .. code:: python

      uniform_node = UniformNode("vec3", "lightDirection")
      print(uniform_node)  # Output: uniform vec3 lightDirection;
      print(repr(uniform_node))  # Output: UniformNode(vtype=vec3, name=lightDirection)

---

**TernaryOpNode Class**

Represents a ternary operation in the abstract syntax tree (AST) of a
programming language or shader code. A ternary operation is a conditional
expression that evaluates to one of two values depending on the result of
a condition.

- **Attributes**:
   - `condition`: The condition expression to be evaluated. This is typically a boolean expression.
   - `true_expr`: The expression that is evaluated and returned if the condition is `True`.
   - `false_expr`: The expression that is evaluated and returned if the condition is `False`.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `TernaryOpNode` instance for debugging purposes.
      - **Returns**: A string in the format :
      
      .. code:: python

        "TernaryOpNode(condition=<condition>, true_expr=<true_expr>, false_expr=<false_expr>)"

- **Example**:
   .. code:: python

      ternary_node = TernaryOpNode("x > 0", "x", "-x")
      print(repr(ternary_node))  
      # Output: TernaryOpNode(condition=x > 0, true_expr=x, false_expr=-x)

**ShaderNode Class**

Represents a complete shader program in the abstract syntax tree (AST).
This node encapsulates all the components of a shader, including inputs,
outputs, functions, and the vertex and fragment shader sections.

- **Attributes**:
   - `name`: The name of the shader program.
   - `global_inputs`: A list of global input variables used in the shader.
   - `global_outputs`: A list of global output variables produced by the shader.
   - `global_functions`: A list of global functions defined in the shader.
   - `vertex_section`: The vertex shader section, containing operations related to vertex processing.
   - `fragment_section`: The fragment shader section, containing operations related to fragment (pixel) processing.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `ShaderNode` instance for debugging purposes.
      - **Returns**: A string in the format:

      .. code:: python

        "ShaderNode(<name>) <global_inputs> <global_outputs> <global_functions> <vertex_section> <fragment_section>"

- **Example**:

   .. code:: python

      shader_node = ShaderNode(
          name="BasicShader",
          global_inputs=["position", "normal"],
          global_outputs=["color"],
          global_functions=["transform", "lighting"],
          vertex_section="vertex operations here",
          fragment_section="fragment operations here",
      )
      print(repr(shader_node))  
      # Output: ShaderNode('BasicShader') ['position', 'normal'] ['color'] ['transform', 'lighting'] 'vertex operations here' 'fragment operations here'

**VERTEXShaderNode Class**

Represents the vertex shader section of a shader program in the abstract
syntax tree (AST). This node encapsulates the inputs, outputs, functions,
and intermediate operations specific to the vertex shader.

- **Attributes**:
   - `inputs`: A list of input variables used by the vertex shader, typically including attributes like position, normal, etc.
   - `outputs`: A list of output variables produced by the vertex shader, such as transformed positions or interpolated data.
   - `functions`: A list of functions defined and used within the vertex shader.
   - `intermidiate`: The intermediate operations or calculations performed within the vertex shader before the final output.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `VERTEXShaderNode` instance for debugging purposes.
      - **Returns**: A string in the format:

      .. code:: python

        "VERTEXShaderNode(<inputs>) <outputs> <functions> <intermidiate>"

- **Example**:

   .. code:: python

      vertex_shader_node = VERTEXShaderNode(
          inputs=["position", "normal"],
          outputs=["gl_Position"],
          functions=["transform", "calculateNormal"],
          intermidiate="intermediate calculations here",
      )
      print(repr(vertex_shader_node))  
      # Output: VERTEXShaderNode(['position', 'normal']) ['gl_Position'] ['transform', 'calculateNormal'] 'intermediate calculations here'

---

**FRAGMENTShaderNode Class**

Represents the fragment shader section of a shader program in the
abstract syntax tree (AST). This node encapsulates the inputs, outputs,
functions, and intermediate operations specific to the fragment shader.

-  **Attributes**:

   -  `inputs`: A list of input variables used by the fragment shader, such as interpolated data from the vertex shader.
   -  `outputs`: A list of output variables produced by the fragment shader, like the final color of the pixel.
   -  `functions`: A list of functions defined and used within the fragment shader.
   -  `intermidiate`: The intermediate operations or calculations performed within the fragment shader before producing the final output.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `FRAGMENTShaderNode` instance for debugging purposes.
      - **Returns**: A string in the format :

      .. code:: python

        "FRAGMENTShaderNode(<inputs>) <outputs> <functions> <intermidiate>"

-  **Example**:

   .. code:: python

      fragment_shader_node = FRAGMENTShaderNode(
          inputs=["fragCoord", "color"],
          outputs=["fragColor"],
          functions=["applyLighting", "computeColor"],
          intermidiate="intermediate calculations here",
      )
      print(repr(fragment_shader_node))
      # Output: FRAGMENTShaderNode(['fragCoord', 'color']) ['fragColor'] ['applyLighting', 'computeColor'] 'intermediate calculations here'

**FunctionNode Class**

The `FunctionNode` class represents a function within the abstract syntax
tree (AST) for shader code. It contains details about the function’s
return type, name, parameters, and body. This class is used in shader
code generation to define functions that can be called within shaders.

- **Attributes**:
   -  `return_type`: The data type that the function returns. It is a string representing the type (e.g., `"float"`, `"vec4"`).
   -  `name`: The name of the function as a string.
   -  `params`: A list of tuples where each tuple represents a parameter with its type and name (e.g.,`[("float", "param1"), ("vec3", "param2")]`).
   -  `body`: A list of statements that constitute the function’s body. Each statement can be an instance of various AST node classes, such as `AssignmentNode`, `ReturnNode`, etc.

- **Methods**:
   -  `__repr__()`:
      -  **Purpose**: Provides a detailed string representation of the `FunctionNode` instance. This is useful for debugging and logging.
      -  **Returns**: A string that includes the function’s return type, name, parameters, and body in a format similar to:

      .. code:: python

         "FunctionNode(return_type=<return_type>, name=<name>, params=<params>, body=<body>)"

- **Example Usage:**

   .. code:: python

      # Define a function node
      function_node = FunctionNode(
          return_type="float",
          name="calculateLighting",
          params=[("vec3", "position"), ("vec3", "normal")],
          body=[
              AssignmentNode(name="result", value=BinaryOpNode(left="position", op="MULTIPLY", right="normal")),
              ReturnNode(value="result")
          ]
      )

      # Print the representation
      print(repr(function_node))
      # Output: FunctionNode(return_type=float, name=calculateLighting, params=[('vec3', 'position'), ('vec3', 'normal')], body=[AssignmentNode(name=result, value=BinaryOpNode(left=position, op=MULTIPLY, right=normal)), ReturnNode(value=result)])

**VariableNode Class**

The `VariableNode` class represents a variable within the abstract
syntax tree (AST) for shader code. It contains details about the
variable’s type and name. This class is used when defining variables in
shader code and is a fundamental part of shader code generation.

- **Attributes**:
   -  `vtype`: The data type of the variable, represented as a string
      (e.g., `"float"`, `"vec3"`).
   -  `name`: The name of the variable as a string (e.g., `"position"`,
      `"color"`).

- **Methods**:
   -  `__repr__()`:
      -  **Purpose**: Provides a detailed string representation of the `VariableNode` instance. This is useful for debugging and logging.

      -  **Returns**: A string that includes the variable’s type and name in a format similar to:

      .. code:: python

         "VariableNode(vtype=<vtype>, name=<name>)"

- **Example Usage:**

   .. code:: python

      # Define a variable node
      variable_node = VariableNode(vtype="vec3", name="position")

      # Print the representation
      print(repr(variable_node))
      # Output: VariableNode(vtype=vec3, name=position)

**AssignmentNode Class**

The `AssignmentNode` class represents an assignment operation within
the abstract syntax tree (AST) for shader code. It captures the
assignment of a value to a variable, which is a fundamental operation in
shaders and other programming languages.

- **Attributes**:
   -  `name`: The name of the variable being assigned a value. This is
      typically a string representing the variable’s identifier (e.g.,
      `"color"`, `"position"`).
   -  `value`: The value being assigned to the variable. This can be a
      more complex expression or value, represented as an instance of
      another node class or a string.

- **Methods**:
   -  `__repr__()`:
      -  **Purpose**: Provides a detailed string representation of the `AssignmentNode` instance. This method is useful for debugging and visualizing the node’s structure.

      -  **Returns**: A string that includes the variable name and the assigned value, formatted like:

      .. code:: python

         "AssignmentNode(name=<name>, value=<value>)"

- **Example Usage:**

   .. code:: python

      # Define an assignment node
      assignment_node = AssignmentNode(name="color", value="vec4(1.0, 0.0, 0.0, 1.0)")

      # Print the representation
      print(repr(assignment_node))
      # Output: AssignmentNode(name=color, value=vec4(1.0, 0.0, 0.0, 1.0))

**IfNode Class**

The `IfNode` class represents a conditional statement within the
abstract syntax tree (AST) for shader code. It captures the structure of
an `if` statement, including the condition to be evaluated and the
bodies of code to execute based on whether the condition is true or
false.

- **Attributes**:
   -  `condition`: An expression or condition that determines which body
      of code will be executed. This is often an instance of an expression
      node, representing a boolean condition.
   -  `if_body`: A list of statements or nodes that are executed if the
      condition evaluates to true.
   -  `else_body`: An optional list of statements or nodes that are
      executed if the condition evaluates to false. This can be `None` if
      there is no `else` part.

- **Methods**:
   -  `__repr__()`:
      -  **Purpose**: Provides a detailed string representation of the `IfNode` instance. This method is useful for debugging and understanding the structure of the node.

      -  **Returns**: A string that includes the condition, `if_body`, and optionally the `else_body`, formatted like:

      .. code:: python

         "IfNode(condition=<condition>, if_body=<if_body>, else_body=<else_body>)"

- **Example Usage:**

   .. code:: python

      # Define an if-node
      if_node = IfNode(
          condition="x > 0",
          if_body=[
              AssignmentNode(name="result", value="1.0")
          ],
          else_body=[
              AssignmentNode(name="result", value="0.0")
          ]
      )

      # Print the representation
      print(repr(if_node))
      # Output: IfNode(condition=x > 0, if_body=[AssignmentNode(name=result, value=1.0)], else_body=[AssignmentNode(name=result, value=0.0)])

**ForNode Class**

Represents a `for` loop within the abstract syntax tree (AST) for shader code. This node encapsulates the initialization, condition, update, and body of the `for` loop.

- **Attributes**:
   - `init`: The initialization statement or expression executed before the loop starts.
   - `condition`: The expression evaluated before each iteration to determine if the loop should continue.
   - `update`: The expression or statement executed at the end of each loop iteration, typically used to update the loop variable or state.
   - `body`: The list of statements or nodes that make up the body of the loop, executed repeatedly as long as the `condition` is true.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `ForNode` instance for debugging purposes.
      - **Returns**: A string in the format:

      .. code:: python

        "ForNode(init=<init>, condition=<condition>, update=<update>, body=<body>)"

- **Example**:

   .. code:: python

      for_node = ForNode(
          init=AssignmentNode(name="i", value="0"),
          condition="i < 10",
          update=AssignmentNode(name="i", value="i + 1"),
          body=[
              AssignmentNode(name="result", value="result + i")
          ]
      )
      print(repr(for_node))  
      # Output: ForNode(init=AssignmentNode(name=i, value=0), condition=i < 10, update=AssignmentNode(name=i, value=i + 1), body=[AssignmentNode(name=result, value=result + i)])

**ReturnNode Class**

Represents a return statement within the abstract syntax tree (AST) for shader code. This node encapsulates the value to be returned from a function.

- **Attributes**:
   - `value`: The expression or value to be returned from the function.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `ReturnNode` instance for debugging purposes.
      - **Returns**: A string in the format:

      .. code:: python

        "ReturnNode(value=<value>)"

- **Example**:

   .. code:: python

      return_node = ReturnNode(value="result")
      print(repr(return_node))  
      # Output: ReturnNode(value=result)

**FunctionCallNode Class**

Represents a function call within the abstract syntax tree (AST) for shader code. This node captures the function name and its arguments.

- **Attributes**:
   - `name`: The name of the function being called.
   - `args`: A list of arguments passed to the function.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `FunctionCallNode` instance for debugging purposes.
      - **Returns**: A string in the format:

      .. code:: python

        "FunctionCallNode(name=<name>, args=<args>)"

- **Example**:

   .. code:: python

      func_call_node = FunctionCallNode(name="someFunction", args=["arg1", "arg2"])
      print(repr(func_call_node))  
      # Output: FunctionCallNode(name=someFunction, args=['arg1', 'arg2'])

**BinaryOpNode Class**

Represents a binary operation within the abstract syntax tree (AST) for shader code. This node captures the left operand, operator, and right operand of the operation.

- **Attributes**:
   - `left`: The left operand of the binary operation.
   - `op`: The operator used for the binary operation.
   - `right`: The right operand of the binary operation.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `BinaryOpNode` instance for debugging purposes.
      - **Returns**: A string in the format:

      .. code:: python

        "BinaryOpNode(left=<left>, op=<op>, right=<right>)"

- **Example**:

   .. code:: python

      binary_op_node = BinaryOpNode(left="a", op="PLUS", right="b")
      print(repr(binary_op_node))  
      # Output: BinaryOpNode(left=a, op=PLUS, right=b)

**MemberAccessNode Class**

Represents an access operation for a member of an object within the abstract syntax tree (AST) for shader code. This node captures the object and the specific member being accessed.

- **Attributes**:
   - `object`: The object whose member is being accessed.
   - `member`: The specific member of the object being accessed.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `MemberAccessNode` instance for debugging purposes.
      - **Returns**: A string in the format:

      .. code:: python

        "MemberAccessNode(object=<object>, member=<member>)"

- **Example**:

   .. code:: python

      member_access_node = MemberAccessNode(object="myStruct", member="x")
      print(repr(member_access_node))  
      # Output: MemberAccessNode(object=myStruct, member=x)

**UnaryOpNode Class**

Represents a unary operation within the abstract syntax tree (AST) for shader code. This node captures the operator and the single operand of the operation.

- **Attributes**:
   - `op`: The operator for the unary operation.
   - `operand`: The single operand on which the unary operation is applied.

- **Methods**:
   - `__repr__()`:
      - **Purpose**: Provides a detailed string representation of the `UnaryOpNode` instance for debugging purposes.
      - **Returns**: A string in the format:

      .. code:: python

        "UnaryOpNode(op=<op>, operand=<operand>)"

- **Example**:

   .. code:: python

      unary_op_node = UnaryOpNode(op="NEG", operand="x")
      print(repr(unary_op_node))  
      # Output: UnaryOpNode(op=NEG, operand=x)

**Explanation:**

-  `op`: Represents the unary operator. This could be an operation
   such as negation (-), logical NOT (!), or any other unary
   operation.
-  `operand`: Represents the operand on which the unary operation is
   performed. This is typically a variable or an expression.

The `UnaryOpNode` class is essential for representing unary operations
in shader code. It enables the AST to handle and process operations that
involve a single operand, facilitating the interpretation and
transformation of shader code that includes unary operations.

Lexer
-----

The `TOKENS` list defines regular expressions for various tokens used
in shader code. These tokens are used by a lexer to tokenize shader
source code into meaningful components. The `KEYWORDS` dictionary maps
shader language keywords to their corresponding token types.

Here’s a breakdown of the token types and their corresponding regular
expressions:

Token Definitions
~~~~~~~~~~~~~~~~~~~

-  **Comments**

   -  ``COMMENT_SINGLE``: Matches single-line comments starting with
      `//`.
   -  ``COMMENT_MULTI``: Matches multi-line comments enclosed between
      `/*` and `*/`.

-  **Shader Language Keywords**

   -  ``SHADER``: Matches the `shader` keyword.
   -  ``INPUT``: Matches the `input` keyword.
   -  ``OUTPUT``: Matches the `output` keyword.
   -  ``VOID``: Matches the `void` keyword.
   -  ``MAIN``: Matches the `main` keyword.
   -  ``UNIFORM``: Matches the `uniform` keyword.
   -  ``VECTOR``: Matches `vec2`, `vec3`, or `vec4`.
   -  ``MATRIX``: Matches `mat2`, `mat3`, or `mat4`.
   -  ``BOOL``: Matches the `bool` keyword.
   -  ``VERTEX``: Matches the `vertex` keyword.
   -  ``FRAGMENT``: Matches the `fragment` keyword.

-  **Data Types**

   -  ``FLOAT_NUMBER``: Matches floating-point numbers (e.g., `1.0`,
      `0.5`, `3.`).
   -  ``FLOAT``: Matches the `float` keyword.
   -  ``INT``: Matches the `int` keyword.
   -  ``UINT``: Matches the `uint` keyword.
   -  ``DOUBLE``: Matches the `double` keyword.
   -  ``SAMPLER2D``: Matches the `sampler2D` keyword.

-  **Identifiers and Constants**

   -  ``IDENTIFIER``: Matches variable and function names.
   -  ``NUMBER``: Matches integer numbers (e.g., `1`, `42`).

-  **Operators and Punctuation**

   -  ``ASSIGN_SHIFT_RIGHT``: Matches `>>=`.

   -  ``ASSIGN_SHIFT_LEFT``: Matches `<<=`.

   -  ``ASSIGN_ADD``: Matches `+=`.

   -  ``ASSIGN_SUB``: Matches `-=`.

   -  ``ASSIGN_MUL``: Matches `*=`.

   -  ``ASSIGN_DIV``: Matches `/=`.

   -  ``ASSIGN_AND``: Matches `&=`.

   -  ``ASSIGN_OR``: Matches `|=`.

   -  ``ASSIGN_XOR``: Matches `^=`.

   -  ``ASSIGN_MOD``: Matches `%=`.

   -  ``BITWISE_SHIFT_LEFT``: Matches `<<`.

   -  ``BITWISE_SHIFT_RIGHT``: Matches `>>`.

   -  ``LESS_EQUAL``: Matches `<=`.

   -  ``GREATER_EQUAL``: Matches `>=`.

   -  ``GREATER_THAN``: Matches `>`.

   -  ``LESS_THAN``: Matches `<`.

   -  ``INCREMENT``: Matches `++`.

   -  ``DECREMENT``: Matches `--`.

   -  ``EQUAL``: Matches `==`.

   -  ``NOT_EQUAL```: Matches `!=`.

   -  ``LOGICAL_AND``: Matches `&&`.

   -  ``LOGICAL_OR``: Matches `||`.

   -  ``XOR``: Matches `^`.

   -  ``NOT``: Matches `!`.

   -  ``PLUS``: Matches `+`.

   -  ``MINUS``: Matches `-`.

   -  ``MULTIPLY``: Matches `*`.

   -  ``DIVIDE``: Matches `/`.

   -  ``MOD``: Matches `%`.

   -  ``DOT``: Matches `.`.

   -  ``EQUALS``: Matches `=`.

   -  ``QUESTION``: Matches `?`.

   -  ``COLON``: Matches `:`.

-  **Brackets and Delimiters**

   -  ``LBRACE``: Matches `{`.
   -  ``RBRACE``: Matches `}`.
   -  ``LPAREN``: Matches `(`.
   -  ``RPAREN``: Matches `)`.
   -  ``SEMICOLON``: Matches `;`.
   -  ``COMMA``: Matches `,`.

-  **Whitespace and Miscellaneous**

   -  ``WHITESPACE``: Matches any whitespace characters.
   -  ``CONST``: Matches the `const` keyword.
   -  ``BITWISE_AND``: Matches `&`.
   -  ``BITWISE_OR``: Matches `|`.
   -  ``BITWISE_XOR``: Matches `^`.
   -  ``BITWISE_NOT``: Matches `~`.

Keywords Dictionary
~~~~~~~~~~~~~~~~~~~~~

The `KEYWORDS` dictionary maps shader language keywords to their
corresponding token types. This helps in identifying and categorizing
keywords during tokenization.

This setup allows a lexer to parse shader code and generate tokens that
can be used for further processing, such as syntax checking, code
generation, or transformation.

Attributes: - code (str): The input code to tokenize - tokens (list): A
list of tokens generated from the input code

Methods
~~~~~~~

**__init__(self):**

Initializes the code generator.

---

**Tokenize :**

This method is designed to process a string of shader code and convert it into a list of tokens based on predefined regular expressions. Here’s a detailed explanation of what each part of the method does:

1. **Initialization**:

   - `pos = 0`: Initializes the position counter to start from the beginning of the code.

2. **Token Matching Loop**:

   - The `while` loop continues as long as `pos` is less than the length of `self.code`.
   - `match = None`: Initializes the `match` variable to store the result of regex matching.

3. **Regex Matching**:

   - The `for` loop iterates over each token type and its corresponding pattern in the `TOKENS` list.
   - `regex = re.compile(pattern)`: Compiles the regex pattern for the current token type.
   - `match = regex.match(self.code, pos)`: Attempts to match the regex pattern against the code starting at the current position.

4. **Handling Matches**:

   - If a match is found:
      - `text = match.group(0)`: Extracts the matched text.
      - `if token_type == "IDENTIFIER" and text in KEYWORDS`: Checks if the identifier is a keyword and updates the token type accordingly.
      - `if token_type != "WHITESPACE"`: Skips whitespace tokens and does not append them to the list of tokens.
      - `self.tokens.append(token)`: Appends the token (type and text) to the `self.tokens` list.
      - `pos = match.end(0)`: Updates the position counter to the end of the matched text.
      - `break`: Exits the `for` loop to continue with the next position.

5. **Handling Unmatched Characters**:

   - If no match is found (`if not match`):
      - `unmatched_char = self.code[pos]`: Captures the character at the current position.
      - `highlighted_code`: Highlights the illegal character in the code for easier debugging.
      - Raises a `SyntaxError` with a message indicating the illegal character and its position.

6. **End of File Token**:

   - `self.tokens.append(("EOF", None))`: Appends an “EOF” (end of file) token to indicate the end of the token stream.

---

**Key Points:**

- **Efficient Matching**: By using regex patterns and the `re.match` method, the tokenizer efficiently matches different types of tokens.
- **Error Handling**: Properly raises a `SyntaxError` when encountering illegal characters.
- **Token Management**: Handles and stores tokens while skipping unnecessary whitespace and maintaining the position in the code.

This method ensures that the input shader code is tokenized correctly, allowing further processing like parsing or code generation to be performed.

Parser
-------

This parser generates an abstract syntax tree (AST) from a list of
tokens.

Attributes: 
   - tokens (list): A list of tokens generated from the input code

Methods
~~~~~~~

-  **__init__(self) :**
      
   Initializes the code generator.

---

- **skip_comments:**
   - **Description**: This method iterates through the token list and advances the position until the current token is no longer identified as a comment. It handles both single-line and multi-line comments by continuously consuming tokens classified as `COMMENT_SINGLE` or `COMMENT_MULTI`.
   - **Parameters**: None
   - **Returns**: None

---

- **eat :**
   - **Description**: This method checks if the current token matches the specified `token_type`. If it does, the token is consumed, and the position is incremented to the next token. After consuming the token, comments are skipped by calling skip_comments. If the current token does not match the expected token type, a `SyntaxError` is raised.
   - **Parameters**:
      - `token_type` (str): The expected token type.
   - **Returns**: None

---

- **parse_uniforms:**
   - **Description**: This method processes the shader code to identify and extract uniform declarations. It starts by consuming the `"UNIFORM"` token and then reads the uniform’s type and name. The method expects uniform types to be one of `"VECTOR"`, `"FLOAT"`, `"DOUBLE"`, `"UINT"`, `"INT"`, or `"SAMPLER2D"`. After parsing the type and name, it consumes the following `"SEMICOLON"` token. The method returns a list of `UniformNode` objects representing the parsed uniform declarations.
   - **Parameters**: None
   - **Returns**:
      - `list`: A list of `UniformNode` objects.
   - **Raises**:
      - `SyntaxError`: If the current token is not `"UNIFORM"` or if an unexpected token is encountered when parsing the uniform type.

---

- **parse :**
   - **Description**: This method initiates the parsing process for the shader code. It calls the parse_shader method to handle the specifics of shader code parsing and constructs the abstract syntax tree (AST) that represents the structure and components of the shader.
   - **Parameters**: None
   - **Returns**:
      - `ShaderNode`: The root node of the abstract syntax tree (AST) representing the parsed shader code.

---

- **parse_shader:**
   - **Description**: This method processes the shader code to construct a `ShaderNode` object. It starts by consuming the “SHADER” token and then skips any comments. It extracts the shader’s name, then parses global inputs, uniforms, outputs, and sections for vertex and fragment shaders. It also collects global functions. The method continues parsing until it encounters the closing brace of the shader definition and constructs a `ShaderNode` representing the shader’s structure.
   - **Parameters**: None
   - **Returns**:
      - `ShaderNode`: The root node of the abstract syntax tree (AST) representing the parsed shader code.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected token type, indicating a syntax issue in the shader code.

---

- **parse_shader_section:**
   - **Description**: This method processes a specific shader section, either “VERTEX” or “FRAGMENT”, by consuming the section header and opening brace. It then collects and processes inputs, outputs, functions, and intermediate statements until it encounters the closing brace. It constructs and returns a `VERTEXShaderNode` or `FRAGMENTShaderNode` based on the `section_type` parameter.
   - **Parameters**:
      - `section_type` (str): The type of shader section to parse, either “VERTEX” or “FRAGMENT”.
   - **Returns**:
      - `VERTEXShaderNode` or `FRAGMENTShaderNode`: The root node of the AST for the specified shader section.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected token type, indicating a syntax issue in the shader section.

---

- **parse_inputs:**
   - **Description**: This method processes and extracts input declarations from the shader code by consuming the “INPUT” token, followed by the variable type and name. It collects these declarations into a list until it encounters a token that is not an “INPUT”.
   - **Parameters**: None

   - **Returns**:
      - `list`: A list of tuples representing the input declarations, where each tuple contains the type and name of an input.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected input types (VECTOR, FLOAT, DOUBLE, UINT, INT, MATRIX, or SAMPLER2D).

---

- **parse_outputs:**
   - **Description**: This method processes and extracts output declarations from the shader code by consuming the “OUTPUT” token, followed by the variable type and name. It continues to collect these declarations into a list until it encounters a token that is not an “OUTPUT”.
   - **Parameters**: None
   - **Returns**:
      - `list`: A list of tuples representing the output declarations, where each tuple contains the type and name of an output.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected output types (VECTOR, FLOAT, DOUBLE, UINT, INT, MATRIX, or SAMPLER2D).

---

**parse_function**
   - **Description**: This method processes a function declaration by extracting the return type, function name, parameters, and body. It expects either “MAIN” or an “IDENTIFIER” as the function name, then parses the function’s parameters enclosed in parentheses, and finally, parses the function’s body within curly braces.
   - **Parameters**: None
   - **Returns**:
      - `FunctionNode`: A `FunctionNode` object representing the parsed function declaration, including its return type, name, parameters, and body.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected format for a function declaration, such as not finding “MAIN” or an “IDENTIFIER” where expected.

**parse_parameters**
   - **Description**: This method processes function parameters by collecting them into a list. It handles multiple parameters separated by commas and continues parsing until the closing parenthesis is encountered.
   - **Parameters**: None.
   - **Returns**:
      - `list`: A list of function parameters, where each parameter is represented according to the shader language’s syntax.
   - **Raises**:
      - `None`.

**parse_parameter**
   - **Description**: This method extracts the type and name of a function parameter. It processes the parameter type using the `parse_type` method and captures the parameter name from the current token.
   - **Parameters**: None.
   - **Returns**:
      - `tuple`: A tuple containing the parameter type and name.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected type for a parameter.

**parse_type**
   - **Description**: This method identifies and returns the type of a shader variable or function. It handles basic shader types such as `void`, `VECTOR`, `FLOAT`, `DOUBLE`, `UINT`, `INT`, `MATRIX`, `SAMPLER2D`, and user-defined types. The method checks the current token and returns the appropriate type string.
   - **Parameters**: None.
   - **Returns**:
      - `str`: The name of the type.
   - **Raises**:
      - `SyntaxError`: If the current token does not match a valid type declaration.

**parse_body**
   - **Description**: This method processes the statements within a function body, constructing a list of statements by identifying and parsing control structures (`IF`, `FOR`), return statements, and assignments or function calls. It continues parsing until it encounters a closing brace `RBRACE` or end-of-file `EOF`.
   - **Parameters**: None.
   - **Returns**:
      - `list`: A list of statements contained in the function body.
   - **Raises**:
      - `SyntaxError`: If an unexpected token is encountered while parsing the function body.

**parse_if_statement**
   - **Description**: This method processes an `if` statement by extracting the condition, the body of the `if` block, and optionally the `else` block if present. It constructs an `IfNode` object representing the parsed `if` statement, including its condition and the corresponding bodies for the `if` and `else` branches.
   - **Parameters**: None.
   - **Returns**:
      - `IfNode`: An `IfNode` object representing the `if` statement, including the condition and the bodies for both the `if` and `else` blocks.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected structure of an `if` statement.

**peak**
   - **Description**: This method retrieves the token that is `n` positions ahead in the token list without advancing the current position. It allows inspection of future tokens for decision-making during parsing.
   - **Parameters**:
      - `n (int)`: The number of tokens to peek ahead in the token list.
   - **Returns**:
      - `tuple`: The nth token ahead in the token list.
   - **Raises**:
      - `IndexError`: If peeking beyond the end of the token list.

**parse_for_loop**
   - **Description**: This method processes the components of a for loop, including initialization, condition, update, and body. It constructs a `ForNode` object representing the for loop structure.
   - **Parameters**: None
   - **Returns**:
      - `ForNode`: An object representing the parsed for loop, including its initialization, condition, update, and body.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected for loop structure.

**parse_update**
   - **Description**: This method interprets an update statement, handling both increment and decrement operations. It constructs a `VariableNode` object representing the update statement with the appropriate operation.
   - **Parameters**: None
   - **Returns**:
      - `ASTNode`: An object representing the update statement, which could be a `VariableNode` reflecting an increment or decrement operation.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected update statement structure.

**parse_return_statement**
   - **Description**: This method interprets a return statement, capturing the values to be returned. It constructs a `ReturnNode` object that represents the return statement with the appropriate return values.
   - **Parameters**: None
   - **Returns**:
      - `ReturnNode`: An object representing the return statement, containing a list of values to be returned.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected return statement structure.

**parse_assignment_or_function_call**
   - **Description**: This method interprets either an assignment statement or a function call. It handles various types of assignment operations and updates to variables. Additionally, it processes function calls when the identifier is followed by parentheses.
   - **Parameters**:
      - `update_condition` (bool, optional): A flag indicating whether the parsing should handle special update conditions (e.g., increment or decrement operations). Default is `False`.
   - **Returns**:
      - `ASTNode`: An object representing the assignment or function call. This could be an `AssignmentNode`, `FunctionCallNode`, or a modified `VariableNode` if an increment or decrement operation is detected.
   - **Raises**:
      - `SyntaxError`: If the current token does not match any expected patterns for assignments, function calls, or updates.

**parse_variable_declaration**
   - **Description**: This method parses a variable declaration, handling both simple declarations and assignments. It constructs a `VariableNode` or `BinaryOpNode` representing the variable declaration or assignment, including handling for member access and compound assignments.
   - **Returns**:
      - `VariableNode` or `BinaryOpNode`: An object representing the variable declaration or assignment.
   - **Raises**:
      - `SyntaxError`  : If the current token does not match the expected variable declaration or assignment structure.

**parse_assignment**
   - **Description**: This method parses an assignment statement, including various assignment operators. It constructs a `BinaryOpNode` representing the assignment operation, with the variable name and the assigned value.
   - **Attributes**:
      - `name (str)`: The name of the variable being assigned.
   - **Returns**:
      - `BinaryOpNode`: An object representing the assignment statement.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected assignment operator or structure.

**parse_additive**
   - **Description**: This method parses an additive expression, which includes addition and subtraction operations. It constructs a `BinaryOpNode` representing the additive expression, handling multiple operations as needed.
   - **Returns**:
      - `ASTNode`: An object representing the additive expression.
   - **Raises**:
      - `SyntaxError`: Not applicable for this method, as it does not handle syntax errors directly.

**parse_multiplicative**
   - **Description**: This method parses a multiplicative expression, which includes multiplication and division operations. It constructs a `BinaryOpNode` representing the multiplicative expression, handling multiple operations as needed.
   - **Returns**:
      - `ASTNode`: An object representing the multiplicative expression.
   - **Raises**:
      - `SyntaxError`: Not applicable for this method, as it does not handle syntax errors directly.

**parse_unary**
   - **Description**: This method parses a unary expression, including unary plus and minus operations. It constructs a `UnaryOpNode` representing the unary expression or proceeds to parse a primary expression if no unary operators are present.
   - **Returns**:
      - `ASTNode`: An object representing the unary expression.
   - **Raises**:
      - `SyntaxError`: Not applicable for this method, as it does not handle syntax errors directly.

**parse_primary**
   - **Description**: This method parses primary expressions, which include parenthesized expressions, numeric literals, and identifiers. It handles different token types to construct the appropriate AST node or value. If the token is not recognized as a valid primary expression, it raises a `SyntaxError`.
   - **Returns**:
      - `ASTNode`: An object representing the primary expression, which could be a value or a node from a function call or identifier.
   - **Raises**:
      - `SyntaxError`: If the current token does not match a valid primary expression.

**parse_function_call**
   - **Description**: This method interprets a function call by reading the function name and its arguments. It constructs a `FunctionCallNode` object representing the function call with the parsed arguments.
   - **Attributes**:
      - `name (str)`: The name of the function being called.
   - **Returns**:
      - `FunctionCallNode`: An object representing the function call, including the function name and a list of arguments.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected structure for a function call.

**parse_expression**
   - **Description**: This method interprets an expression, handling various operators to construct a `BinaryOpNode` that represents the expression’s structure.
   - **Returns**:
      - `ASTNode`: An object representing the parsed expression, which could be a `BinaryOpNode` reflecting the expression’s operators and operands.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected structure for an expression.

**parse_ternary**
   - **Description**: This method interprets a ternary expression, handling the ternary operator (`? :`) to construct a `TernaryOpNode` that represents the ternary expression’s condition and its two possible outcomes.
   - **Returns**:
      - `ASTNode`: An object representing the parsed ternary expression, which could be a `TernaryOpNode` reflecting the condition and both branches of the ternary operator.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected structure for a ternary expression.

**parse_function_call_or_identifier**
   - **Description**: This method determines whether the current token represents a function call or a simple identifier. It constructs a `FunctionCallNode` if it detects a function call, or a `VariableNode` if it detects an identifier. It also handles member access if a dot (`.`) follows the identifier.
   - **Returns**:
      - `ASTNode`: An object representing either a `FunctionCallNode` for function calls, a `VariableNode` for identifiers, or a member access node if applicable.
   - **Raises**:
      - `SyntaxError`: If the current token does not match the expected structure for a function call or identifier.

**parse_member_access**
   - **Description**: This method parses member access operations, such as accessing a field of an object. It constructs a `MemberAccessNode` representing the member access and handles cases where multiple member accesses are chained.
   - **Attributes**:
      - `object (str)`: The object being accessed.
   - **Returns**:
      - `MemberAccessNode`: An object representing the member access operation.
   - **Raises**:
      - `SyntaxError`: If the current token is not a valid identifier following the dot (`.`), or if the structure of the member access is not valid.


API References For DirectX , Metal And OpenGL To CrossGL
---------------------------------------------------------

DirectX AST
-----------

TernaryOpNode
~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a ternary operation in an abstract syntax tree (AST).
   -  Contains the condition, the expression to evaluate if the
      condition is true, and the expression to evaluate if the condition
      is false.

-  **Attributes**:

   -  `condition`: The condition expression for the ternary operation.
   -  `true_expr`: The expression evaluated when the condition is true.
   -  `false_expr`: The expression evaluated when the condition is false.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `TernaryOpNode`
         instance, including the condition, true expression, and false
         expression.

ShaderNode
~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a shader in an abstract syntax tree (AST).
   -  Contains structures for vertex and pixel shader inputs and
      outputs, as well as functions defined within the shader.

-  **Attributes**:

   -  `vsinput_struct`: The structure defining the inputs for the
      vertex shader.
   -  `vsoutput_struct`: The structure defining the outputs for the
      vertex shader.
   -  `psinput_struct`: The structure defining the inputs for the
      pixel shader.
   -  `psoutput_struct`: The structure defining the outputs for the
      pixel shader.
   -  `functions`: The list of functions defined within the shader.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `ShaderNode` instance,
         including the vertex and pixel shader input/output structures
         and functions.

`StructNode`
~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a structure in an abstract syntax tree (AST).
   -  Contains the name of the structure and its members.

-  **Attributes**:

   -  `name`: The name of the structure.
   -  `members`: The list of members (fields) within the structure.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `StructNode` instance,
         including the structure’s name and its members.

FunctionNode
~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a function in an abstract syntax tree (AST).
   -  Contains the function’s return type, name, parameters, and body.

-  **Attributes**:

   -  `return_type`: The return type of the function.
   -  `name`: The name of the function.
   -  `params`: The list of parameters for the function.
   -  `body`: The body of the function, containing the statements to
      be executed.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `FunctionNode`
         instance, including the return type, name, parameters, and body
         of the function.

VariableNode
~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a variable in an abstract syntax tree (AST).
   -  Contains the variable’s type, name, and optional semantic
      information.

-  **Attributes**:

   -  `vtype`: The type of the variable.
   -  `name`: The name of the variable.
   -  `semantic`: Optional semantic information associated with the
      variable.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `VariableNode`
         instance, including the variable’s type, name, and semantic
         information.

AssignmentNode
~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents an assignment operation in an abstract syntax tree
      (AST).
   -  Contains the left-hand side (variable or expression), right-hand
      side (value or expression), and the operator used for the
      assignment.

-  **Attributes**:

   -  `left`: The left-hand side of the assignment (variable or
      expression).
   -  `right`: The right-hand side of the assignment (value or
      expression).
   -  `operator`: The operator used for the assignment, defaulting to
      `"="`.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `AssignmentNode`
         instance, including the left-hand side, operator, and
         right-hand side of the assignment.

IfNode
~~~~~~~~~~

-  **Description**:

   -  Represents an `if` statement in an abstract syntax tree (AST).
   -  Contains the condition for the `if` statement, the body to
      execute if the condition is true, and an optional body for the
      `else` branch.

-  **Attributes**:

   -  `condition`: The condition to evaluate for the `if` statement.
   -  `if_body`: The body of code to execute if the condition is true.
   -  `else_body`: The optional body of code to execute if the
      condition is false.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `IfNode` instance,
         including the condition, `if` body, and `else` body.

ForNode
~~~~~~~~~~~

-  **Description**:

   -  Represents a `for` loop statement in an abstract syntax tree
      (AST).
   -  Contains the initialization, condition, update expression, and the
      body of the loop.

-  **Attributes**:

   -  `init`: The initialization expression for the `for` loop.
   -  `condition`: The condition to evaluate for continuing the loop.
   -  `update`: The update expression to modify the loop variable.
   -  `body`: The body of code to execute during each iteration of the
      loop.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `ForNode` instance,
         including the initialization, condition, update, and body of
         the `for` loop.

ReturnNode
~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a `return` statement in an abstract syntax tree
      (AST).
   -  Contains the value to be returned from a function or method.

-  **Attributes**:

   -  `value`: The value to return from the function or method.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `ReturnNode` instance,
         including the value to be returned.

FunctionCallNode
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a function call in an abstract syntax tree (AST).
   -  Contains the name of the function being called and the arguments
      passed to it.

-  **Attributes**:

   -  `name`: The name of the function being called.
   -  `args`: The list of arguments passed to the function.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `FunctionCallNode`
         instance, including the function name and arguments.

BinaryOpNode
~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a binary operation in an abstract syntax tree (AST).
   -  Contains the left operand, the operator used, and the right
      operand.

-  **Attributes**:

   -  `left`: The left operand of the binary operation.
   -  `op`: The operator used in the binary operation.
   -  `right`: The right operand of the binary operation.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `BinaryOpNode`
         instance, including the left operand, operator, and right
         operand.

MemberAccessNode
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents access to a member of an object in an abstract syntax
      tree (AST).
   -  Contains the object being accessed and the member being accessed.

-  **Attributes**:

   -  `object`: The object whose member is being accessed.
   -  `member`: The member of the object being accessed.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `MemberAccessNode`
         instance, including the object and the member.

VectorConstructorNode
~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a vector constructor in an abstract syntax tree (AST).
   -  Contains the type of the vector and the arguments used to
      initialize it.

-  **Attributes**:

   -  `type_name`: The type of the vector being constructed.
   -  `args`: The list of arguments used to initialize the vector.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the
         `VectorConstructorNode` instance, including the vector type
         and arguments.

UnaryOpNode
~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a unary operation in an abstract syntax tree (AST).
   -  Contains the operator used and the operand on which the operation
      is performed.

-  **Attributes**:

   -  `op`: The operator used in the unary operation.
   -  `operand`: The operand on which the unary operation is applied.

-  **Methods**:

   -  **__repr__**:

      -  Returns a string representation of the `UnaryOpNode`
         instance, including the operator and operand.

   -  **`__str__`**:

      -  Returns a formatted string of the unary operation, showing the
         operator followed by the operand.

DirectX Lexer
-------------

Tokens
~~~~~~

-  ``COMMENT_SINGLE``: Matches single-line comments starting with
   ``//``.
-  ``COMMENT_MULTI``: Matches multi-line comments enclosed by
   ``/* ... */``.
-  ``STRUCT``: Matches the keyword ``struct``.
-  ``CBUFFER``: Matches the keyword ``cbuffer``.
-  ``TEXTURE2D``: Matches the keyword ``Texture2D``.
-  ``SAMPLER_STATE``: Matches the keyword ``SamplerState``.
-  ``FVECTOR``: Matches float vector types (e.g., ``float2``,
   ``float3``, ``float4``).
-  ``FLOAT``: Matches the keyword ``float``.
-  ``INT``: Matches the keyword ``int``.
-  ``UINT``: Matches the keyword ``uint``.
-  ``BOOL``: Matches the keyword ``bool``.
-  ``MATRIX``: Matches matrix types (e.g., ``float2x2``,
   ``float3x3``, ``float4x4``).
-  ``VOID``: Matches the keyword ``void``.
-  ``RETURN``: Matches the keyword ``return``.
-  ``IF``: Matches the keyword ``if``.
-  ``ELSE_IF``: Matches ``else if`` keyword.
-  ``ELSE``: Matches the keyword ``else``.
-  ``FOR``: Matches the keyword ``for``.
-  ``REGISTER``: Matches the keyword ``register``.
-  ``SEMANTIC``: Matches semantic annotations (e.g.,
   ``: POSITION``).
-  ``IDENTIFIER``: Matches identifiers (variable names, function
   names, etc.).
-  ``NUMBER``: Matches numerical literals (integers and floats).
-  ``LBRACE``: Matches the left brace ``{``.
-  ``RBRACE``: Matches the right brace ``}``.
-  ``LPAREN``: Matches the left parenthesis ``(``.
-  ``RPAREN``: Matches the right parenthesis ``)``.
-  ``LBRACKET``: Matches the left bracket ``[``.
-  ``RBRACKET``: Matches the right bracket ``]``.
-  ``SEMICOLON``: Matches the semicolon ``;``.
-  ``COMMA``: Matches the comma ``,``.
-  ``COLON``: Matches the colon ``:``.
-  ``QUESTION``: Matches the question mark ``?``.
-  ``LESS_EQUAL``: Matches the less than or equal to operator
   ``<=``.
-  ``GREATER_EQUAL``: Matches the greater than or equal to operator
   ``>=``.
-  ``LESS_THAN``: Matches the less than operator ``<``.
-  ``GREATER_THAN``: Matches the greater than operator ``>``.
-  ``EQUAL``: Matches the equality operator ``==``.
-  ``NOT_EQUAL``: Matches the not equal to operator ``!=``.
-  ``PLUS_EQUALS``: Matches the ``+=`` operator.
-  ``MINUS_EQUALS``: Matches the ``-=`` operator.
-  ``MULTIPLY_EQUALS``: Matches the ``*=`` operator.
-  ``DIVIDE_EQUALS``: Matches the ``/=`` operator.
-  ``AND``: Matches the logical AND operator ``&&``.
-  ``OR``: Matches the logical OR operator ``||``.
-  ``DOT``: Matches the dot operator ``.``.
-  ``MULTIPLY``: Matches the multiplication operator ``*``.
-  ``DIVIDE``: Matches the division operator ``/``.
-  ``PLUS``: Matches the addition operator ``+``.
-  ``MINUS``: Matches the subtraction operator ``-``.
-  ``EQUALS``: Matches the assignment operator ``=``.
-  ``WHITESPACE``: Matches whitespace characters.

Keywords
~~~~~~~~

-  ``struct``: Maps to ``STRUCT``.
-  ``cbuffer``: Maps to ``CBUFFER``.
-  ``Texture2D``: Maps to ``TEXTURE2D``.
-  ``SamplerState``: Maps to ``SAMPLER_STATE``.
-  ``float``: Maps to ``FLOAT``.
-  ``float2``, ``float3``, ``float4``: Map to ``FVECTOR``.
-  ``int``: Maps to ``INT``.
-  ``uint``: Maps to ``UINT``.
-  ``bool``: Maps to ``BOOL``.
-  ``void``: Maps to ``VOID``.
-  ``return``: Maps to ``RETURN``.
-  ``if``: Maps to ``IF``.
-  ``else``: Maps to ``ELSE``.
-  ``for``: Maps to ``FOR``.
-  ``register``: Maps to ``REGISTER``.

__init__
~~~~~~~~~~~~

-  **Description**:

   -  Initializes the lexer with the given source code.
   -  Tokenizes the source code into a list of tokens.

-  **Parameters**:

   -  `code`: The source code to be tokenized.

-  **Returns**:

   -  None

-  **Raises**:

   -  None

.. _tokenize-1:

Tokenize:
~~~~~~~~~~~~

-  **Description**:

   -  Tokenizes the source code into a list of tokens based on defined
      patterns.
   -  Iterates through the source code, matches patterns, and
      categorizes tokens, while ignoring whitespace and comments.

-  **Returns**:

   -  None

-  **Raises**:

   -  `SyntaxError`: If an illegal character is encountered in the
      source code.

DirectX Parser
--------------

.. _init__-1:

__init__
~~~~~~~~~~~~

-  **Description**:

   -  Initializes the parser with a list of tokens.
   -  Sets the initial position and current token, and skips any initial
      comments.

-  **Parameters**:

   -  `tokens`: The list of tokens to be parsed.

-  **Returns**:

   -  None

-  **Raises**:

   -  None

skip_comments
~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Skips over tokens that are comments (both single-line and
      multi-line) in the source code.

-  **Returns**:

   -  None

-  **Raises**:

   -  None

eat
~~~~~~~

-  **Description**:

   -  Consumes the current token if it matches the expected type.
   -  Advances to the next token and skips any comments following the
      current token.

-  **Parameters**:

   -  `token_type`: The type of token expected to be consumed.

-  **Returns**:

   -  None

-  **Raises**:

   -  `SyntaxError`: If the current token does not match the expected
      token type.

parse
~~~~~~~~~

-  **Description**:

   -  Parses the entire shader code by calling parse_shader.
   -  Ensures that the end of the file (EOF) is reached after parsing.

-  **Returns**:

   -  The parsed shader object.

-  **Raises**:

   -  None

parse_shader
~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses the shader code to extract structures and functions.
   -  Identifies and assigns structures to specific shader stages and
      collects functions.

-  **Returns**:

   -  A `ShaderNode` object containing the parsed structures and
      functions.

-  **Raises**:

   -  None

parse_struct
~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses a structure definition, including its name and members.
   -  Processes each member’s type, name, and optional semantic
      information.

-  **Returns**:

   -  A `StructNode` object representing the parsed structure.

-  **Raises**:

   -  None

parse_function
~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses a function definition, including its return type, name,
      parameters, and body.
   -  Handles optional semantic tokens and constructs a `FunctionNode`
      with the parsed details.

-  **Returns**:

   -  A `FunctionNode` object representing the parsed function.

-  **Raises**:

   -  None

parse_parameters
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses function parameters, including their types, names, and
      optional semantic information.
   -  Continues parsing until the closing parenthesis is encountered.

-  **Returns**:

   -  A list of `VariableNode` objects representing the function
      parameters.

-  **Raises**:

   -  None

parse_block
~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses a block of statements enclosed in braces.
   -  Collects and returns statements until the closing brace is
      encountered.

-  **Returns**:

   -  A list of statements parsed from the block.

-  **Raises**:

   -  None

parse_statement
~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses different types of statements based on the current token.
   -  Handles variable declarations or assignments, `if` statements,
      `for` loops, `return` statements, and expressions.

-  **Returns**:

   -  A statement node representing the parsed statement.

-  **Raises**:

   -  None

parse_variable_declaration_or_assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses variable declarations, assignments, and other related
      statements based on the current token.
   -  Handles various scenarios including simple declarations,
      assignments with expressions, and compound assignments.

-  **Returns**:

   -  A node representing a variable declaration or assignment, or an
      expression statement if none of the previous conditions are met.

-  **Raises**:

   -  None

parse_if_statement
~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses an `if` statement, including its condition, the body of
      the `if` block, and optionally an `else` or `else if` block.
   -  Handles nested `else if` statements by delegating to
      `parse_else_if_statement` if the next token is `ELSE_IF`.

-  **Returns**:

   -  An `IfNode` representing the parsed `if` statement, including
      its condition, `if` block, and optional `else` or `else if`
      block.

-  **Raises**:

   -  None

parse_else_if_statement
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses an `else if` statement, including its condition, the body
      of the `else if` block, and optionally an `else` or another
      `else if` block.
   -  Handles nested `else if` statements by calling
      `parse_else_if_statement` recursively.

-  **Returns**:

   -  An `IfNode` representing the parsed `else if` statement,
      including its condition, `else if` block, and optional `else`
      or nested `else if` blocks.

-  **Raises**:

   -  None

parse_for_statement
~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses a `for` loop statement, including initialization, loop
      condition, update expression, and the loop body.
   -  Handles initialization of variables or simple expressions.
   -  Extracts and processes the condition and update expressions, along
      with the body of the loop.

-  **Returns**:

   -  A `ForNode` representing the parsed `for` loop statement,
      including the initialization, condition, update expression, and
      body of the loop.

-  **Raises**:

   -  `SyntaxError` if the `for` statement’s syntax is incorrect or
      missing required components.

parse_return_statement
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses a `return` statement.
   -  Extracts the return value and ensures it is followed by a
      semicolon.

-  **Returns**:

   -  A `ReturnNode` containing the parsed return value.

parse_expression_statement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses a statement that consists of an expression followed by a
      semicolon.
   -  Handles expressions that may be standalone or part of more complex
      statements.

-  **Returns**:

   -  The parsed expression, which could be any valid expression node
      (`BinaryOpNode`, `UnaryOpNode`, `FunctionCallNode`, etc.).

parse_expression
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses an expression that may involve assignment operators,
      ternary operations, and logical operations.
   -  Handles assignment (`=`, `+=`, `-=`, `*=`, `/=`) and
      ternary (`condition ? true_expr : false_expr`) operators.

-  **Returns**:

   -  The root node of the parsed expression, which could be an
      `AssignmentNode`, `TernaryOpNode`, or another type of
      expression node.

parse_assignment
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses an assignment expression, which can be a simple assignment
      or involve nested assignments.
   -  Handles the assignment operator (`=`) and recursively parses the
      right-hand side of the assignment.

-  **Returns**:

   -  An `AssignmentNode` representing the assignment operation, or
      the left-hand side expression if no assignment operator is found.

parse_logical_or
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses logical OR expressions, handling multiple OR operations.
   -  Constructs a binary operation node for each logical OR (`||`)
      encountered.

-  **Returns**:

   -  A `BinaryOpNode` representing the logical OR operation, with
      nested binary operations for multiple OR expressions.

parse_logical_and
~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses logical AND expressions, handling multiple AND operations.
   -  Constructs a binary operation node for each logical AND (`&&`)
      encountered.

-  **Returns**:

   -  A `BinaryOpNode` representing the logical AND operation, with
      nested binary operations for multiple AND expressions.

parse_equality
~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses equality and inequality expressions, handling multiple
      equality checks.
   -  Constructs a binary operation node for each equality (`==`) or
      inequality (`!=`) operation encountered.

-  **Returns**:

   -  A `BinaryOpNode` representing the equality or inequality
      operation, with nested binary operations for multiple equality
      checks.

parse_relational
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses relational expressions, handling comparisons like less than
      (`<`), greater than (`>`), less than or equal to (`<=`), and
      greater than or equal to (`>=`).
   -  Constructs a binary operation node for each relational operation
      encountered.

-  **Returns**:

   -  A `BinaryOpNode` representing the relational operation, with
      nested binary operations for multiple comparisons.

parse_additive
~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses additive expressions, which involve addition (`+`) and
      subtraction (`-`).
   -  Constructs a `BinaryOpNode` for each additive operation, with
      nested binary operations for multiple additions or subtractions.

-  **Returns**:

   -  A `BinaryOpNode` representing the additive operation, with
      nested binary operations for multiple additive expressions.

parse_multiplicative
~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Parses multiplicative expressions, which include multiplication
      (`*`) and division (`/`).
   -  Constructs a `BinaryOpNode` for each multiplicative operation,
      handling nested expressions where multiple multiplicative
      operations are present.

-  **Returns**:

   -  A `BinaryOpNode` representing the multiplicative operation,
      including any nested operations.

parse_unary
~~~~~~~~~~~~~~~

-  **Parameters**:

   -  None (The `parse_unary` function does not take any explicit
      parameters.)

-  **Description**:

   -  The `parse_unary` function is responsible for parsing unary
      expressions in a mathematical expression.
   -  Unary expressions involve a single operand (e.g., `-x`, `+y`),
      where the unary operator (`+` or `-`) is applied to the
      operand.
   -  If the current token corresponds to a unary operator (`PLUS` or
      `MINUS`), the function processes it and recursively parses the
      operand.
   -  Otherwise, it falls back to parsing the primary expression (e.g.,
      literals, identifiers, function calls).

-  **Returns**:

   -  A `UnaryOpNode` representing the unary operation, including any
      nested unary expressions.

parse_primary
~~~~~~~~~~~~~~~~~

-  **Parameters**:

   -  None

-  **Description**:

   -  Handles the parsing of primary expressions in a mathematical
      expression.
   -  Primary expressions include literals (e.g., integers, floats,
      vectors), identifiers (variable names), function calls, and
      parenthesized expressions (nested expressions within parentheses).
   -  Examines the current token and determines the appropriate action
      based on the token type.

-  **Returns**:

   -  The parsed expression (a `VariableNode`, numeric value, function
      call, or parenthesized expression).

parse_vector_constructor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Parameters**:

   -  `type_name`: The type of the vector being constructed (e.g.,
      “int”, “float”, “fvector”).

-  **Description**:

   -  The `parse_vector_constructor` function handles the parsing of
      vector constructors.
   -  Vector constructors are used to create vectors by specifying their
      components within parentheses (e.g., `(1, 2, 3)`).
   -  The function iterates through the tokens until it encounters the
      closing parenthesis (`RPAREN`).
   -  It parses each expression (component) separated by commas and
      collects them in the `args` list.
   -  Finally, it constructs a `VectorConstructorNode` with the
      specified type and the collected arguments.

-  **Returns**:

   -  A `VectorConstructorNode` representing the constructed vector.

parse_function_call_or_identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Parameters**:

   -  None (The `parse_function_call_or_identifier` function does not
      take any explicit parameters.)

-  **Description**:

   -  The `parse_function_call_or_identifier` function handles the
      parsing of either a function call or an identifier (variable
      name).
   -  It examines the current token:

      -  If the token corresponds to an `IDENTIFIER`, it extracts the
         name and advances to the next token.
      -  If the next token is an `LPAREN`, it indicates a function
         call, and the function parses the arguments using
         `self.parse_function_call(name)`.
      -  If the next token is a `DOT`, it indicates member access
         (e.g., accessing a method or property of an object) and parses
         it using `self.parse_member_access(name)`.
      -  Otherwise, it constructs a `VariableNode` with an empty type
         and the extracted name.

-  **Returns**:

   -  Either a function call node, a member access node, or a variable
      node, depending on the context.

parse_function_call
~~~~~~~~~~~~~~~~~~~~~~~

-  **Parameters**:

   -  `name`: The name of the function being called.

-  **Description**:

   -  The `parse_function_call` function handles the parsing of
      function calls in an expression.
   -  It starts by consuming the opening parenthesis token (`LPAREN`).
   -  While the current token is not the closing parenthesis token
      (`RPAREN`), it continues to parse expressions (arguments)
      separated by commas.
   -  Each argument is obtained by calling `self.parse_expression()`.
   -  If a comma follows an argument, it consumes the comma token.
   -  Finally, it consumes the closing parenthesis token and constructs
      a `FunctionCallNode` with the specified function name and
      arguments.

-  **Returns**:

   -  A `FunctionCallNode` representing the function call.

parse_member_access
~~~~~~~~~~~~~~~~~~~~~~~

-  **Parameters**:

   -  `object`: The object (variable or expression) on which the
      member access is performed.

-  **Description**:

   -  The `parse_member_access` function handles the parsing of member
      access in an expression.
   -  It starts by consuming the dot token (`DOT`).
   -  If the next token is not an `IDENTIFIER`, it raises a
      `SyntaxError`.
   -  Otherwise, it extracts the member name and advances to the next
      token.
   -  If there’s another dot after this member access, it recursively
      calls itself with the updated `MemberAccessNode`.
   -  Otherwise, it constructs a `MemberAccessNode` with the specified
      object and member.

-  **Returns**:

   -  A `MemberAccessNode` representing the member access.

DirectX Codegen
---------------

The HLSLCodeGen class within the CrossGL framework is pivotal in
translating CrossGL shader abstract syntax trees (AST) into CrossGL
code, which is essential for DirectX applications. This class
systematically converts the AST (representing the logical structure of a
shader)—>into corresponding CrossGL code that can be executed.

Methods

__init__(self)
~~~~~~~~~~~~~~

Initializes the code generator.

generate
~~~~~~~~~~~~

-  **Description**:

   -  Generates shader code from the given Abstract Syntax Tree (AST).
   -  Handles the creation of both vertex and fragment shaders,
      including custom functions and shader-specific I/O declarations.

-  **Steps**:

   1. **Process Structs**:

      -  Calls `process_structs` to handle any structures defined in
         the AST.

   2. **Initialize Shader Code**:

      -  Starts with the base shader declaration line:
         `shader main {\n`.

   3. **Generate Custom Functions**:

      -  Iterates through the functions in the AST, excluding the main
         vertex and fragment functions (`VSMain` and `PSMain`).
      -  Appends the generated code for each custom function.

   4. **Generate Vertex Shader**:

      -  Adds a section comment for the vertex shader.
      -  Includes vertex shader I/O declarations by calling
         `generate_io_declarations` with `"vertex"`.
      -  Adds the main function for the vertex shader using
         `generate_vertex_main`, fetching the function named
         `VSMain`.

   5. **Generate Fragment Shader**:

      -  Adds a section comment for the fragment shader.
      -  Includes fragment shader I/O declarations by calling
         `generate_io_declarations` with `"fragment"`.
      -  Adds the main function for the fragment shader using
         `generate_fragment_main`, fetching the function named
         `PSMain`.

   6. **Finalize Shader Code**:

      -  Closes the shader block with `}\n`.

-  **Returns**:

   -  The complete shader code as a string.

process_structs
~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Processes structure definitions from the Abstract Syntax Tree
      (AST) and populates lists of vertex and fragment shader inputs and
      outputs based on the members of the provided structures.

-  **Parameters**:

   -  `ast` (`ShaderNode`): An instance of `ShaderNode` containing
      structure definitions and functions for vertex and fragment
      shaders. This includes optional vertex input (`vsinput_struct`),
      vertex output (`vsoutput_struct`), fragment input
      (`psinput_struct`), and fragment output (`psoutput_struct`)
      structures.

-  **Returns**:

   -  `None`: This method updates instance variables
      (`self.vertex_inputs`, `self.vertex_outputs`,
      `self.fragment_inputs`, and `self.fragment_outputs`) directly
      based on the structure members in the provided `ast`.

generate_io_declarations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates shader I/O declarations based on the specified shader
      type (vertex or fragment). It creates declarations for input and
      output variables in the shader code.

-  **Parameters**:

   -  `shader_type` (`str`): Specifies the type of shader for which
      to generate I/O declarations. It can be `"vertex"` or
      `"fragment"`.

-  **Returns**:

   -  `str`: A string containing the formatted I/O declarations for
      the specified shader type. The string includes `input` and
      `output` statements with appropriate types and names, formatted
      according to the shader’s requirements. The string is stripped of
      any trailing whitespace.

generate_function
~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates the code for a function based on the provided
      `FunctionNode`. This includes defining the function’s return
      type, name, parameters, and body.

-  **Parameters**:

   -  `func` (`FunctionNode`): The function node containing the
      details of the function to be generated. It includes the return
      type, function name, parameters, and body.

-  **Returns**:

   -  `str`: A string containing the formatted code for the function.
      This includes the function signature and body, properly indented
      and formatted.

generate_vertex_main
~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates the main function for the vertex shader, which is
      typically the entry point of the shader. It formats and includes
      the function body with appropriate indentation.

-  **Parameters**:

   -  `func` (`FunctionNode`): The function node representing the
      vertex shader’s main function. It contains the body of the
      function that will be used to generate the shader code.

-  **Returns**:

   -  `str`: A string containing the formatted code for the vertex
      shader’s `main` function, including proper indentation and the
      function body.

generate_fragment_main
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates the main function for the fragment shader, which is
      typically the entry point of the shader. It formats and includes
      the function body with appropriate indentation.

-  **Parameters**:

   -  `func` (`FunctionNode`): The function node representing the
      fragment shader’s main function. It contains the body of the
      function that will be used to generate the shader code.

-  **Returns**:

   -  `str`: A string containing the formatted code for the fragment
      shader’s `main` function, including proper indentation and the
      function body.

generate_function_body
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates the code for the body of a function by iterating through
      statements. It formats each statement based on its type and
      includes the appropriate indentation.

-  **Parameters**:

   -  `body` (`List[ASTNode]`): A list of statements in the function
      body, where each statement is an instance of `ASTNode` or its
      derived classes.
   -  `indent` (`int`): The level of indentation to apply to each
      line of code. Default is `0`.
   -  `is_main` (`bool`): A flag indicating whether the function
      being generated is the `main` function. Default is `False`.

-  **Returns**:

   -  `str`: A string containing the formatted code for the function
      body, including the appropriate indentation and formatted
      statements.

generate_for_loop
~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates code for a `for` loop based on the provided
      `ForNode`. This includes formatting the initialization,
      condition, and update expressions, and properly indenting the loop
      body.

-  **Parameters**:

   -  `node` (`ForNode`): An instance of `ForNode` representing
      the `for` loop, containing `init`, `condition`, `update`,
      and `body`.
   -  `indent` (`int`): The level of indentation to apply to each
      line of the loop code. It controls how deep the code will be
      indented. Default is `0`.
   -  `is_main` (`bool`): A flag indicating whether the loop is
      inside the `main` function. Default is `False`.

-  **Returns**:

   -  `str`: A string containing the formatted code for the `for`
      loop, including the initialization, condition, update, and the
      body of the loop with proper indentation.

generate_if_statement
~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates code for an `if` statement, including handling
      `else` and `else if` branches. The code is properly indented
      according to the provided level.

-  **Parameters**:

   -  `node` (`IfNode`): An instance of `IfNode` representing the
      `if` statement, including the condition, `if_body`, and
      `else_body`.
   -  `indent` (`int`): The level of indentation to apply to each
      line of the `if` statement code. Default is `0`.
   -  `is_main` (`bool`): A flag indicating whether the `if`
      statement is inside the `main` function. Default is `False`.

-  **Returns**:

   -  `str`: A string containing the formatted code for the `if`
      statement, including the condition, body, and optional `else` or
      `else if` blocks with proper indentation.

generate_assignment
~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates code for an assignment operation. Special handling is
      included for assignments where the left-hand side is a member of
      `output` when in the `main` function.

-  **Parameters**:

   -  `node` (`AssignmentNode`): An instance of `AssignmentNode`
      representing the assignment operation, including the left-hand
      side (`node.left`) and right-hand side (`node.right`)
      expressions.
   -  `is_main` (`bool`): A flag indicating whether the code is
      being generated inside the `main` function. Default is
      `False`.

-  **Returns**:

   -  `str`: A string containing the formatted code for the
      assignment. Special handling for output variables if `is_main`
      is `True`, translating `position` to `gl_Position`.

generate_expression
~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Generates code for various types of expressions. Handles different
      node types such as variables, binary operations, assignments,
      unary operations, function calls, member accesses, ternary
      operations, and vector constructors.

-  **Parameters**:

   -  `expr` (`ExpressionNode`): The expression to generate code
      for, which can be a node of various types (e.g., `VariableNode`,
      `BinaryOpNode`, etc.).
   -  `is_main` (`bool`): A flag indicating whether the code is
      being generated inside the `main` function. Default is
      `False`.

-  **Returns**:

   -  `str`: A string containing the formatted code for the
      expression, appropriately handling different node types.

map_type
~~~~~~~~~~~~

-  **Description**:

   -  Maps an HLSL type to its corresponding type in the shader language
      used by the generator. Utilizes a dictionary (`type_map`) for
      type conversion.

-  **Parameters**:

   -  `hlsl_type` (`str`): The HLSL type string that needs to be
      mapped.

-  **Returns**:

   -  `str`: The mapped type string based on the `type_map`
      dictionary. If the type is not found in the dictionary, it returns
      the original `hlsl_type`.

Metal
------

Metal AST
---------

.. _ternaryopnode-1:

TernaryOpNode
~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a ternary conditional operation in the abstract syntax
      tree (AST). It contains a condition, a true expression, and a
      false expression.

-  **Constructor Parameters**:

   -  `condition` (`ASTNode`): The condition to be evaluated.
   -  `true_expr` (`ASTNode`): The expression to be evaluated and
      returned if the condition is true.
   -  `false_expr` (`ASTNode`): The expression to be evaluated and
      returned if the condition is false.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `TernaryOpNode` instance.
      -  **Returns**: `str` - A string representation of the node
         with its condition, true expression, and false expression.

.. _shadernode-1:

ShaderNode
~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a shader node in the abstract syntax tree (AST) for a
      shader. This node contains the functions defined in the shader.

-  **Constructor Parameters**:

   -  `functions` (`List[FunctionNode]`): A list of `FunctionNode`
      instances representing the functions defined in the shader.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `ShaderNode` instance.
      -  **Returns**: `str` - A string representation of the node
         with its functions.

.. _structnode-1:

StructNode
~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a struct definition in the abstract syntax tree (AST)
      for a shader. This node contains the name of the struct and its
      member variables.

-  **Constructor Parameters**:

   -  `name` (`str`): The name of the struct.
   -  `members` (`List[VariableNode]`): A list of `VariableNode`
      instances representing the members of the struct.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `StructNode` instance.
      -  **Returns**: `str` - A string representation of the node
         with its name and members.

.. _functionnode-1:

FunctionNode
~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a function definition in the abstract syntax tree
      (AST). This node includes details about the function’s qualifier,
      return type, name, parameters, body, and any associated
      attributes.

-  **Constructor Parameters**:

   -  `qualifier` (`str`): The qualifier of the function (e.g.,
      `public`, `private`).
   -  `return_type` (`str`): The return type of the function.
   -  `name` (`str`): The name of the function.
   -  `params` (`List[VariableNode]`): A list of `VariableNode`
      instances representing the function’s parameters.
   -  `body` (`List[ASTNode]`): A list of `ASTNode` instances
      representing the body of the function.
   -  `attributes` (`List[str]`, optional): A list of string
      attributes associated with the function.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `FunctionNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including its qualifier, return type, name, parameters, body,
         and attributes.

ArrayAccessNode
~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents an array access operation in the abstract syntax tree
      (AST). This node contains details about the array being accessed
      and the index used to access an element within the array.

-  **Constructor Parameters**:

   -  `array` (`ASTNode`): The array being accessed.
   -  `index` (`ASTNode`): The index used to access an element in
      the array.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `ArrayAccessNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including its array and index.

.. _variablenode-1:

VariableNode
~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a variable declaration in the abstract syntax tree
      (AST). This node contains information about the variable’s type,
      its name, and any additional attributes associated with the
      variable.

-  **Constructor Parameters**:

   -  `vtype` (`str`): The type of the variable (e.g., `int`,
      `float`, `vec3`).
   -  `name` (`str`): The name of the variable.
   -  `attributes` (`list`, optional): Additional attributes or
      qualifiers associated with the variable. Defaults to an empty list
      if not provided.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `VariableNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including its type, name, and attributes.

AttributeNode
~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents an attribute or decoration associated with a function,
      variable, or other elements in the abstract syntax tree (AST).
      This node includes the name of the attribute and any associated
      arguments.

-  **Constructor Parameters**:

   -  `name` (`str`): The name of the attribute (e.g., `location`,
      `binding`).
   -  `args` (`list`, optional): A list of arguments or parameters
      associated with the attribute. Defaults to an empty list if not
      provided.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `AttributeNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including its name and arguments.

.. _assignmentnode-1:

AssignmentNode
~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents an assignment operation in the abstract syntax tree
      (AST). This node holds the left-hand side (LHS) variable or
      expression, the right-hand side (RHS) value or expression, and the
      operator used for assignment.

-  **Constructor Parameters**:

   -  `left` (`ASTNode`): The variable or expression on the left
      side of the assignment.
   -  `right` (`ASTNode`): The value or expression to be assigned to
      the left side.
   -  `operator` (`str`, optional): The assignment operator (e.g.,
      `=`, `+=`, `-=`, etc.). Defaults to `"="`.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `AssignmentNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including its left side, operator, and right side.

.. _ifnode-1:

IfNode
~~~~~~~~~~

-  **Description**:

   -  Represents an `if` statement in the abstract syntax tree (AST).
      This node encapsulates the condition of the `if` statement and
      its associated `if` and `else` bodies.

-  **Constructor Parameters**:

   -  `condition` (`ASTNode`): The condition expression that
      determines whether the `if` body or `else` body should be
      executed.
   -  `if_body` (`list` of `ASTNode`): The statements to be
      executed if the condition evaluates to `True`.
   -  `else_body` (`list` of `ASTNode`, optional): The statements
      to be executed if the condition evaluates to `False`. Defaults
      to `None`.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `IfNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including its condition, `if` body, and `else` body.

.. _fornode-1:

ForNode
~~~~~~~~~~~

-  **Description**:

   -  Represents a `for` loop in the abstract syntax tree (AST). This
      node captures the initialization, loop condition, update
      expression, and the body of the loop.

-  **Constructor Parameters**:

   -  `init` (`ASTNode`): The initialization statement for the
      `for` loop, such as setting up a loop variable.
   -  `condition` (`ASTNode`): The loop condition that determines
      whether the loop should continue running.
   -  `update` (`ASTNode`): The update expression to be evaluated at
      the end of each loop iteration, such as incrementing a loop
      variable.
   -  `body` (`list` of `ASTNode`): The statements to be executed
      on each iteration of the loop.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `ForNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including its initialization, condition, update, and body.

.. _returnnode-1:

ReturnNode
~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a `return` statement in the abstract syntax tree
      (AST). This node captures the value that is to be returned from a
      function.

-  **Constructor Parameters**:

   -  `value` (`ASTNode`): The expression or value to be returned by
      the function.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `ReturnNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including the value being returned.

.. _functioncallnode-1:

FunctionCallNode
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a function call in the abstract syntax tree (AST). This
      node contains information about the function being called and the
      arguments passed to it.

-  **Constructor Parameters**:

   -  `name` (`str`): The name of the function being called.
   -  `args` (`List[ASTNode]`): A list of arguments passed to the
      function call. Each argument is an `ASTNode`.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `FunctionCallNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including the function name and its arguments.

.. _binaryopnode-1:

BinaryOpNode
~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a binary operation in the abstract syntax tree (AST).
      This node is used for operations involving two operands and an
      operator, such as addition, subtraction, multiplication, etc.

-  **Constructor Parameters**:

   -  `left` (`ASTNode`): The left operand of the binary operation.
   -  `op` (`str`): The operator used in the operation (e.g., `+`,
      `-`, `*`, `/`).
   -  `right` (`ASTNode`): The right operand of the binary
      operation.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `BinaryOpNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including the left operand, operator, and right operand.

.. _memberaccessnode-1:

MemberAccessNode
~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents access to a member of an object in the abstract syntax
      tree (AST). This node is used to refer to a property or method of
      an object.

-  **Constructor Parameters**:

   -  `object` (`ASTNode`): The object or variable whose member is
      being accessed.
   -  `member` (`str`): The name of the member being accessed (e.g.,
      a property or method).

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `MemberAccessNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including the object and the member being accessed.

.. _vectorconstructornode-1:

VectorConstructorNode
~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a vector constructor in the abstract syntax tree (AST).
      This node is used to construct vector types by specifying the type
      and the components of the vector.

-  **Constructor Parameters**:

   -  `type_name` (`str`): The name of the vector type being
      constructed (e.g., `vec3`, `vec4`).
   -  `args` (`List[ASTNode]`): A list of expressions representing
      the components of the vector.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `VectorConstructorNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including the vector type and its components.

.. _unaryopnode-1:

UnaryOpNode
~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a unary operation in the abstract syntax tree (AST).
      This node is used to model operations that apply to a single
      operand, such as negation or increment.

-  **Constructor Parameters**:

   -  `op` (`str`): The operator for the unary operation (e.g.,
      `+`, `-`, `++`, `--`).
   -  `operand` (`ASTNode`): The operand on which the unary
      operation is applied.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `UnaryOpNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including the unary operator and its operand.

TextureSampleNode
~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a texture sampling operation in the abstract syntax
      tree (AST). This node is used to model operations where a texture
      is sampled using specified coordinates and a sampler.

-  **Constructor Parameters**:

   -  `texture` (`str`): The name or reference to the texture being
      sampled.
   -  `sampler` (`str`): The name or reference to the sampler used
      for sampling the texture.
   -  `coordinates` (`ASTNode`): The coordinates used to sample the
      texture, typically represented as a vector.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `TextureSampleNode` instance.
      -  **Returns**: `str` - A string representation of the node,
         including the texture, sampler, and coordinates used for
         sampling.

ThreadgroupSyncNode
~~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a synchronization point for thread groups in the
      abstract syntax tree (AST). This node is used to synchronize the
      execution of threads within a thread group.

-  **Constructor Parameters**:

   -  No parameters are needed for this class.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `ThreadgroupSyncNode` instance.
      -  **Returns**: `str` - A string indicating that the node is
         a synchronization point for thread groups.

ConstantBufferNode
~~~~~~~~~~~~~~~~~~~~~~

-  **Description**:

   -  Represents a constant buffer in the abstract syntax tree (AST).
      Constant buffers are used to group and manage constants that are
      passed to shaders.

-  **Constructor Parameters**:

   -  **`name`** (`str`): The name of the constant buffer.
   -  **`members`** (`list` of `VariableNode`): A list of members
      (variables) within the constant buffer.

-  **Methods**:

   -  **__repr__**:

      -  **Description**: Returns a string representation of the
         `ConstantBufferNode` instance.
      -  **Returns**: `str` - A formatted string that includes the
         name and members of the constant buffer.

Metal Lexer
-----------

`TOKENS` and `KEYWORDS` definitions provide a comprehensive set of
token patterns for parsing a shader language, potentially for HLSL,
GLSL, or a similar language. Here’s a brief overview of what each part
does:

TOKENS List
~~~~~~~~~~~~~~~

The `TOKENS` list defines regex patterns for different types of
tokens. Each token has a name and a regex pattern to match it.

-  **Comment Tokens**:

   -  ``COMMENT_SINGLE``: Matches single-line comments starting with
      `//`.
   -  ``COMMENT_MULTI``: Matches multi-line comments enclosed in `/*`
      and `*/`.

-  **Shader and Language Constructs**:

   -  ``STRUCT``, ``CONSTANT``, ``TEXTURE2D``, ``SAMPLER``: Keywords for
      specific constructs or types.
   -  ``VECTOR``, ``FLOAT``, ``HALF``, ``INT``, ``UINT``, ``BOOL``,
      ``VOID``: Data types.
   -  ``QUESTION``, ``IF``, ``ELSE``, ``FOR``, ``RETURN``: Common
      control flow and function keywords.
   -  ``VERTEX``, ``FRAGMENT``: Shader stages.
   -  ``USING``, ``NAMESPACE``, ``METAL``, ``DEVICE``, ``THREADGROUP``,
      ``THREAD``: Specific to certain shading languages or extensions.

-  **Syntax Elements**:

   -  ``IDENTIFIER``: Matches variable and function names.
   -  ``NUMBER``: Matches numeric literals.
   -  ``STRING``: Matches string literals.
   -  ``LBRACE``, ``RBRACE``, ``LPAREN``, ``RPAREN``, ``LBRACKET``,
      ``RBRACKET``, ``SEMICOLON``, ``COMMA``, ``COLON``: Various syntax
      symbols.
   -  ``LESS_EQUAL``, ``GREATER_EQUAL``, ``LESS_THAN``,
      ``GREATER_THAN``, ``EQUAL``, ``NOT_EQUAL``: Comparison operators.
   -  ``PLUS_EQUALS``, ``MINUS_EQUALS``, ``MULTIPLY_EQUALS``,
      ``DIVIDE_EQUALS``: Compound assignment operators.
   -  ``PLUS``, ``MINU`S`, ``MULTIPLY``, ``DIVIDE``: Arithmetic
      operators.
   -  ``AND``, ``OR``: Logical operators.
   -  ``DOT``: Member access operator.
   -  ``EQUALS``: Assignment operator.
   -  ``WHITESPACE```: Matches spaces, tabs, and newlines.

.. _keywords-dictionary-1:

KEYWORDS Dictionary
~~~~~~~~~~~~~~~~~~~~~~~

The `KEYWORDS` dictionary maps specific keywords to their
corresponding token types. This helps in recognizing and categorizing
keywords during parsing.

-  **Shader and Language Keywords**:

   -  Maps shader and language-specific keywords to their token type
      names defined in `TOKENS`.

Methods
~~~~~~~~~

.. _init__self-1:

__init__(self)
~~~~~~~~~~~~~~~~~~

Initializes the code generator.

tokenize(self)
~~~~~~~~~~~~~~~~~~

| **Description:**
| Tokenizes the input code into a sequence of tokens by matching against
  predefined patterns.

| **Parameters:**
| - None

| **Returns:**
| - None

| **Raises:**
| - `SyntaxError`: If an illegal character is encountered in the input
  code.

Metal Parser
------------

.. _methods-1:

Methods
~~~~~~~~~

.. _init__self-2:

__init__(self)
~~~~~~~~~~~~~~~~~~

Initializes the code generator.

.. _eat-1:

eat
~~~~~~~

-  **Description**:

   -  Consumes the current token if it matches the expected type.
   -  Advances to the next token and skips any comments following the
      current token.

-  **Parameters**:

   -  `token_type`: The type of token expected to be consumed.

-  **Returns**: None

-  **Raises**:

   -  `SyntaxError`: If the current token does not match the expected
      token type.

skip_comments(self)
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Skips over single-line and multi-line comments in the token stream by
  advancing past them.

| **Parameters:** None

| **Returns:** None

| **Raises:** None

parse(self)
~~~~~~~~~~~~~~~

| **Description:**
| Initiates the parsing process by calling parse_shader to generate
  the Abstract Syntax Tree (AST) for the shader code. Ensures that the
  entire input has been consumed by checking for the end of file
  (`EOF`).

| **Parameters:** None

**Returns:**
   - `ASTNode`: The root node of the parsed Abstract Syntax Tree (AST) representing the shader.

**Raises:**
   - `SyntaxError`: If there is any remaining unparsed input after the shader has been parsed.

parse_shader(self)
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the shader code by sequentially identifying and processing
  various components such as preprocessor directives, `using`
  statements, structs, constant buffers, and functions. The method
  iterates through the tokens until it reaches the end of the file
  (`EOF`), constructing a list of functions and other shader
  components.

| **Parameters:**  None

**Returns:**
   - `ShaderNode`: A node representing the parsed shader, containing all the functions and components.

**Raises:**
   - `SyntaxError`: If the shader contains unrecognized tokens that cannot be skipped or parsed.

parse_preprocessor_directive(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a preprocessor directive from the shader code. It handles
  directives that include a string or are enclosed within angle brackets
  (`< >`). The method consumes tokens associated with the directive
  until it reaches the end of the directive.

| **Parameters:** None

| **Returns:** None

**Raises:**
   - `SyntaxError`: If the preprocessor directive is not properly closed with a `GREATER_THAN` token.

parse_using_statement(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `using` statement specifically for the `namespace metal;`
  declaration in the shader code. This method consumes the relevant
  tokens for `using`, `namespace`, `metal`, and the terminating
  semicolon (`;`).

| **Parameters:** None

| **Returns:** None

**Raises:**
   - `SyntaxError`: If any of the expected tokens (`USING`, `NAMESPACE`, `METAL`, or `SEMICOLON`) are not found in sequence.

parse_struct(self)
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `struct` declaration in the shader code. This method reads
  the structure’s name, its member variables, and any associated
  attributes.

| **Parameters:** None

**Returns:**
   - `StructNode`: A node representing the structure, including its name and members.

**Raises:**
   - `SyntaxError`: If any of the expected tokens (`STRUCT`, `IDENTIFIER`, `LBRACE`, `RBRACE`, `SEMICOLON`) are not found in sequence.

parse_constant_buffer(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `constant` buffer declaration in the shader code. This
  method reads the buffer’s name and its member variables.

| **Parameters:**  None

**Returns:**
   - `ConstantBufferNode`: A node representing the constant buffer, including its name and members.

**Raises:**
   - `SyntaxError`: If any of the expected tokens (`CONSTANT`, `IDENTIFIER`, `LBRACE`, `RBRACE`, `SEMICOLON`) are not found in sequence.

parse_function(self)
~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a function declaration in the shader code, including function
  qualifiers, return type, parameters, and body. Handles function
  attributes before and after the parameters.

| **Parameters:** None

**Returns:**
   - `FunctionNode`: A node representing the function, including its qualifier, return type, name, parameters, body, and attributes.

**Raises:**
   - `SyntaxError`: If any of the expected tokens (`VERTEX`, `FRAGMENT`, `KERNEL`, `IDENTIFIER`, `LPAREN`, `RPAREN`, `LBRACE`, `RBRACE`, etc.) are not found in sequence.

parse_parameters(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the parameter list for a function, including handling
  attributes, types, optional template parameters, and names. It
  continues parsing until it encounters a closing parenthesis.

| **Parameters:** None

**Returns:**
   - `List[VariableNode]`: A list of `VariableNode` instances representing each parameter with its type, name, and attributes.

**Raises:**
   - `SyntaxError`: - If an unexpected token is encountered in the parameter list. - If a token that is neither a comma nor a closing parenthesis is found when expected.

parse_attributes(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a sequence of attributes from the token stream. Attributes are
  enclosed in `[[ ]]`, and this method extracts the attribute name and
  its arguments.

| **Parameters:** None

**Returns:**
   - `List[AttributeNode]`: A list of `AttributeNode` instances representing the parsed attributes, including their names and arguments.

| **Raises:** `None`

parse_block(self)
~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a block of statements enclosed in curly braces `{}`. This
  method collects statements within the block until it encounters the
  closing brace `}`.

| **Parameters:** None

**Returns:**
   - `List[ASTNode]`: A list of statements parsed from the block, where each statement is represented as an `ASTNode`.

**Raises:**
   - `SyntaxError`: If the closing brace `RBRACE` is not found, indicating a mismatch or incomplete block.

parse_statement(self)
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a statement based on the current token type. This method
  determines the type of statement and delegates the parsing to the
  appropriate handler method, such as variable declarations, conditional
  statements, loops, or expressions.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed statement represented as an `ASTNode`. The specific type of `ASTNode` depends on the statement type, such as `VariableDeclarationNode`, `IfNode`, `ForNode`, `ReturnNode`, or `ExpressionStatementNode`.

**Raises:**
   - `SyntaxError`: If the current token does not match any known statement types or if there is an issue parsing the statement.

parse_variable_declaration_or_assignment(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a variable declaration or assignment statement. This method
  handles different cases including variable declarations with or
  without initialization, assignments, and compound assignments. It also
  deals with member accesses and operations.

| **Parameters:**
| - None

**Returns:**
   - `ASTNode`: The parsed statement represented as an `ASTNode`.This could be a `VariableNode`, `AssignmentNode`, `BinaryOpNode`, or a general expression node, depending on the syntax of the statement.

**Raises:**
   - `SyntaxError`: If the syntax of the variable declaration or assignment does not match the expected format, or if there are issues parsing the expression.


parse_if_statement(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an `if` statement. This method handles the syntax of an
  `if` statement including the condition and both the `if` and
  optional `else` blocks.

| **Parameters:** None

**Returns:**
   - `IfNode`: An AST node representing the `if` statement. 
   - This node contains:

     - The `condition` as an expression.
     - The `if_body` as a block of statements executed if the condition is true.
     - The `else_body` as a block of statements executed if the condition is false (or `None` if there is no `else` block).


**Raises:**
   - `SyntaxError`: If the syntax of the `if` statement is incorrect or if there are issues parsing the expression or blocks

parse_for_statement(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `for` loop statement. This method handles the
  initialization, condition, and update expressions of the `for` loop,
  as well as the body of the loop.

**Parameters:** None

**Returns:**
   - `ForNode`: An AST node representing the `for` loop statement.
   -  This node contains:

      - `init`: The initialization expression or statement (e.g., variable declaration and assignment).
      - `condition`: The condition expression that controls the loop’s continuation.
      - `update`: The update expression executed after each iteration of the loop.
      - `body`: The block of statements executed in each iteration of the loop.


**Raises:**
   - `SyntaxError`: If there are issues with the syntax of the `for` statement or problems parsing the expressions or block.

parse_return_statement(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `return` statement. This method retrieves the expression
  that is returned from a function and ensures proper syntax with a
  terminating semicolon.

| **Parameters:** None

**Returns:**
   - `ReturnNode`: An AST node representing the `return` statement.This node contains: - `value`: The expression to be returned by the function.

**Raises:**
   - `SyntaxError`: If there are issues with the syntax of the `return` statement or problems parsing the expression.

parse_expression_statement(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an expression statement. This method handles any general
  expressions followed by a semicolon, treating them as statements.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed expression, which can be any type of expression node (e.g., `BinaryOpNode`, `FunctionCallNode`, etc.).

**Raises:**
   - `SyntaxError`: If there are issues with the syntax of the expression or if the semicolon is missing.

parse_expression(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an expression by delegating to the `parse_assignment` method.
  This method serves as the entry point for parsing expressions,
  handling the overall expression parsing process.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed assignment expression or any other expression node resulting from the `parse_assignment` method.

**Raises:**
   - `SyntaxError`: If there are issues with the syntax of the assignment or any sub-expressions.

parse_assignment(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an assignment expression. This method first parses the
  left-hand side of the assignment using `parse_logical_or()`. It then
  checks for assignment operators (`EQUALS`, `PLUS_EQUALS`,
  `MINUS_EQUALS`, `MULTIPLY_EQUALS`, `DIVIDE_EQUALS`) and parses
  the right-hand side expression. Additionally, it handles ternary
  conditional expressions if a `QUESTION` token is encountered.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed assignment expression, which could be an `AssignmentNode` or a `TernaryOpNode` depending on the presence of conditional operators.

**Raises:**
   - `SyntaxError`: If there are issues with the syntax of the assignment or ternary expressions.

parse_logical_or(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a logical OR expression. This method first parses the left-hand
  side of the expression using `parse_logical_and()`. It then
  processes any subsequent logical OR operators, parsing the right-hand
  side of each OR operation and combining the results into a
  `BinaryOpNode` representing the logical OR operation.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed logical OR expression, which is represented as a `BinaryOpNode` if there are multiple OR operations, or a single expression if there is no OR operation.

**Raises:**
   - `SyntaxError`: If the syntax of the logical OR expression is invalid.

parse_logical_and(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a logical AND expression. This method first parses the
  left-hand side of the expression using `parse_equality()`. It then
  processes any subsequent logical AND operators, parsing the right-hand
  side of each AND operation and combining the results into a
  `BinaryOpNode` representing the logical AND operation.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed logical AND expression, which is represented as a `BinaryOpNode` if there are multiple AND operations, or a single expression if there is no AND operation.

**Raises:**
   - `SyntaxError`: If the syntax of the logical AND expression is invalid.

parse_equality(self)
~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an equality expression. This method starts by parsing the
  left-hand side of the expression using `parse_relational()`. It then
  processes any subsequent equality or inequality operators (`==` or
  `!=`), parsing the right-hand side of each operation and combining
  the results into a `BinaryOpNode` representing the equality or
  inequality operation.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed equality expression, represented as a `BinaryOpNode` if there are multiple equality operations, or a single expression if there are no equality operations.

**Raises:**
   - `SyntaxError`: If the syntax of the equality expression is invalid.

parse_relational(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a relational expression. This method begins by parsing the
  left-hand side of the relational expression using
  `parse_additive()`. It then processes any relational operators
  (`<`, `>`, `<=`, `>=`), parsing the right-hand side of each
  operation and combining the results into a `BinaryOpNode`
  representing the relational operation.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed relational expression, represented as a `BinaryOpNode` if there are multiple relational operations, or a single expression if there are no relational operations.

**Raises:**
   - `SyntaxError`: If the syntax of the relational expression is invalid.

parse_additive(self)
~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an additive expression. This method starts by parsing the
  left-hand side of the expression using `parse_multiplicative()`. It
  then processes any additive operators (`+`, `-`), parsing the
  right-hand side of each operation and combining the results into a
  `BinaryOpNode` representing the additive operation.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed additive expression, represented as a `BinaryOpNode` if there are multiple additive operations, or a single expression if there are no additive operations.

**Raises:**
   - `SyntaxError`: If the syntax of the additive expression is invalid.

parse_multiplicative(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a multiplicative expression. This method starts by parsing the
  left-hand side of the expression using `parse_unary()`. It then
  processes any multiplicative operators (`*`, `/`), parsing the
  right-hand side of each operation and combining the results into a
  `BinaryOpNode` representing the multiplicative operation.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed multiplicative expression, represented as a `BinaryOpNode` if there are multiple multiplicative operations, or a single expression if there are no multiplicative operations.

**Raises:**
   - `SyntaxError`: If the syntax of the multiplicative expression is invalid.

parse_unary(self)
~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a unary expression. This method handles unary operators such as
  `+` and `-`, applying these operators to the result of a recursive
  call to `parse_unary()`. If no unary operator is present, it
  delegates to `parse_primary()` to handle the primary expression.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed unary expression, represented as a `UnaryOpNode` if a unary operator is present, or a primary expression if no unary operator is found.

**Raises:**
   - `SyntaxError`: If the syntax of the unary expression is invalid.

parse_primary(self)
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a primary expression, which includes literals, variables,
  function calls, or expressions inside parentheses.

| **Parameters:** None

**Returns:**
   - `ASTNode`: The parsed primary expression, such as a `VariableNode`, a constructor call, a literal value, or an expression inside parentheses.

**Raises:**
   - `SyntaxError`: If an unexpected token is encountered in the expression.

parse_vector_constructor(self, type_name)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a vector constructor expression. This includes the opening
  parenthesis, a list of expressions separated by commas, and the
  closing parenthesis.

**Parameters:**
   - `type_name` (str): The type of the vector being constructed (e.g., `vec2`, `vec3`, `vec4`).

**Returns:**
   - `VectorConstructorNode`: A node representing the vector constructor, which includes the vector type and its arguments.

**Raises:**
   - `SyntaxError`: If an unexpected token is encountered (though this specific case is not directly handled in this method).

parse_function_call_or_identifier(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses either a function call or a member access based on the current
  token. If the token indicates a function call, it processes that;
  otherwise, it handles member access or just returns a variable node.

**Returns:**

- **Function Call:** If `LPAREN` is the next token after the identifier.

  - `FunctionCallNode`: Represents a function call with its name and arguments.
- **Member Access:** If `DOT` follows the identifier.

  - `MemberAccessNode`: Represents accessing a member of a variable.
- **Variable Node:** If no additional tokens are present.

  - `VariableNode`: Represents a simple variable.


parse_function_call(self, name)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a function call with the given function name and its arguments.
  The arguments are collected until the closing parenthesis is
  encountered.

**Returns:**
   - `FunctionCallNode`: Represents a function call with its name and arguments.

parse_member_access(self, object)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses member access expressions. It handles cases where members are
  accessed with dot notation, including nested member accesses.

**Returns:**
   - `MemberAccessNode`: Represents the member access expression with the object and the member. If there are nested member accesses, the function will recursively parse them.

parse_texture_sample(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Purpose:**
| Parses a texture sampling operation, which typically involves calling
  a `sample` method on a texture with specified parameters.

**Return:** - Returns a `TextureSampleNode` with the texture,
sampler, and coordinates.

.. _metal-codegen-1:

Metal Codegen
-------------

Methods

__init__(self)

Initializes the code generator.

generate(self, ast)
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates shader code from the abstract syntax tree (AST). This method
  processes the structs, custom functions, vertex shader, and fragment
  shader sections to produce the final shader code.

**Parameters:**
   - `ast` (AST): The abstract syntax tree representing the shader code, including functions and other relevant structures.

**Returns:**
   - `str`: The generated shader code as a string, including vertex and fragment shader sections.

**Raises:**
   - `ValueError`: If no vertex or fragment functions are found in the AST when generating shader sections.

process_structs(self, ast)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Processes struct definitions in the abstract syntax tree (AST) to
  categorize and map vertex and fragment input/output variables. This
  method updates the lists of vertex and fragment inputs and outputs
  based on the struct definitions.

**Parameters:**
   - `ast` (AST): The abstract syntax tree representing the shader code, including function and struct definitions.

**Returns:** `None`

**Raises:**
   - `KeyError`: If a struct with an unexpected name is encountered (though this specific case is not directly handled in this method).

generate_io_declarations(self, shader_type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates input and output declarations for vertex or fragment shaders
  based on the shader type. This method formats the declarations
  according to the shader type and the lists of vertex and fragment
  inputs and outputs.

**Parameters:**
   - `shader_type` (str): The type of shader for which to generate declarations (`"vertex"` or `"fragment"`).

**Returns:**
   - `str`: A string containing the formatted input and output declarations for the specified shader type.

**Raises:**
   - `ValueError`: If an invalid `shader_type` is provided (though this specific case is not directly handled in this method).

generate_function(self, func)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates the code for a function, including its signature and body.
  It formats the function declaration and populates it with the
  function’s parameters and return type.

**Parameters:**
   - `func` (FunctionNode): The function node representing the function to generate code for, including its return type, name, parameters, and body.

**Returns:**
   - `str`: A string containing the formatted function declaration and body.

**Raises:**
   - `TypeError`: If the `func` parameter is not an instance of `FunctionNode` (though this specific case is not directly handled in this method).

generate_main_function(self, func)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates the `main` function code, including its body. It formats
  the `main` function with appropriate indentation and generates the
  function body.

**Parameters:**
   - `func` (FunctionNode): The function node representing the `main` function to generate code for, including its body.

**Returns:**
   - `str`: A string containing the formatted `main` function with its body.

**Raises:**
   - `TypeError`: If the `func` parameter is not an instance of `FunctionNode` (though this specific case is not directly handled in this method).

generate_function_body(self, body, indent=0, is_main=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates the body of a function, including variable declarations,
  assignments, return statements, and control flow statements. It
  handles different types of statements and formats them with
  appropriate indentation.

**Parameters:**

- `body` (list): A list of statements and expressions to include in the function body.
- `indent` (int, optional): The level of indentation for formatting the code (default is 0).
- `is_main` (bool, optional): A flag indicating if the function is the `main` function, affecting how certain statements are handled (default is False).


**Returns:**
   - `str`: A string containing the formatted code for the function body.

**Raises:**
   - `TypeError`: If any item in the `body` list is not an instance of an expected node type (though this specific case is not directly handled in this method).

generate_for_loop(self, node, indent, is_main)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates the code for a `for` loop statement, including its
  initialization, condition, update expression, and body. It handles
  formatting and indentation for the loop structure.

**Parameters:**

- `node` (ForNode): The `ForNode` instance representing the `for` loop, including initialization, condition, update, and body.
- `indent` (int): The level of indentation for formatting the code.
- `is_main` (bool): A flag indicating if the function is the `main` function, affecting how certain statements are handled.


**Returns:**
   - `str`: A string containing the formatted code for the `for` loop.

**Raises:**
   - `TypeError`: If `node` is not an instance of `ForNode`, though this specific case is not directly handled in this method.

generate_if_statement(self, node, indent, is_main)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates the code for an `if` statement, including the condition,
  the `if` body, and the optional `else` body. Handles formatting
  and indentation for the `if` structure.

**Parameters:**

- `node` (IfNode): The `IfNode` instance representing the `if` statement, including its condition, `if` body, and optional `else` body.
- `indent` (int): The level of indentation for formatting the code.
- `is_main` (bool): A flag indicating if the function is the `main` function, affecting how certain statements are handled.


**Returns:**
   - `str`: A string containing the formatted code for the `if` statement.

**Raises:**
   - `TypeError`: If `node` is not an instance of `IfNode`, though this specific case is not directly handled in this method.

generate_assignment(self, node, is_main)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates the code for an assignment statement, handling special cases
  for assignments to output positions and general assignments. Formats
  the assignment based on whether it is in the `main` function.

**Parameters:**

- `node` (AssignmentNode): The `AssignmentNode` instance representing the assignment, including the left-hand side (LHS) and right-hand side (RHS) expressions.
- `is_main` (bool): A flag indicating if the function is the `main` function, which affects how certain assignments are formatted.


**Returns:**
   - `str`: A string containing the formatted code for the assignment statement.

**Raises:**
   - `TypeError`: If `node` is not an instance of `AssignmentNode`, though this specific case is not directly handled in this method.

generate_expression(self, expr, is_main=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Generates code for an expression, handling various types of AST nodes
  including variables, assignments, binary operations, function calls,
  member access, unary operations, ternary operations, and vector
  constructors.

**Parameters:**

- `expr` (ASTNode): The AST node representing the expression to be converted to code. This can be a `VariableNode`, `AssignmentNode`, `BinaryOpNode`, `FunctionCallNode`, `MemberAccessNode`, `UnaryOpNode`, `TernaryOpNode`, or `VectorConstructorNode`.
- `is_main` (bool, optional): A flag indicating if the expression is within the `main` function, affecting how some expressions are formatted. Defaults to `False`.


**Returns:**
   - `str`: A string containing the generated code for the expression.

**Raises:**
   - `TypeError`: If `expr` is not an instance of a recognized AST node class or a string.

map_type(self, metal_type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Maps a type from the internal representation (e.g., Metal shading
  language types) to the corresponding type in the target language.

**Parameters:**
   - `metal_type` (str): The type in the internal representation that needs to be mapped to the target language type.

**Returns:**
   - `str`: The corresponding type in the target language based on the `type_map`. If `metal_type` is not found in `type_map`, it returns the `metal_type` itself.

**Raises:** `None`

OpenGL
------

OpenGL AST
~~~~~~~~~~

UniformNode
~~~~~~~~~~~~~~~~

Represents a uniform variable in a shader program.

- **Description**: This class represents a uniform variable used to pass data from the application to the shader. It stores the type and name of the uniform and provides methods to return its string representation.

- **Attributes**:
   - `vtype (str)`: The data type of the uniform variable (e.g., `float`, `vec3`).
   - `name (str)`: The name of the uniform variable.

- **Returns**:
   - `UniformNode`: An object representing the uniform variable, with methods to generate its shader code representation.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `UniformNode` instance, suitable for debugging.
   - `__str__() -> str`: Returns the uniform declaration in the shader code as a string.

- **Raises**:
   - `None`: This class does not raise exceptions.


ConstantNode
~~~~~~~~~~~~~~~~

Represents a constant value used in shader code.

- **Description**: This class encapsulates a constant value in shader code, such as a number, boolean, or any fixed data type. It provides methods to return its string representation.

- **Attributes**:
   - `value (any)`: The constant value to be represented (e.g., `42`, `3.14`, `true`).

- **Returns**:
   - `ConstantNode`: An object representing the constant value, with methods to generate its string representation.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `ConstantNode` instance, suitable for debugging.
   - `__str__() -> str`: Returns the string representation of the constant value.

- **Raises**:
   - `None`: This class does not raise exceptions.


VersionDirectiveNode
~~~~~~~~~~~~~~~~~~~~

Represents a GLSL version directive in shader code.

- **Description**: This class encapsulates a GLSL version directive, which specifies the GLSL version and profile being used in the shader code.

- **Attributes**:
   - `number (str)`: The version number of GLSL (e.g., `450`).
   - `profile (str)`: The profile of GLSL (e.g., `core`, `compatibility`).

- **Returns**:
   - `VersionDirectiveNode`: An object representing the GLSL version directive, with methods to generate its string representation.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `VersionDirectiveNode` instance, suitable for debugging.
   - `__str__() -> str`: Returns the GLSL version directive as a string.

- **Raises**:
   - `None`: This class does not raise exceptions.


LayoutNode
~~~~~~~~~~~~~~~~

Represents a GLSL layout qualifier for shader variables.

- **Description**: This class encapsulates a GLSL layout qualifier, specifying the location and type of shader variables. It supports variables in different sections of the shader code.

- **Attributes**:
   - `location_number (int)`: The location number of the shader variable (e.g., `0`, `1`).
   - `dtype (str)`: The data type of the shader variable (e.g., `vec4`, `float`).
   - `name (str)`: The name of the shader variable.

- **Returns**:
   - `LayoutNode`: An object representing the GLSL layout qualifier, with methods to generate its string representation.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `LayoutNode` instance, suitable for debugging.
   - `__str__() -> str`: Returns the GLSL layout qualifier as a string.

- **Raises**:
   - `None`: This class does not raise exceptions.


TernaryOpNode
~~~~~~~~~~~~~~~~

Represents a ternary conditional expression in shader code.

- **Description**: This class encapsulates a ternary conditional expression, which is used for conditional operations in shader code. It stores the condition, true expression, and false expression.

- **Attributes**:
   - `condition (ASTNode)`: The condition expression that evaluates to either `true` or `false`.
   - `true_expr (ASTNode)`: The expression to evaluate and return if the condition is `true`.
   - `false_expr (ASTNode)`: The expression to evaluate and return if the condition is `false`.

- **Returns**:
   - `TernaryOpNode`: An object representing the ternary operation, with methods to generate its string representation.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `TernaryOpNode` instance, including the condition, true expression, and false expression.

- **Raises**:
   - `None`: This class does not raise exceptions.


ShaderNode
~~~~~~~~~~~~~~~~

Represents a shader program, encapsulating all its components.

- **Description**: This class represents a complete shader program, including the version, input and output variables, uniforms, and the vertex and fragment shader sections.

- **Attributes**:
   - `version (str)``: The version of the shader language used.
   - `global_inputs (list of LayoutNode)`: A list of layout nodes specifying global input variables.
   - `global_outputs (list of LayoutNode)`: A list of layout nodes specifying global output variables.
   - `uniforms (list of UniformNode)`: A list of uniform variables used in the shader.
   - `vertex_section (list of ASTNode)`: A list of AST nodes representing the vertex shader section.
   - `fragment_section (list of ASTNode)`: A list of AST nodes representing the fragment shader section.
   - `functions (list of FunctionNode)`: A list of function nodes defined in the shader.

- **Returns**:
   - `ShaderNode`: An object representing the entire shader program, with methods to generate its string representation.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `ShaderNode` instance, showing its version, global inputs, global outputs, functions, vertex section, and fragment section.

- **Raises**:
   - `None`: This class does not raise exceptions.

.. _vertexshadernode-class-1:

VERTEXShaderNode
~~~~~~~~~~~~~~~~

Represents the vertex shader section of a shader program, including input and output variables, uniform variables, functions, and layout qualifiers.

- **Description**: This class represents the vertex shader portion of a shader program, encapsulating its inputs, outputs, uniforms, and any associated functions or layout qualifiers.

- **Attributes**:
   - `inputs (list of LayoutNode)`: A list of input variables for the vertex shader.
   - `outputs (list of LayoutNode)`: A list of output variables for the vertex shader.
   - `uniform (list of UniformNode)`: A list of uniform variables used in the vertex shader.
   - `functions (list of FunctionNode)`: A list of functions defined in the vertex shader.
   - `layout_qualifiers (list of LayoutNode, optional)`: A list of layout qualifiers specifying additional layout information.

- **Returns**:
   - `VERTEXShaderNode`: An object representing the vertex shader section, with attributes and methods to manipulate its components.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `VERTEXShaderNode` instance, including its inputs, outputs, uniform variables, functions, and layout qualifiers.

- **Raises**:
   - `None`: This class does not raise exceptions.

.. _fragmentshadernode-class:

FRAGMENTShaderNode
~~~~~~~~~~~~~~~~~~

Represents the fragment shader section of a shader program, including input and output variables, uniform variables, functions, and layout qualifiers.

- **Description**: This class represents the fragment shader portion of a shader program, encapsulating its inputs, outputs, uniforms, and any associated functions or layout qualifiers.

- **Attributes**:
   - `inputs (list of LayoutNode)`: A list of input variables for the fragment shader.
   - `outputs (list of LayoutNode)`: A list of output variables for the fragment shader.
   - `uniform (list of UniformNode)`: A list of uniform variables used in the fragment shader.
   - `functions (list of FunctionNode)`: A list of functions defined in the fragment shader.
   - `layout_qualifiers (list of LayoutNode, optional)`: A list of layout qualifiers specifying additional layout information.

- **Returns**:
   - `FRAGMENTShaderNode`: An object representing the fragment shader section, with attributes and methods to manipulate its components.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `FRAGMENTShaderNode` instance, including its inputs, outputs, uniform variables, functions, and layout qualifiers.

- **Raises**:
   - `None`: This class does not raise exceptions.

.. _functionnode-class:

FunctionNode
~~~~~~~~~~~~

Represents a function definition within a shader or programming language.

- **Description**: This class encapsulates a function's return type, name, parameters, and body within a shader or programming language context.

- **Attributes**:
   - `return_type (str)`: The return type of the function (e.g., `void`, `float`, `vec4`).
   - `name (str)`: The name of the function.
   - `params (list of VariableNode)`: A list of parameters for the function, where each parameter is represented as a `VariableNode`.
   - `body (list of ASTNode)`: A list of statements or expressions representing the function body.

- **Returns**:
   - `FunctionNode`: An object representing the function, with attributes and methods to manipulate its components.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `FunctionNode` instance, including its return type, name, parameters, and body.

- **Raises**:
   - `None`: This class does not raise exceptions.

.. _variablenode-class:

VariableNode
~~~~~~~~~~~~

Represents a variable within a shader or programming language.

- **Description**: This class encapsulates the type of a variable and its name within a shader or programming language context.

- **Attributes**:
   - `vtype (str)`: The type of the variable (e.g., `int`, `float`, `vec3`).
   - `name (str)`: The name of the variable.

- **Returns**:
   - `VariableNode`: An object representing the variable, with attributes and methods to manipulate its components.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `VariableNode` instance, including its type and name.

- **Raises**:
   - `None`: This class does not raise exceptions.

.. _assignmentnode-class:

AssignmentNode
~~~~~~~~~~~~~~

Represents an assignment operation within a shader or programming language.

- **Description**: This class encapsulates an assignment operation, including the variable name being assigned and the value assigned to it.

- **Attributes**:
   - `name (str)`: The name of the variable being assigned.
   - `value (any)`: The value assigned to the variable.

- **Returns**:
   - `AssignmentNode`: An object representing the assignment operation, with attributes and methods to manipulate its components.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `AssignmentNode` instance, including the variable name and the assigned value.

- **Raises**:
   - `None`: This class does not raise exceptions.

.. _ifnode-class:

IfNode
~~~~~~

Represents an if-else conditional structure within a shader or programming language.

- **Description**: This class encapsulates an if-else conditional structure, including the condition, the body of the if statement, optional else-if chains, and an optional else body.

- **Attributes**:
   - `condition (ASTNode)`: The condition to evaluate.
   - `if_body (list of ASTNode)`: The body of the if statement.
   - `else_if_chain (list of tuple, optional)`: A list of tuples, each containing a condition and a body for else-if statements.
   - `else_body (list of ASTNode, optional)`: The body of the else statement.

- **Returns**:
   - `IfNode`: An object representing the if-else structure, with attributes and methods to manipulate its components.

- **Methods**:
   - `__repr__() -> str`: Returns a string representation of the `IfNode` instance, including its condition, if body, else-if chain, and else body.

- **Raises**:
   - `None`: This class does not raise exceptions.

.. _fornode-class-1:

ForNode Class
~~~~~~~~~~~~~~~~~

- **Description:** Represents a for-loop structure within a shader or programming language. It includes the initialization, condition, update, and the body of the loop.

- **Constructor Parameters:**
   - `init` (ASTNode): The initialization statement of the for-loop.
   - `condition` (ASTNode): The condition to evaluate for each iteration.
   - `update` (ASTNode): The update statement executed after each iteration.
   - `body` (list of ASTNode): The body of the for-loop.

- **Attributes:**
   - `init` (ASTNode): The initialization statement.
   - `condition` (ASTNode): The condition to evaluate.
   - `update` (ASTNode): The update statement.
   - `body` (list of ASTNode): The body of the for-loop.

- **Methods:**
   - `__repr__() -> str`: Returns a string representation of the `ForNode` instance, including its initialization, condition, update, and body.

ReturnNode Class
~~~~~~~~~~~~~~~~~~~~

- **Description:** Represents a return statement within a shader or programming language. It includes the value to be returned.

- **Constructor Parameters:**
   - `value` (any): The value to be returned by the return statement.

- **Attributes:**
   - `value` (any): The value to be returned.

- **Methods:**
   - `__repr__() -> str`: Returns a string representation of the `ReturnNode` instance, including the value to be returned.

FunctionCallNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Description:** Represents a function call within a shader or programming language. It includes the function name and the arguments passed to the function.

- **Constructor Parameters:**
   - `name` (str): The name of the function being called.
   - `args` (list of ASTNode): A list of arguments passed to the function.

- **Attributes:**
   - `name` (str): The name of the function.
   - `args` (list of ASTNode): The arguments passed to the function.

- **Methods:**
   - `__repr__() -> str`: Returns a string representation of the `FunctionCallNode` instance, including the function name and arguments.

BinaryOpNode Class
~~~~~~~~~~~~~~~~~~~~~~

- **Description:** Represents a binary operation within a shader or programming language. It includes the left operand, the operator, and the right operand.

- **Constructor Parameters:**
   - `left` (ASTNode): The left operand of the binary operation.
   - `op` (str): The operator of the binary operation (e.g., `+`, `-`, `*`, `/`).
   - `right` (ASTNode): The right operand of the binary operation.

- **Attributes:**
   - `left` (ASTNode): The left operand.
   - `op` (str): The operator.
   - `right` (ASTNode): The right operand.

- **Methods:**
   - `__repr__() -> str`: Returns a string representation of the `BinaryOpNode` instance, including the left operand, operator, and right operand.

MemberAccessNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Description:** Represents member access within a shader or programming language. It includes the object and the member being accessed.

- **Constructor Parameters:**
   - `object` (ASTNode): The object whose member is being accessed.
   - `member` (str): The member being accessed.

- **Attributes:**
   - `object` (ASTNode): The object.
   - `member` (str): The member being accessed.

- **Methods:**
   - `__repr__() -> str`: Returns a string representation of the `MemberAccessNode` instance, including the object and the member being accessed.

UnaryOpNode Class
~~~~~~~~~~~~~~~~~~~~~

- **Description:** Represents a unary operation within a shader or programming language. It includes the operator and the operand.

- **Constructor Parameters:**
   - `op` (str): The operator of the unary operation (e.g., `-`, `!`, `~`).
   - `operand` (ASTNode): The operand of the unary operation.

- **Attributes:**
   - `op` (str): The operator.
   - `operand` (ASTNode): The operand.

- **Methods:**
   - `__repr__() -> str`: Returns a string representation of the `UnaryOpNode` instance, including the operator and operand.
   - `__str__() -> str`: Returns a string representation of the unary operation in the format `(operator operand)`.

OpenGL Lexer
------------

.. _tokens-list-1:

TOKENS List
~~~~~~~~~~~~~~~

| **Description:**
| Defines a list of tuples representing different types of tokens used
  in a shader or programming language. Each tuple contains a token name
  and its corresponding regular expression pattern.

| **Tokens:**

- ``COMMENT_SINGLE``: Matches single-line comments starting with ``//``.
- ``COMMENT_MULTI``: Matches multi-line comments enclosed by ``/* ... */``.
- ``ELSE_IF``: Matches ``else if`` statements.
- ``VERSION``: Matches version directives starting with ``#version``.
- ``NUMBER``: Matches numeric literals (e.g., ``123``, ``123.45``).
- ``CORE``: Matches the keyword ``core``.
- ``SHADER``: Matches the keyword ``shader``.
- ``INPUT``: Matches the keyword ``input``.
- ``OUTPUT``: Matches the keyword ``output``.
- ``VOID``: Matches the keyword ``void``.
- ``MAIN``: Matches the ``main`` function.
- ``UNIFORM``: Matches the keyword ``uniform``.
- ``VECTOR``: Matches vector types (e.g., ``vec2``, ``vec3``, ``vec4``).
- ``MATRIX``: Matches matrix types (e.g., ``mat2``, ``mat3``, ``mat4``).
- ``BOOL``: Matches the keyword ``bool``.
- ``FLOAT``: Matches the keyword ``float``.
- ``INT``: Matches the keyword ``int``.
- ``SAMPLER2D``: Matches the keyword ``sampler2D``.
- ``PRE_INCREMENT``: Matches the pre-increment operator ``++`` when followed by a word character.
- ``PRE_DECREMENT``: Matches the pre-decrement operator ``--`` when followed by a word character.
- ``POST_INCREMENT``: Matches the post-increment operator ``++`` when preceded by a word character.
- ``POST_DECREMENT``: Matches the post-decrement operator ``--`` when preceded by a word character.
- ``IDENTIFIER``: Matches identifiers (e.g., variable names, function names) using the pattern ``[a-zA-Z_][a-zA-Z_0-9]*``.
- ``LBRACE``: Matches the left brace ``{``.
- ``RBRACE``: Matches the right brace ``}``.
- ``LPAREN``: Matches the left parenthesis ``(``.
- ``RPAREN``: Matches the right parenthesis ``)``.
- ``SEMICOLON``: Matches the semicolon ``;``.
- ``COMMA``: Matches the comma ``,``.
- ``ASSIGN_ADD``: Matches the addition assignment operator ``+=``.
- ``ASSIGN_SUB``: Matches the subtraction assignment operator ``-=``.
- ``ASSIGN_MUL``: Matches the multiplication assignment operator ``*=``.
- ``ASSIGN_DIV``: Matches the division assignment operator ``/=``.
- ``EQUAL``: Matches the equality operator ``==``.
- ``NOT_EQUAL``: Matches the inequality operator ``!=``.
- ``WHITESPACE``: Matches whitespace characters.
- ``IF``: Matches the keyword ``if``.
- ``ELSE``: Matches the keyword ``else``.
- ``FOR``: Matches the keyword ``for``.
- ``RETURN``: Matches the keyword ``return``.
- ``LESS_EQUAL``: Matches the less than or equal to operator ``<=``.
- ``GREATER_EQUAL``: Matches the greater than or equal to operator ``>=``.
- ``LESS_THAN``: Matches the less than operator ``<``.
- ``GREATER_THAN``: Matches the greater than operator ``>``.
- ``AND``: Matches the logical AND operator ``&&``.
- ``OR``: Matches the logical OR operator ``||``.
- ``NOT``: Matches the logical NOT operator ``!``.
- ``PLUS``: Matches the addition operator ``+``.
- ``MINUS``: Matches the subtraction operator ``-``.
- ``MULTIPLY``: Matches the multiplication operator ``*``.
- ``DIVIDE``: Matches the division operator ``/``.
- ``DOT``: Matches the dot operator ``.``.
- ``EQUALS``: Matches the assignment operator ``=``.
- ``QUESTION``: Matches the ternary conditional operator ``?``.
- ``COLON``: Matches the colon ``:``.
- ``LAYOUT``: Matches the keyword ``layout``.
- ``IN``: Matches the keyword ``in``.
- ``OUT``: Matches the keyword ``out``.

.. _keywords-dictionary-2:

KEYWORDS Dictionary
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Defines a dictionary mapping specific keywords to their corresponding
  token names.

| **Keywords:**

- ``"void"``: ``VOID``
- ``"main"``: ``MAIN``
- ``"vertex"``: ``VERTEX``
- ``"fragment"``: ``FRAGMENT``
- ``"else if"``: ``ELSE_IF``
- ``"if"``: ``IF``
- ``"else"``: ``ELSE``
- ``"for"``: ``FOR``
- ``"return"``: ``RETURN``
- ``"layout"``: ``LAYOUT``
- ``"in"``: ``IN``
- ``"out"``: ``OUT``


Methods

__init__(self)

Initializes the code generator.

Tokenize Method
~~~~~~~~~~~~~~~~~~~

| **Description:**
| Tokenizes the input code by matching it against predefined token
  patterns and appending the tokens to the `self.tokens` list. It
  handles identifiers, keywords, version directives, and ignores
  whitespace. If an illegal character is encountered, it raises a
  `SyntaxError`.

**Parameters:**
   - `self`: The instance of the class containing the code to be tokenized.

**Attributes:**
   - `self.code` (str): The code to be tokenized. - `self.tokens` (list of tuple): The list of tokens generated from the code.

| **Method Details:**

- tokenize(self):

  - Initializes the position `pos` to 0.
  - Iterates through the code, matching it against token patterns.
  - Appends matched tokens to `self.tokens`.
  - Handles special cases for identifiers and keywords.
  - Ignores whitespace tokens.
  - Raises a `SyntaxError` for illegal characters.
  - Appends an `EOF` token at the end.


OpenGL Parser
-------------

Methods

__init__(self)

Initializes the code generator.

skip_comments Method
~~~~~~~~~~~~~~~~~~~~

**Description**:
    Skips over multi-line comments in the code by consuming tokens until
    the end of the comment is reached.

**Parameters**:
    - `self`: The instance of the class containing the code and tokens.

**Method Details**:

- `skip_comments(self)`:
    - Continues to consume tokens while the current token type is `"COMMENT_MULTI"`.
    - Uses the `eat` method to consume the current token.


eat Method
~~~~~~~~~~

**Description**:
    Consumes the current token if it matches the expected token type and
    advances to the next token. If the token does not match, it raises a
    `SyntaxError`. It also skips comments after consuming a token.

**Parameters**:
    - `self`: The instance of the class containing the tokens.
    - `token_type` (str): The expected type of the current token.

**Method Details**:

- `eat(self, token_type)`:
    - Checks if the current token type matches the expected `token_type`.
    - If it matches, increments the position `pos` and updates `current_token` to the next token.
    - Calls `skip_comments()` to skip any comments after consuming a token.
    - If it does not match, raises a `SyntaxError` with a message indicating the expected and actual token types.


parse Method
~~~~~~~~~~~~

**Description**:
    Parses the input code, handling comments, version directives, and
    shader definitions. It returns the root node of the parsed shader.

**Parameters**:
    - `self`: The instance of the class containing the code and tokens.

**Method Details**:

- `parse(self)`:
    - Calls `skip_comments()` to skip any comments at the beginning.
    - Parses the version directive using `parse_version_directive()` and stores the result in `version_node`.
    - Parses the shader using `parse_shader(version_node)` and stores the result in `shader_node`.
    - Returns `shader_node` as the root node of the parsed shader.


parse_version_directive Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**:
    Parses the version directive from the input tokens. It handles the
    `VERSION` token followed by a `NUMBER` token and optionally a
    `CORE` token.

**Parameters**:
    - `self`: The instance of the class containing the code and tokens.

**Method Details**:

- `parse_version_directive(self)`:
    - Checks if the current token is `VERSION`.
    - If true, consumes the `VERSION` token.
    - Checks if the next token is `NUMBER`.
    - If true, stores the number and consumes the `NUMBER` token.
    - Optionally checks for a `CORE` token and consumes it if present.
    - Returns a `VersionDirectiveNode` with the parsed number and optional version identifier.
    - Raises a `SyntaxError` if the expected tokens are not found.


parse_layout Method
~~~~~~~~~~~~~~~~~~~~

**Description**:
    Parses the layout directive from the input tokens. It handles the
    `LAYOUT` token followed by a `location` identifier and its
    associated number, and then processes either an `IN` or `OUT`
    token to determine the input/output type.

**Parameters**:
    - `self`: The instance of the class containing the code and tokens.
    - `current_section`: The current section being parsed.

**Method Details**:

- `parse_layout(self, current_section)`:
    - Consumes the `LAYOUT` and `LPAREN` tokens.
    - Checks for the `location` identifier and consumes the `IDENTIFIER`, `EQUALS`, and `NUMBER` tokens.
    - Consumes the `RPAREN` token and skips any comments.
    - Checks for `IN` or `OUT` tokens to determine the input/output type.
    - If `IN`, consumes the `IN` token, parses the type, and consumes the `IDENTIFIER` and `SEMICOLON` tokens.
    - If `OUT`, consumes the `OUT` token, parses the type, and consumes the `IDENTIFIER` and `SEMICOLON` tokens.
    - Returns a `LayoutNode` with the parsed section, location number, data type, name, and input/output type.
    - Raises a `SyntaxError` if the expected tokens are not found.


parse_shader Method
~~~~~~~~~~~~~~~~~~~~

**Description**:
    Parses the shader code, handling global inputs, outputs, uniforms, and
    specific sections for vertex and fragment shaders.

**Parameters**:
    - `self`: The instance of the class containing the code and tokens.
    - `version_node`: The node representing the version directive.

**Method Details**:

- `parse_shader(self, version_node)`:
    - Initializes lists for global inputs, outputs, and uniforms.
    - Creates empty `VERTEXShaderNode` and `FRAGMENTShaderNode` instances.
    - Sets `current_section` to `None`.
    - Iterates through tokens until `EOF` is reached:
        - Handles single-line comments to determine the current section (`VERTEX` or `FRAGMENT`).
        - Parses layout directives and appends them to the appropriate section.
        - Parses inputs and appends them to the appropriate section or global list.
        - Parses outputs and appends them to the appropriate section or global list.
        - Parses uniforms and appends them to the global list.
        - Parses version directives.
        - Parses functions and appends them to the appropriate section.
        - Handles braces to parse shader sections and appends content to the appropriate section.
    - Raises `SyntaxError` for unexpected tokens or misplaced functions and braces.


parse_shader_section Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**:
    Parses a section of the shader code, handling inputs, outputs,
    uniforms, functions, and layout qualifiers within braces.

**Parameters**:
    - `self`: The instance of the class containing the code and tokens.
    - `current_section`: The current section being parsed.

**Method Details**:

- `parse_shader_section(self, current_section)`:
    - Initializes lists for inputs, outputs, uniforms, functions, and layout qualifiers.
    - Consumes the `LBRACE` token.
    - Iterates through tokens until `RBRACE` or `EOF` is reached:
        - Parses layout directives and appends them to `layout_qualifiers`.
        - Parses inputs and appends them to `inputs`.
        - Parses outputs and appends them to `outputs`.
        - Parses uniforms and appends them to `uniforms`.
        - Parses functions and appends them to `functions`.
    - Returns a tuple of lists containing inputs, outputs, uniforms, layout qualifiers, and functions when `RBRACE` is encountered.
    - Raises a `SyntaxError` for unexpected tokens or end of input.


parse_inputs Method
~~~~~~~~~~~~~~~~~~~~

**Description**:
    Parses the input variables from the tokens, handling the `IN` token
    followed by the variable type and name.

**Parameters**:
    - `self`: The instance of the class containing the code and tokens.

**Method Details**:

- `parse_inputs(self)`:
    - Initializes an empty list `inputs`.
    - Iterates through tokens while the current token is `IN`:
        - Consumes the `IN` token.
        - Parses the variable type and stores it in `vtype`.
        - Stores the variable name from the current token.
        - Consumes the `IDENTIFIER` and `SEMICOLON` tokens.
        - Appends a tuple `(vtype, name)` to `inputs`.
    - Returns the list `inputs`.


parse_outputs Method
~~~~~~~~~~~~~~~~~~~~

**Description**:
    Parses the output variables from the tokens, handling the `OUT`
    token followed by the variable type and name.

**Parameters**:
    - `self`: The instance of the class containing the code and tokens.

**Method Details**:

- `parse_outputs(self)`:
    - Initializes an empty list `outputs`.
    - Iterates through tokens while the current token is `OUT`:
        - Consumes the `OUT` token.
        - Parses the variable type and stores it in `vtype`.
        - Stores the variable name from the current token.
        - Consumes the `IDENTIFIER` and `SEMICOLON` tokens.
        - Appends a tuple `(vtype, name)` to `outputs`.
    - Returns the list `outputs`.

parse_uniforms Method
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the uniform variables from the tokens, handling the `UNIFORM`
  token followed by the variable type and name.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_uniforms(self)`:

  - Initializes an empty list `uniforms`.
  - Iterates through tokens while the current token is `UNIFORM`:

    - Consumes the `UNIFORM` token.
    - Parses the variable type and stores it in `vtype`.
    - Stores the variable name from the current token.
    - Consumes the `IDENTIFIER` and `SEMICOLON` tokens.
    - Appends a `UniformNode` with `vtype` and `name` to `uniforms`.
  - Returns the list `uniforms`.


parse_variable Method
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a variable declaration or assignment from the tokens, handling
  various forms of assignments and member access.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.
   - `type_name`: The type of the variable being parsed.

| **Method Details:**

- `parse_variable(self, type_name)`:

  - Stores the variable name from the current token and consumes the `IDENTIFIER` token.
  - Handles member access by consuming `DOT` and `IDENTIFIER` tokens, appending to the variable name.
  - If the next token is `SEMICOLON`, consumes it and returns a `VariableNode`.
  - If the next token is `EQUALS`, consumes it, parses the expression, and returns an `AssignmentNode`.
  - If the next token is a compound assignment operator (`ASSIGN_ADD`, `ASSIGN_SUB`, `ASSIGN_MUL`, `ASSIGN_DIV`), consumes it, parses the expression, and returns a `BinaryOpNode`.
  - Raises a `SyntaxError` for unexpected tokens or missing semicolons.


parse_assignment_or_function_call Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an assignment or function call from the tokens, handling
  various types of assignments, increments, decrements, and function
  calls.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_assignment_or_function_call(self)`:

  - Initializes `type_name` as an empty string.
  - Checks if the current token is a type (`VECTOR`, `FLOAT`, `INT`, `MATRIX`):

    - If true, stores the type name and consumes the token.
  - If the current token is `IDENTIFIER`, calls `parse_variable` with `type_name`.

    - Stores the identifier name and consumes the `IDENTIFIER` token.
  - Checks for assignment operators (`EQUALS`, `ASSIGN_ADD`, `ASSIGN_SUB`, `ASSIGN_MUL`, `ASSIGN_DIV`):

    - If true, calls `parse_assignment` with the name.
  - Checks for increment (`PRE_INCREMENT`, `POST_INCREMENT`) or decrement (`PRE_DECREMENT`, `POST_DECREMENT`) operators:

    - If true, consumes the operator and returns an `AssignmentNode` with a `UnaryOpNode`.
  - Checks for a function call (`LPAREN`):

    - If true, calls `parse_function_call` with the name.
  - Raises a `SyntaxError` for unexpected tokens after the identifier.


parse_function Method
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a function definition from the tokens, handling the return
  type, function name, parameters, and body.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_function(self)`:

  - Parses the return type using `parse_type()`.
  - Checks if the current token is `MAIN` or `IDENTIFIER`:

    - If `MAIN`, stores the function name and consumes the `MAIN` token.
    - If `IDENTIFIER`, stores the function name and consumes the `IDENTIFIER` token.
  - Raises a `SyntaxError` if neither `MAIN` nor `IDENTIFIER` is found.
  - Consumes the `LPAREN` token.
  - Parses the parameters using `parse_parameters()`.
  - Consumes the `RPAREN` token.
  - Consumes the `LBRACE` token.
  - Parses the function body using `parse_body()`.
  - Consumes the `RBRACE` token.
  - Returns a `FunctionNode` with the return type, function name, parameters, and body.


parse_body Method
~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the body of a function, handling various statements such as
  `if`, `for`, `return`, and assignments or function calls.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_body(self)`:

  - Initializes an empty list `body`.
  - Iterates through tokens until `RBRACE` or `EOF` is encountered:

    - If the current token is `IF`, parses an `if` statement and appends it to `body`.
    - If the current token is `FOR`, parses a `for` loop and appends it to `body`.
    - If the current token is `RETURN`, parses a `return` statement and appends it to `body`.
    - If the current token is a type or identifier (`VECTOR`, `IDENTIFIER`, `FLOAT`, `INT`), parses an assignment or function call and appends it to `body`.
  - Raises a `SyntaxError` for unexpected tokens.
  - Returns the list `body`.


parse_parameters Method
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the parameters of a function, handling multiple parameters
  separated by commas.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_parameters(self)`:

  - Initializes an empty list `params`.
  - If the current token is not `RPAREN`, parses the first parameter and appends it to `params`.
  - Iterates through tokens while the current token is `COMMA`:
    - Consumes the `COMMA` token.
    - Parses the next parameter and appends it to `params`.
  - Returns the list `params`.


parse_parameter Method
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a single parameter, handling the parameter type and name.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_parameter(self)`:

  - Parses the parameter type using `parse_type()`.
  - Stores the parameter name from the current token.
  - Consumes the `IDENTIFIER` token.
  - Returns a tuple `(param_type, param_name)`.


parse_type Method
~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the type of a variable or function return type from the tokens.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_type(self)`:

  - Checks if the current token is `VOID`:
    - If true, consumes the `VOID` token and returns `"void"`.
  - Checks if the current token is one of the predefined types (`VECTOR`, `FLOAT`, `INT`, `MATRIX`, `BOOLEAN`, `SAMPLER2D`):
    - If true, stores the type name, consumes the token, and returns the type name.
  - Checks if the current token is `IDENTIFIER`:
    - If true, stores the type name, consumes the `IDENTIFIER` token, and returns the type name.
  - Raises a `SyntaxError` for unexpected type tokens.


parse_arguments Method
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the arguments of a function call, handling multiple arguments
  separated by commas.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_arguments(self)`:

  - Initializes an empty list `args`.
  - Iterates through tokens until `RPAREN` is encountered:

    - Parses an expression and appends it to `args`.

    - If the current token is `COMMA`, consumes it.
  - Returns the list `args`.


parse_update Method
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an update statement, handling various forms of increments,
  decrements, and assignments.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

| **Method Details:**

- `parse_update(self)`:

  - If the current token is `IDENTIFIER`:
    - Stores the identifier name and consumes the `IDENTIFIER` token.

    - Checks for `POST_INCREMENT` or `POST_DECREMENT` and returns a `UnaryOpNode`.
    - Checks for assignment operators (`EQUALS`, `ASSIGN_ADD`, `ASSIGN_SUB`, `ASSIGN_MUL`, `ASSIGN_DIV`):
    - Consumes the operator, parses the expression, and returns an `AssignmentNode` or `BinaryOpNode`.
  - If the current token is `PRE_INCREMENT` or `PRE_DECREMENT`:
    - Consumes the operator and the `IDENTIFIER` token, and returns a `UnaryOpNode`.
  - Raises a `SyntaxError` for unexpected tokens or missing identifiers.

parse_assignment Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an assignment statement, handling the variable name, assignment
  operator, and expression.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_assignment(self)`:

  - Stores the variable name from the current token and consumes the `IDENTIFIER` token.

  - Consumes the `EQUALS` token.

  - Parses the expression and stores it in `expr`.

  - Consumes the `SEMICOLON` token.

  - Returns an `AssignmentNode` with the variable name and expression.


parse_function_call_or_identifier Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a function call or an identifier, handling the function name
  and its arguments or member access.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- Checks if the current token is `VECTOR`:
  
  - If true, stores the function name and consumes the `VECTOR` token.
  
  - Otherwise, stores the function name and consumes the `IDENTIFIER` token.

- If the next token is `LPAREN`, calls `parse_function_call` with the function name.

- If the next token is `DOT`, calls `parse_member_access` with the function name.

- Returns a `VariableNode` with the function name if no further tokens are found.


parse_additive Method
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an additive expression, handling addition and subtraction
  operations.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_additive(self)`:

  - Parses the left-hand side of the expression using `parse_multiplicative()`.

  - Iterates through tokens while the current token is `PLUS` or `MINUS`:

    - Stores the operator and consumes the token.

    - Parses the right-hand side of the expression using `parse_multiplicative()`.

  - Creates a `BinaryOpNode` with the left-hand side, operator, and right-hand side.

  - Returns the final `BinaryOpNode`.


parse_primary Method
~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a primary expression, handling various types of tokens such as
  negation, identifiers, numbers, and parenthesized expressions.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_primary(self)`:

  - Checks if the current token is `MINUS`:

    - Consumes the `MINUS` token.

    - Recursively calls `parse_primary()` to handle the negation.

    - Returns a `UnaryOpNode` with the negation operator and the parsed value.

  - Checks if the current token is an `IDENTIFIER`, `VECTOR`, or `FLOAT`:

    - Calls `parse_function_call_or_identifier()` to handle the token.

  - Checks if the current token is `NUMBER`:

    - Stores the token value.

    - Consumes the `NUMBER` token.

    - Returns the stored value.

  - Checks if the current token is `LPAREN`:

    - Consumes the `LPAREN` token.

    - Calls `parse_expression()` to parse the expression inside the parentheses.

    - Consumes the `RPAREN` token.

    - Returns the parsed expression.

  - Raises a `SyntaxError` if the token is unexpected.


parse_multiplicative Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a multiplicative expression, handling multiplication and
  division operations.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_multiplicative(self)`:

  - Parses the left-hand side of the expression using `parse_primary()`.

  - Iterates through tokens while the current token is `MULTIPLY` or `DIVIDE`:

    - Stores the operator and consumes the token.

    - Parses the right-hand side of the expression using `parse_primary()`.

  - Creates a `BinaryOpNode` with the left-hand side, operator, and right-hand side.

  - Returns the final `BinaryOpNode`.


parse_expression Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a general expression, handling additive expressions, comparison
  operators, logical operators, and ternary conditional expressions.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_expression(self)`:

  - Parses the left-hand side of the expression using `parse_additive()`.

  - Iterates through tokens while the current token is a comparison or logical operator (`LESS_THAN`, `GREATER_THAN`, `LESS_EQUAL`, `GREATER_EQUAL`, `EQUAL`, `NOT_EQUAL`, `AND`, `OR`):

    - Stores the operator and consumes the token.

    - Parses the right-hand side of the expression using `parse_additive()`.

  - Creates a `BinaryOpNode` with the left-hand side, operator, and right-hand side.

  - Checks if the current token is `QUESTION` for a ternary conditional expression:

    - Consumes the `QUESTION` token.

    - Parses the true expression using `parse_expression()`.

    - Consumes the `COLON` token.

    - Parses the false expression using `parse_expression()`.

    - Creates a `TernaryOpNode` with the condition, true expression, and false expression.

  - Returns the final expression node.


parse_return Method
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a return statement, handling the return keyword and the
  associated expression.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_return(self)`:

  - Consumes the `RETURN` token.

  - Parses the expression to be returned using `parse_expression()`.

  - Consumes the `SEMICOLON` token.

  - Returns a `ReturnNode` with the parsed expression.


parse_else_if_chain Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a chain of `else if` and `else` statements, handling their
  conditions and bodies.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_else_if_chain(self)`:

  - Initializes an empty list `else_if_chain` and sets `else_body` to `None`.

  - Iterates through tokens while the current token is `ELSE_IF` or `ELSE`:

    - If the current token is `ELSE_IF`:
    
      - Consumes the `ELSE_IF` token.
      
      - Consumes the `LPAREN` token.
      
      - Parses the `elif` condition using `parse_expression()`.
      
      - Consumes the `RPAREN` token.
      
      - Consumes the `LBRACE` token.
      
      - Parses the `elif` body using `parse_body()`.
      
      - Consumes the `RBRACE` token.
      
      - Appends the condition and body as a tuple to `else_if_chain`.
    
    - If the current token is `ELSE`:
    
      - Consumes the `ELSE` token.
      
      - Consumes the `LBRACE` token.
      
      - Parses the `else` body using `parse_body()`.
      
      - Consumes the `RBRACE` token.
      
      - Breaks the loop.

  - Returns the `else_if_chain` and `else_body`.


parse_if Method
~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an `if` statement, handling the condition, body, and any
  associated `else if` and `else` statements.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_if(self)`:

  - Consumes the `IF` token.

  - Consumes the `LPAREN` token.

  - Parses the condition using `parse_expression()`.

  - Consumes the `RPAREN` token.

  - Consumes the `LBRACE` token.

  - Parses the body of the `if` statement using `parse_body()`.

  - Consumes the `RBRACE` token.

  - Parses any `else if` and `else` statements using `parse_else_if_chain()`.

  - Returns an `IfNode` with the condition, body, `else if` chain, and `else` body.


parse_for Method
~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `for` loop, handling the initialization, condition, update,
  and body of the loop.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_for(self)`:

  - Consumes the `FOR` token.

  - Consumes the `LPAREN` token.

  - Parses the initialization statement using `parse_assignment()`.

  - Consumes the `SEMICOLON` token.

  - Parses the loop condition using `parse_expression()`.

  - Consumes the `SEMICOLON` token.

  - Parses the loop update using `parse_expression()`.

  - Consumes the `RPAREN` token.

  - Consumes the `LBRACE` token.

  - Parses the loop body using `parse_body()`.

  - Consumes the `RBRACE` token.

  - Returns a `ForNode` with the initialization, condition, update, and body.


parse_body Method
~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the body of a function or a block of statements, handling
  different types of statements such as assignments, expressions, returns,
  and control flow.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_body(self)`:

  - Initializes an empty list `body`.

  - Iterates through tokens while the current token is not `RBRACE` or `EOF`:

    - Calls `parse_statement()` to parse each statement.

    - Appends each parsed statement to the `body`.

  - Returns the list `body`.


parse_statement Method
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a single statement, handling assignments, expressions, returns,
  `if` statements, `for` loops, and `break` statements.

**Parameters:**
   - `self`: The instance of the class containing the code and tokens.

**Method Details:**

- `parse_statement(self)`:

  - Checks if the current token is `IDENTIFIER` and the next token is `EQUALS`:

    - Calls `parse_assignment()` to handle the assignment.

  - Checks if the current token is `RETURN`:

    - Calls `parse_return()` to handle the return statement.

  - Checks if the current token is `IF`:

    - Calls `parse_if()` to handle the `if` statement.

  - Checks if the current token is `FOR`:

    - Calls `parse_for()` to handle the `for` loop.

  - Checks if the current token is `BREAK`:

    - Consumes the `BREAK` token.
    - Consumes the `SEMICOLON` token.

  - Checks if the current token is an expression:

    - Calls `parse_expression()` to handle the expression.
    - Consumes the `SEMICOLON` token.

  - Raises a `SyntaxError` if the token is unexpected.

.. _opengl-codegen-1:

OpenGL Codegen
--------------

Methods

__init__(self)

Initializes the code generator.

generate Method
~~~~~~~~~~~~~~~~~~

**Description:**  
Generates shader code from the abstract syntax tree (AST).

**Parameters:**  

- `self`: The instance of the class containing the code and tokens.  
- `ast (ASTNode)` – The abstract syntax tree representing the shader code.

**Returns:**  
- `str` – The generated shader code as a string, or an empty string if the `ast` is not a `ShaderNode`.

**Method Details:**  

- `generate(self, ast)`:
   - Checks if the `ast` is an instance of `ShaderNode`.
   - Sets `self.current_shader` to the `ast`.
   - Calls `generate_shader(ast)` to generate the shader code.
   - Returns an empty string if the `ast` is not a `ShaderNode`.


generate_shader Method
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates the shader code for both vertex and fragment sections from the given node.

**Parameters:** 

- `self`: The instance of the class containing the code and tokens.  
- `node (ShaderNode)` – The node representing the shader structure.

**Returns:**  
- `str` – The generated shader code for the vertex and fragment sections.

**Method Details:**  

- `generate_shader(self, node)`:
   - Sets up the shader by initializing `shader_inputs`, `shader_outputs`, and `uniforms` from the node.
   - Initializes the shader code with `shader main {`.
   - Generates the vertex shader section:
      - Sets `self.vertex_item` to `node.vertex_section`.
      - If `vertex_item` exists:
      - Adds the vertex section to the code.
      - Generates layout qualifiers using `generate_layouts()`.
      - Adds inputs and outputs for the shader and vertex item.
      - Generates uniforms using `generate_uniforms()`.
      - Generates functions using `generate_functions()`.
      - Raises a `ValueError` if no vertex shader section is present.
   - Generates the fragment shader section if present:
      - Sets `self.fragment_item` to `node.fragment_section`.
      - If `fragment_item` exists and has layout qualifiers or functions:
      - Adds the fragment section to the code.
      - Generates layout qualifiers using `generate_layouts()`.
      - Adds inputs and outputs for the fragment item.
      - Generates uniforms using `generate_uniforms()`.
      - Generates functions using `generate_functions()`.
      - Raises a `ValueError` if no fragment shader section is present.
   - Closes the shader code with `}`.
   - Returns the generated shader code.


generate_uniforms Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates the uniform declarations for the shader.

**Parameters:**  
- `self`: The instance of the class containing the code and tokens.

**Returns:**  
- `str` – The generated uniform declarations.

**Method Details:**  

- `generate_uniforms(self)`:
   - Initializes an empty list `uniform_lines`.
   - Iterates through each uniform in `self.uniforms`:
   - Appends the uniform declaration to `uniform_lines`.
   - Joins the list into a single string with newline characters and returns it.


generate_layouts Method
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates the layout qualifiers for the shader, handling both input and output types.

**Parameters:**  

- `self`: The instance of the class containing the code and tokens.  
- `layouts (list of LayoutNode)` – A list of layout objects, each containing `io_type`, `dtype`, and `name`.

**Returns:**  
- `str` – The generated layout qualifiers.

**Method Details:**  

- `generate_layouts(self, layouts)`:

  - Initializes an empty string `code`.
  - Iterates through each layout in `layouts`:
  - Checks if the layout’s `io_type` is `input`:
  - Appends the input layout declaration to `code`.
  - Checks if the layout’s `io_type` is `output`:
  - Appends the output layout declaration to `code`.
  - Returns the generated code string.


generate_functions Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates the function definitions for the shader, handling both vertex and fragment shader types.

**Parameters:**

- `self`: The instance of the class containing the code and tokens.  
- `functions (list[FunctionNode])` – A list of function nodes, each representing a function in the shader.  
- `shader_type (str)` – The type of shader (`vertex` or `fragment`).

**Returns:**  
- `str` – The generated function definitions.

**Method Details:**  

- `generate_functions(self, functions, shader_type)`:
   - Initializes an empty string `code`.
   - Checks if `shader_type` is either `vertex` or `fragment`.
   - Iterates through each `function_node` in `functions`:

     - Generates the parameter list by mapping each parameter’s type and name.
     - Generates the function header with the return type, function name, and parameters.
     - Generates the function body by iterating through each statement in `function_node.body` and calling `generate_statement()`.
     - Closes the function definition.
   - Returns the generated code string.


generate_statement Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates the code for a given statement, handling various types of statements such as variable declarations, assignments, control flow statements, and expressions.

**Parameters:** 

- `self`: The instance of the class containing the code and tokens.  
- `stmt`: The statement node to be generated.  
- `shader_type`: The type of shader (`vertex` or `fragment`).  
- `indent`: The indentation level for the generated code (default is 0).

**Method Details:**  

- `generate_statement(self, stmt, shader_type, indent=0)`:
   - Initializes the indentation string `indent_str` based on the `indent` level.
   - Checks the type of `stmt` and generates the corresponding code:
   - If `stmt` is a `VariableNode`:
   - Returns the variable declaration with the mapped type and name.
   - If `stmt` is an `AssignmentNode`:
   - Returns the assignment statement generated by `generate_assignment()`.
   - If `stmt` is an `IfNode`:
   - Returns the `if` statement generated by `generate_if()`.
   - If `stmt` is a `ForNode`:
   - Returns the `for` loop generated by `generate_for()`.
   - If `stmt` is a `ReturnNode`:
   - Returns the return statement with the generated expression.
   - Otherwise:
   - Returns the generated expression.
   - Each generated statement is properly indented based on the `indent` level.

generate_assignment Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates the code for an assignment statement, handling the left-hand side (LHS) and right-hand side (RHS) expressions.

**Parameters:** 

- `self`: The instance of the class containing the code and tokens.  
- `node`: The assignment node containing the LHS and RHS expressions.  
- `shader_type`: The type of shader (`vertex` or `fragment`).

**Method Details:**  

- `generate_assignment(self, node, shader_type)`:

  - Generates the LHS expression using `generate_expression(node.name, shader_type)`.

  - Generates the RHS expression using `generate_expression(node.value, shader_type)`.

  - Returns the assignment statement in the format `lhs = rhs`.

---

generate_if Method
~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates code for an `if` statement, including optional `else if` and `else` blocks, formatted with the specified indentation.

**Parameters:**  

- `node` (IfNode): An `IfNode` instance representing the `if` statement and its associated conditions and blocks.  
- `shader_type` (str): Specifies the type of shader being generated (e.g., `"vertex"` or `"fragment"`), affecting how certain constructs are handled.  
- `indent` (int): The current level of indentation to apply in the generated code.

**Returns:**  
- `str`: A string containing the generated code for the `if` statement, properly formatted with indentation.

**Method Details:**  
- Constructs the `if` statement with its condition and corresponding body.  
- Handles chained `else if` conditions and their bodies.  
- Includes an optional `else` block if provided.  
- Ensures that code blocks are correctly indented based on the `indent` parameter.

---

generate_else_if Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates code for an `else if` block within an `if` statement, formatted with the specified indentation.

**Parameters:**  

- `node` (IfNode): An `IfNode` instance representing the `else if` condition and its associated body.  
- `shader_type` (str): Specifies the type of shader being generated (e.g., `"vertex"` or `"fragment"`), influencing the handling of specific constructs.  
- `indent` (int): The level of indentation to apply in the generated code.

**Returns:**  
- `str`: A string containing the generated code for the `else if` block, properly formatted with indentation.

**Method Details:**  
- Constructs the `else if` block with its condition and corresponding body.  
- Ensures that the code within the `else if` block is correctly indented based on the `indent` parameter.

---

generate_for Method
~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates code for a `for` loop construct, including initialization, condition, update, and body, formatted with the specified indentation.

**Parameters:** 

- `node` (ForNode): An instance of `ForNode` representing the `for` loop’s components such as initialization, condition, update, and body.  
- `shader_type` (str): Specifies the type of shader being generated (e.g., `"vertex"` or `"fragment"`), affecting the syntax and semantics of the loop.  
- `indent` (int): The level of indentation to apply to the generated code.

**Returns:**  
- `str`: A string containing the generated code for the `for` loop, properly formatted with indentation.

**Method Details:**  
- **Initialization (`init`)**: Generates the initialization statement for the `for` loop, stripping trailing semicolons.  
- **Condition (`condition`)**: Generates the loop’s condition expression.  
- **Update (`update`)**: Generates the update statement for the `for` loop, stripping trailing semicolons.  
- **Body**: Generates the code for the body of the `for` loop, applying additional indentation.

**Example:**

.. code:: cpp

   for (int i = 0; i < 10; i++) {
       // Loop body
   }

---

generate_update Method
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates the code for the update part of a `for` loop, handling various types of expressions such as assignments, unary operations, and binary operations.

**Parameters:**  

- `node` (ASTNode): An instance of `AssignmentNode`, `UnaryOpNode`, or `BinaryOpNode` representing the update expression in the `for` loop.  
- `shader_type` (str): Specifies the type of shader being generated (e.g., `"vertex"` or `"fragment"`), which can affect how the update expression is formatted.

**Returns:**  
- `str`: A string containing the generated code for the update expression.

**Method Details:**  

- **AssignmentNode**: Handles both simple assignments and increments/decrements.  
  - If the value is a `UnaryOpNode`, it generates increment or decrement operations.  
  - Otherwise, it generates a standard assignment.  
- **UnaryOpNode**: Generates pre-increment, post-increment, pre-decrement, post-decrement, or unary operations based on the operation type.  
- **BinaryOpNode**: Handles binary operations and maps them to appropriate operators using `map_operator`.  
- **Error Handling**: Raises a `ValueError` for unsupported node types.

---

generate_expression Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Generates code for various types of expressions used in shader programming. This includes translating simple strings, handling variables, binary and unary operations, function calls, ternary operations, and member accesses.

**Parameters:**

- `expr` (ASTNode): An instance of a specific type of expression node, such as `VariableNode`, `BinaryOpNode`, etc.  
- `shader_type` (str): Indicates the type of shader (e.g., `"vertex"` or `"fragment"`), which might influence how the expressions are formatted.

**Returns:**  
- `str`: A string containing the generated code for the expression.

**Method Details:**  

1. **str**: Uses `translate_expression` to handle basic string translation or identifiers.  
2. **VariableNode**: Generates a variable declaration or usage based on its type and name.  
3. **BinaryOpNode**: Generates binary operations by recursively generating code for left and right operands and mapping the operator.  
4. **FunctionCallNode**: Generates function calls, including the function name and arguments.  
5. **UnaryOpNode**: Handles unary operations, including pre-increment and pre-decrement.  
6. **TernaryOpNode**: Generates ternary conditional expressions.  
7. **MemberAccessNode**: Handles member accesses (e.g., object.property).  
8. **Default Case**: Converts any other node types to their string representations.

---

translate_expression Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Translates a given expression (identifier) into its corresponding name based on the shader type. It checks if the expression matches any of the inputs or outputs for the current shader item and returns the appropriate name.

**Parameters:**  

- `expr` (str): The identifier or expression to be translated.  
- `shader_type` (str): The type of shader (`"vertex"` or `"fragment"`) which determines which item lists to check.

**Returns:**  
- `str`: The translated name if a match is found, otherwise the original expression.

**Method Details:**  

1. **Vertex Shader Type:**  

   - If `shader_type` is `"vertex"` and `self.vertex_item` is not `None`, it checks the inputs and outputs of `self.vertex_item`.  
   - If `expr` matches any input or output names, it returns the matched name.  
   - If no match is found, it returns the original expression.

2. **Fragment Shader Type:**  

   - If `shader_type` is `"fragment"` and `self.fragment_item` is not `None`, it checks the inputs and outputs of `self.fragment_item`.  
   - If `expr` matches any input or output names, it returns the matched name.  
   - If no match is found, it returns the original expression.

3. **Default Return:**  

   - If the shader type is not recognized or no match is found, the method returns the expression as is.

---

map_type Method
~~~~~~~~~~~~~~~~~~~

**Description:**  
Translates internal type representations into their corresponding shader types using a predefined mapping.

**Parameters:**  
- `vtype` (str): The internal type representation to be mapped.

**Returns:**  
- `str`: The corresponding shader type based on the mapping, or the original type if no mapping is found.

**Method Details:** 

1. **Type Mapping:** 

   - The method uses a dictionary called `type_map` to define the mappings: 

   .. code:: cpp
 
      vec3 maps to vec3  
      vec4 maps to vec4  
      float maps to float  
      int maps to int  
      bool maps to bool 

   - The `type_map` dictionary includes common GLSL types.

2. **Lookup:**  
   - The method attempts to find the `vtype` in the `type_map` dictionary.  
   - If `vtype` is found, it returns the corresponding shader type.  
   - If `vtype` is not found in the dictionary, it returns the original `vtype`.

---

map_operator Method
~~~~~~~~~~~~~~~~~~~~~~~

**Description:**  
Maps internal operator representations to their corresponding shader language operators using a predefined mapping.

**Parameters:**  
- `op` (str): The internal operator representation to be mapped.

**Returns:**  
- `str`: The corresponding shader operator based on the mapping, or the original operator if no mapping is found.

**Method Details:** 

1. **Operator Mapping:** 

   - The method uses a dictionary called `operator_map` to define the mappings:  

   .. code:: cpp

      + maps to +  
      - maps to -  
      * maps to *  
      / maps to /  
      == maps to ==  
      != maps to !=  

   - The `operator_map` dictionary includes common GLSL operators.

2. **Lookup:**  
   - The method attempts to find the `op` in the `operator_map` dictionary.  
   - If `op` is found, it returns the corresponding shader operator.  
   - If `op` is not found in the dictionary, it returns the original operator.

---

This format should provide a clear and organized documentation for each method, making it easier for users to understand and use the methods effectively.

Mojo
----

Mojo AST
---------

.. _ternaryopnode-class-2:

TernaryOpNode Class
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a ternary conditional operation in an abstract syntax tree
  (AST). This node type models the conditional expression and its two
  possible outcomes, facilitating the generation of conditional code in
  shader programming.

**Constructor Parameters**:
   - `condition` (MojoASTNode): The condition expression that determines which of the two outcomes to choose.
   - `true_expr` (MojoASTNode): The expression to be evaluated and returned if the condition is true.
   - `false_expr` (MojoASTNode): The expression to be evaluated and returned if the condition is false.

**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `TernaryOpNode` instance, useful for debugging
        and logging.
      - **Returns**: A string in the format:

      .. code:: python

        "TernaryOpNode(condition={self.condition}, true_expr={self.true_expr}, false_expr={self.false_expr})"


.. _shadernode-class-2:

ShaderNode Class
~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a shader program in an abstract syntax tree (AST),
  containing a collection of functions that define the shader’s behavior
  and structure.

**Constructor Parameters**:
   - `functions` (list of MojoASTNode): A list of function nodes (`MojoASTNode`) that are part of the shader. These functions define the various operations and logic within the shader.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `ShaderNode` instance, useful for debugging
        and logging.
      - **Returns**: `str`: A string representation of the `ShaderNode` in the format:

      .. code:: python

        "ShaderNode(functions={self.functions})"


StructNode Class
~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a structure definition in an abstract syntax tree (AST). It
  encapsulates the name of the structure and its members, which define
  the structure’s layout and data types.

**Constructor Parameters**:
   - `name` (str): The name of the structure.
   - `members` (list of Tuple[str, str]): A list of tuples where each tuple represents a member of the structure. Each tuple contains the member’s name and its data type.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `StructNode` instance, which is useful for
        debugging and logging.
      - **Returns**: `str`: A string representation of the `StructNode` in the format:

      .. code:: python

        "StructNode(name={self.name}, members={self.members})"


.. _functionnode-class-2:

FunctionNode Class
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a function definition in an abstract syntax tree (AST). It
  includes the function’s attributes, return type, name, parameters,
  body, and any additional attributes.

**Constructor Parameters**:
   - `qualifier` (str): Specifies any qualifiers for the function, such as `static`, `inline`, or `extern`.
   - `return_type` (str): The data type that the function returns.
   - `name` (str): The name of the function.
   - `params` (list of Tuple[str, str]): A list of tuples where each tuple represents a parameter of the function. Each tuple contains the parameter’s type and name.
   - `body` (list of ASTNode): A list of statements representing the body of the function.
   - `attributes` (list of str, optional): A list of additional attributes or modifiers for the function, such as `const`, `volatile`, etc. Defaults to an empty list if not provided.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `FunctionNode` instance, which is useful for
        debugging and logging.
      - **Returns**: `str`: A string representation of the `FunctionNode` in the format:

      .. code:: python

        "FunctionNode(qualifier={self.qualifier}, return_type={self.return_type}, name={self.name}, params={self.params}, body={self.body}, attributes={self.attributes})"

VariableDeclarationNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a variable declaration in an abstract syntax tree (AST). It
  includes the variable’s type, name, and optionally an initial value.

**Constructor Parameters**:
   - `var_type` (str): The data type of the variable (e.g., `int`, `float`, `vec3`).
   - `name` (str): The name of the variable.
   - `initial_value` (Optional[str]): The initial value assigned to the variable. Defaults to `None` if not provided.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `VariableDeclarationNode` instance, which is useful for debugging and logging.
      - **Returns**: `str`: A string representation of the `VariableDeclarationNode` in the format:

      .. code:: python

        "VariableDeclarationNode(var_type={self.var_type}, name={self.name}, initial_value={self.initial_value})"

ArrayAccessNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents an array access operation in an abstract syntax tree (AST).
  It includes the array being accessed and the index used for accessing
  an element.

**Constructor Parameters**:
   - `array` (MojoASTNode): The array from which an element is accessed.
   - `index` (MojoASTNode): The index used to access an element of the array.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `ArrayAccessNode` instance, which is useful
        for debugging and logging.
      - **Returns**: `str`: A string representation of the `ArrayAccessNode` in the format:

      .. code:: python

        "ArrayAccessNode(array={self.array}, index={self.index})"

.. _variablenode-class-2:

VariableNode Class
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a variable declaration or reference in an abstract syntax
  tree (AST). It includes the variable’s type, name, and optional
  attributes.

**Constructor Parameters**:
   - `vtype` (str): The type of the variable (e.g., `"int"`, `"float"`).
   - `name` (str): The name of the variable.
   - `attributes` (list, optional): A list of attributes associated with the variable. Defaults to an empty list if not provided.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `VariableNode` instance, which is useful for
        debugging and logging.
      - **Returns**: `str`: A string representation of the `VariableNode` in the format:

      .. code:: python

        "VariableNode(vtype='{self.vtype}', name='{self.name}', attributes={self.attributes})"

AttributeNode Class
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents an attribute associated with a variable, function, or other
  elements in an abstract syntax tree (AST). Attributes are often used
  to specify metadata or additional properties.

**Constructor Parameters**:
   - `name` (str): The name of the attribute (e.g., `"location"`, `"binding"`).
   - `args` (list, optional): A list of arguments for the attribute. Defaults to an empty list if not provided.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `AttributeNode` instance, which is useful for
        debugging and logging.
      - **Returns**: `str`: A string representation of the `AttributeNode` in the format:

      .. code:: python

        "AttributeNode(name='{self.name}', args={self.args})"


.. _assignmentnode-class-2:

AssignmentNode Class
~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents an assignment operation in the abstract syntax tree (AST).
  This node is used to model the assignment of a value to a variable,
  potentially with a specific operator.

**Constructor Parameters:**
   - `left` (MojoASTNode): The left-hand side of the assignment, typically a variable or an array element.
   - `right` (MojoASTNode): The right-hand side of the assignment, representing the value to be assigned.
   - `operator` (str, optional): The assignment operator. Defaults to `"="`. Other operators like `"+="`, `"-="`, etc., can be used.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `AssignmentNode` instance, which is useful for
        debugging and logging.
      - **Returns**: `str`: A string representation of the `AssignmentNode` in the format:

      .. code:: python

        "AssignmentNode(left={self.left}, operator='{self.operator}', right={self.right})"

.. _ifnode-class-2:

IfNode Class
~~~~~~~~~~~~~~~~

| **Description:**
| Represents an `if` statement in the abstract syntax tree (AST). This
  node is used to model conditional logic with an optional `else`
  block.

**Constructor Parameters:**
   - `condition` (MojoASTNode): The condition to be evaluated for the `if` statement. This typically involves a boolean expression.
   - `if_body` (list of MojoASTNode): The body of the `if` block, containing statements to be executed if the condition evaluates to `True`.
   - `else_body` (list of MojoASTNode, optional): The body of the `else` block, containing statements to be executed if the condition evaluates to `False`. Defaults to `None` if no `else` block is present.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `IfNode` instance, including the condition,
        `if_body`, and `else_body`.
      - **Returns**: `str`: A string representation of the `IfNode` in the format:

      .. code:: python

        "IfNode(condition={self.condition}, if_body={self.if_body}, else_body={self.else_body})"

.. _fornode-class-2:

ForNode Class
~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a `for` loop in the abstract syntax tree (AST). This node
  models the structure of a `for` loop, including initialization,
  condition, update, and body.

**Constructor Parameters:**
   - `init` (MojoASTNode): The initialization statement of the `for` loop, which is executed once before the loop starts.
   - `condition` (MojoASTNode): The loop condition that is evaluated before each iteration. The loop continues to execute as long as this condition is `True`.
   - `update` (MojoASTNode): The update statement executed after each iteration of the loop.
   - `body` (list of MojoASTNode): The body of the `for` loop, containing the statements to be executed in each iteration.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `ForNode` instance, including the
        initialization, condition, update, and body.
      - **Returns**: `str`: A string representation of the `ForNode` in the format:

      .. code:: python

        "ForNode(init={self.init}, condition={self.condition}, update={self.update}, body={self.body})"

WhileNode Class
~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a `while` loop in the abstract syntax tree (AST). This
  node models the structure of a `while` loop, including its condition
  and body.

**Constructor Parameters:**
   - `condition` (MojoASTNode): The condition that is evaluated before each iteration. The loop continues to execute as long as this condition is `True`.
   - `body` (list of MojoASTNode): The body of the `while` loop, containing the statements to be executed in each iteration.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `WhileNode` instance, including the condition
        and body.
      - **Returns**: `str`: A string representation of the `WhileNode` in the format:

      .. code:: python

        "WhileNode(condition={self.condition}, body={self.body})"

.. _returnnode-class-2:

ReturnNode Class
~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a `return` statement in the abstract syntax tree (AST).
  This node captures the value to be returned from a function or method.

**Constructor Parameters:**
   - `value` (MojoASTNode or None): The value to be returned. If `None`, it represents a return statement with no value.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `ReturnNode` instance, including the return
        value.
      - **Returns**: `str`: A string representation of the `ReturnNode` in the format:

      .. code:: python

        "ReturnNode(value={self.value})"

.. _functioncallnode-class-2:

FunctionCallNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a function or method call in the abstract syntax tree
  (AST). This node captures the name of the function being called and
  the arguments passed to it.

**Constructor Parameters:**
   - `name` (str): The name of the function or method being called.
   - `args` (list of MojoASTNode): The arguments passed to the function. Each argument is represented as an AST node.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `FunctionCallNode` instance, including the
        function name and its arguments.
      - **Returns**: `str`: A string representation of the `FunctionCallNode` in the format:

      .. code:: python

        "FunctionCallNode(name={self.name}, args={self.args})"


.. _binaryopnode-class-2:

BinaryOpNode Class
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a binary operation in the abstract syntax tree (AST). This
  node captures two operands and the operator used to combine them.

**Constructor Parameters:**
   - `left` (MojoASTNode): The left operand of the binary operation.
   - `op` (str): The operator used in the binary operation (e.g., "+", "-", "*", "/").
   - `right` (MojoASTNode): The right operand of the binary operation.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `BinaryOpNode` instance, including the left
        operand, the operator, and the right operand.
      - **Returns**: `str`: A string representation of the `BinaryOpNode` in the format:

      .. code:: python

        "BinaryOpNode(left={self.left}, operator={self.op}, right={self.right})"


.. _unaryopnode-class-2:

UnaryOpNode Class
~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a unary operation in the abstract syntax tree (AST). This
  node captures the operator and its single operand.

**Constructor Parameters:**
   - `op` (str): The operator used in the unary operation (e.g., "+", "-", "++", "--").
   - `operand` (MojoASTNode): The operand for the unary operation.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `UnaryOpNode` instance, including the operator
        and the operand.
      - **Returns**: `str`: A string representation of the `UnaryOpNode` in the format:

      .. code:: python

        "UnaryOpNode(operator={self.op}, operand={self.operand})"


.. _memberaccessnode-class-2:

MemberAccessNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents an access operation on a member of an object in the
  abstract syntax tree (AST). This node captures the object and the
  specific member being accessed.

**Constructor Parameters:**
   - `object` (MojoASTNode): The object or variable whose member is being accessed.
   - `member` (str): The name of the member being accessed.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `MemberAccessNode` instance, including the
        object and the member.
      - **Returns**: `str`: A string representation of the `MemberAccessNode` in the format:

      .. code:: python

        "MemberAccessNode(object={self.object}, member={self.member})"


VectorConstructorNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a vector constructor operation in the abstract syntax tree
  (AST). This node is used to create vectors from a set of arguments
  with a specified type.

**Constructor Parameters:**
   - `type_name` (str): The name of the vector type (e.g., `"vec2"`, `"vec3"`, `"vec4"`).
   - `args` (List[MojoASTNode]): A list of arguments used to initialize the vector.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `VectorConstructorNode` instance, including
        the vector type and its initialization arguments.
      - **Returns**: `str`: A string representation of the `VectorConstructorNode` in the format:

      .. code:: python

        "VectorConstructorNode(type_name={self.type_name}, args={self.args})"


TextureSampleNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a texture sampling operation in the abstract syntax tree
  (AST). This node is used to sample a texture using a specified sampler
  and texture coordinates.

**Constructor Parameters:**
   - `texture` (MojoASTNode): The texture to be sampled.
   - `sampler` (MojoASTNode): The sampler used to sample the texture.
   - `coordinates` (MojoASTNode): The coordinates at which the texture is sampled.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `TextureSampleNode` instance, including the
        texture, sampler, and coordinates used for sampling.
      - **Returns**: `str`: A string representation of the `TextureSampleNode` in the format:

      .. code:: python

        "TextureSampleNode(texture={self.texture}, sampler={self.sampler}, coordinates={self.coordinates})"


ThreadgroupSyncNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a synchronization point for thread groups in a compute
  shader or parallel execution environment. This node ensures that all
  threads in the group reach the synchronization point before
  continuing.

**Constructor Parameters:**
   - None

**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `ThreadgroupSyncNode` instance.
      - **Returns**: `str`: A string representation of the `ThreadgroupSyncNode` in the format:

      .. code:: python

        "ThreadgroupSyncNode()"


ConstantBufferNode Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a constant buffer in a shader program, which is used to
  store uniform data that remains constant across multiple shader
  invocations.

**Constructor Parameters:**
   - `name` (str): The name of the constant buffer.
   - `members` (list of `VariableNode`): A list of variables that are members of the constant buffer.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `ConstantBufferNode` instance.
      - **Returns**: `str`: A string representation of the `ConstantBufferNode` in the format:

      .. code:: python

        "ConstantBufferNode(name={self.name}, members={self.members})"


ImportNode Class
~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents an import statement in a shader program, used to include
  external modules or libraries with an optional alias.

**Constructor Parameters:**
   - `module_name` (str): The name of the module to be imported.
   - `alias` (str, optional): An alias for the module, allowing it to be referenced with a different name in the shader.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `ImportNode` instance.
      - **Returns**: `str`: A string representation of the `ImportNode` in the format:

      .. code:: python

        "ImportNode(module_name='{self.module_name}', alias='{self.alias}')"
        
        if an alias is provided, otherwise
        
        "ImportNode(module_name='{self.module_name}')"


ClassNode Class
~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a class definition in the shader program, including its
  name, base classes, and members.

**Constructor Parameters:**
   - `name` (str): The name of the class.
   - `base_classes` (list of str): A list of base class names that this class inherits from.
   - `members` (list of `MojoASTNode`): A list of member variables and methods that belong to the class.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `ClassNode` instance.
      - **Returns**: `str`: A string representation of the `ClassNode` in the format:

      .. code:: python

        "ClassNode(name={self.name}, base_classes={self.base_classes}, members={self.members})"


DecoratorNode Class
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a decorator applied to functions or classes in the shader
  program, including the decorator’s name and any optional arguments.

**Constructor Parameters:**
   - `name` (str): The name of the decorator.
   - `args` (list of `MojoASTNode`, optional): A list of arguments for the decorator. Defaults to an empty list if not provided.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `DecoratorNode` instance.
      - **Returns**: `str`: A string representation of the `DecoratorNode` in the format:

      .. code:: python

        "DecoratorNode(name={self.name}, args={self.args})"


SwitchCaseNode Class
~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a case in a switch statement, including the condition for
  the case and the block of code to execute if the condition is met.

**Constructor Parameters:**
   - `condition` (MojoASTNode): The condition that determines if this case should be executed.
   - `body` (list of `MojoASTNode`): The block of code to execute if the condition is met.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `SwitchCaseNode` instance.
      - **Returns**: `str`: A string representation of the `SwitchCaseNode` in the format:

      .. code:: python

        "SwitchCaseNode(condition={self.condition}, body={self.body})"


SwitchNode Class
~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Represents a switch statement, including the expression to evaluate
  and the list of cases to handle different values of the expression.

**Constructor Parameters:**
   - `expression` (MojoASTNode): The expression being evaluated in the switch statement.
   - `cases` (list of `SwitchCaseNode`): A list of `SwitchCaseNode` instances, each representing a case in the switch statement.


**Methods**:
   - `__repr__()`:
      - **Description**: Returns a string representation of the `SwitchNode` instance.
      - **Returns**: `str`: A string representation of the `SwitchNode` in the format:

      .. code:: python

        "SwitchNode(expression={self.expression}, cases={self.cases})"


Mojo Lexer
------------

Token Definitions and Keywords for Mojo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _token-definitions-1:

**Token Definitions**
^^^^^^^^^^^^^^^^^^^^^

-  | ``COMMENT_SINGLE``: ``#.*``
   | Represents a single-line comment starting with ``#``.

-  | ``COMMENT_MULTI``: ``"""[\s\S]*?"""``
   | Represents a multi-line comment enclosed in triple double quotes
     (``"""``).

-  | ``STRUCT``: ``\bstruct\b``
   | Represents the ``struct`` keyword for defining structures.

-  | ``LET``: ``\blet\b``
   | Represents the ``let`` keyword for variable declaration.

-  | ``VAR``: ``\bvar\b``
   | Represents the ``var`` keyword for variable declaration.

-  | ``FN``: ``\bfn\b``
   | Represents the ``fn`` keyword for function definition.

-  | ``RETURN``: ``\breturn\b``
   | Represents the ``return`` keyword for returning values from
     functions.

-  | ``IF``: ``\bif\b``
   | Represents the ``if`` keyword for conditional statements.

-  | ``ELSE``: ``\belse\b``
   | Represents the ``else`` keyword for conditional statements.

-  | ``FOR``: ``\bfor\b``
   | Represents the ``for`` keyword for loop statements.

-  | ``WHILE``: ``\bwhile\b``
   | Represents the ``while`` keyword for loop statements.

-  | ``IMPORT``: ``\bimport\b``
   | Represents the ``import`` keyword for importing modules.

-  | ``DEF``: ``\bdef\b``
   | Represents the ``def`` keyword for function definition.

-  | ``INT``: ``\bInt\b``
   | Represents the ``Int`` type keyword.

-  | ``FLOAT``: ``\bFloat\b``
   | Represents the ``Float`` type keyword.

-  | ``BOOL``: ``\bBool\b``
   | Represents the ``Bool`` type keyword.

-  | ``STRING``: ``\bString\b``
   | Represents the ``String`` type keyword.

-  | ``IDENTIFIER``: ``[a-zA-Z_][a-zA-Z0-9_]*``
   | Represents an identifier consisting of letters, digits, and
     underscores.

-  | ``NUMBER``: ``\d+(\.\d+)?``
   | Represents a number, which can be an integer or a floating-point
     number.

-  | ``LBRACE``: ``\{``
   | Represents the left brace ``{``.

-  | ``RBRACE``: ``\}``
   | Represents the right brace ``}``.

-  | ``LPAREN``: ``\(``
   | Represents the left parenthesis ``(``.

-  | ``RPAREN``: ``\)``
   | Represents the right parenthesis ``)``.

-  | ``LBRACKET``: ``\[``
   | Represents the left bracket ``[``.

-  | ``RBRACKET``: ``\]``
   | Represents the right bracket ``]``.

-  | ``SEMICOLON``: ``;``
   | Represents the semicolon ``;``.

-  | ``STRING_LITERAL``: ``"[^"]*"``
   | Represents a string literal enclosed in double quotes.

-  | ``COMMA``: ``,``
   | Represents the comma ``,``.

-  | ``COLON``: ``:``
   | Represents the colon ``:``.

-  | ``LESS_EQUAL``: ``<=``
   | Represents the less-than-or-equal-to operator.

-  | ``GREATER_EQUAL``: ``>=``
   | Represents the greater-than-or-equal-to operator.

-  | ``LESS_THAN``: ``<``
   | Represents the less-than operator.

-  | ``GREATER_THAN``: ``>``
   | Represents the greater-than operator.

-  | ``EQUAL``: ``==``
   | Represents the equality operator.

-  | ``NOT_EQUAL``: ``!=``
   | Represents the inequality operator.

-  | ``PLUS_EQUALS``: ``+=``
   | Represents the addition assignment operator.

-  | ``MINUS_EQUALS``: ``-=``
   | Represents the subtraction assignment operator.

-  | ``MULTIPLY_EQUALS``: ``*=``
   | Represents the multiplication assignment operator.

-  | ``DIVIDE_EQUALS``: ``/=``
   | Represents the division assignment operator.

-  | ``PLUS``: ``+``
   | Represents the addition operator.

-  | ``MINUS``: ``-``
   | Represents the subtraction operator.

-  | ``MULTIPLY``: ``*``
   | Represents the multiplication operator.

-  | ``DIVIDE``: ``/``
   | Represents the division operator.

-  | ``AND``: ``&&``
   | Represents the logical AND operator.

-  | ``OR`` : ``\|\|``
   | Represents the logical OR operator.

-  | ``DOT``: ``\.``
   | Represents the dot ``.`` for member access.

-  | ``EQUALS``: ``=``
   | Represents the assignment operator.

-  | ``WHITESPACE``: ``\s+``
   | Represents whitespace characters (spaces, tabs, newlines).

.. _keywords-1:

**Keywords**
^^^^^^^^^^^^

-  ``struct``: ``STRUCT``
-  ``let``: ``LET``
-  ``var``: ``VAR``
-  ``fn``: ``FN``
-  ``return``: ``RETURN``
-  ``if``: ``IF``
-  ``else``: ``ELSE``
-  ``for``: ``FOR``
-  ``while``: ``WHILE``
-  ``import``: ``IMPORT``
-  ``def``: ``DEF``
-  ``Int``: ``INT``
-  ``Float``: ``FLOAT``
-  ``Bool``: ``BOOL``
-  ``String``: ``STRING``

Methods

__init__(self)

Initializes the code generator.

.. _tokenize-method-1:

Tokenize Method
~~~~~~~~~~~~~~~~~~~

| **Description:**
| Tokenizes the input code into a list of tokens based on predefined
  patterns. It processes each segment of the code to match against the
  token patterns and converts identifiers to keywords if applicable.

| **Parameters:**
| - None

| **Returns:**
| - None

| **Method Details:**

- Initializes the token position to zero and iterates through the code.
- For each position, attempts to match the code segment with predefined regex patterns.
- If a match is found, determines the token type:
  - Converts `IDENTIFIER` tokens to keywords if they match predefined keywords.
  - Skips tokens of types `WHITESPACE`, `COMMENT_SINGLE`, and `COMMENT_MULTI`.
  - Appends other tokens to the `tokens` list.
- Moves the position index forward by the length of the matched text.
- Raises a `SyntaxError` if an illegal character is encountered.
- Appends an `EOF` (end-of-file) token at the end of the code.


Mojo Parser
------------

Methods

__init__(self)

Initializes the code generator.

.. _eat-2:

eat
~~~~~~~

-  **Description**:

   -  Consumes the current token if it matches the expected type.
   -  Advances to the next token and skips any comments following the
      current token.

-  **Parameters**:

   -  `token_type`: The type of token expected to be consumed.

-  **Returns**:

   -  None

-  **Raises**:

   -  `SyntaxError`: If the current token does not match the expected
      token type.

.. _skip_commentsself-1:

skip_comments(self)
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Skips over single-line and multi-line comments in the token stream by
  advancing past them.

| **Parameters:**
| - None

| **Returns:**
| - None

| **Raises:**
| - None

.. _parse-method-1:

parse Method
~~~~~~~~~~~~~~~~

| **Description:**
| Parses the entire code to generate an abstract syntax tree (AST)
  representation. It starts by parsing the module and ensures the end of
  the file is reached.

| **Parameters:**
| - None

| **Returns:**
| - `module`: The parsed module, which is an AST representation of the
  code.

| **Method Details:**
| - Calls `parse_module` to parse the module’s structure from the
  code. - Calls eat to ensure that the end-of-file (EOF) token is
  present and correctly positioned. - Returns the parsed module.

parse_module Method
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the module to extract statements and constructs an abstract
  syntax tree (AST). It handles different types of statements, including
  imports, structures, classes, constant buffers, functions, variable
  declarations or assignments, and decorators.

| **Parameters:**
| - None

| **Returns:**
| - `ShaderNode`: An instance of `ShaderNode` containing the list of
  parsed statements.

| **Method Details:**

- Iterates through tokens until the end-of-file (EOF) token is encountered.
- Handles each type of statement based on the current token type:
  - **IMPORT**: Calls `parse_import_statement` to parse import statements.
  - **STRUCT**: Calls `parse_struct` to parse structure definitions.
  - **CLASS**: Calls `parse_class` to parse class definitions.
  - **CONSTANT**: Calls `parse_constant_buffer` to parse constant buffer declarations.
  - **FN**: Calls `parse_function` to parse function definitions.
  - **LET, VAR**: Calls `parse_variable_declaration_or_assignment` to parse variable declarations or assignments.
  - **DECORATOR**: Calls `parse_decorator` to parse decorator statements.
- Uses `eat` to consume and process the current token.
- Returns a `ShaderNode` instance containing all parsed statements.


parse_import_statement Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an import statement from the source code and constructs an
  `ImportNode`.

| **Parameters:**
| - None

| **Returns:**
| - `ImportNode`: An instance with the module name and optional alias.

| **Method Details:**

- Consumes the `"IMPORT"` token.
- Extracts the module name from the `"IDENTIFIER"` token.
- Optionally handles the `"AS"` keyword to set an alias.
- Consumes the `"SEMICOLON"` token if present.


parse_struct Method
~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `struct` definition from the source code and constructs a
  `StructNode`.

| **Parameters:**
| - None

| **Returns:**
| - `StructNode`: An instance with the struct’s name and its members.

| **Method Details:**

- Consumes the `"STRUCT"` token.
- Extracts the struct name from the `"IDENTIFIER"` token.
- Consumes the `"COLON"` token.
- Iterates over subsequent tokens to parse member variables, handling optional type declarations and attributes.
- Stops parsing members upon encountering `"EOF"`, `"FN"`, `"STRUCT"`, or `"CLASS"` tokens.

parse_class Method
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `class` definition from the source code and constructs a
  `ClassNode`.

| **Parameters:**
| - None

| **Returns:**
| - `ClassNode`: An instance representing the class with its name,
  base classes, and members.

| **Method Details:**

- Consumes the `"CLASS"` token.
- Extracts the class name from the `"IDENTIFIER"` token.
- Parses optional base classes enclosed in parentheses.
- Consumes the `"LBRACE"` token.
- Iterates over tokens to parse class members, including functions, variable declarations, or nested classes.
- Stops parsing members upon encountering the `"RBRACE"` token.
- Constructs and returns a `ClassNode` with the parsed name, base classes, and members.


parse_constant_buffer Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a constant buffer definition from the source code and
  constructs a `ConstantBufferNode`.

| **Parameters:**
| - None

| **Returns:**
| - `ConstantBufferNode`: An instance representing the constant buffer
  with its name and members.

| **Method Details:**

- Consumes the `"CONSTANT"` token.
- Extracts the constant buffer name from the `"IDENTIFIER"` token.
- Consumes the `"LBRACE"` token.
- Iterates over tokens to parse the members of the constant buffer, extracting the variable type and name, and consuming the `"SEMICOLON"` token.
- Stops parsing members upon encountering the `"RBRACE"` token.
- Constructs and returns a `ConstantBufferNode` with the parsed name and members.


.. _parse_function-method-1:

parse_function Method
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a function definition from the source code and constructs a
  `FunctionNode`.

| **Parameters:**
| - None

| **Returns:**
| - `FunctionNode`: An instance representing the parsed function,
  including its attributes, return type, name, parameters, body, and
  additional attributes.

| **Method Details:**

- Parses function attributes using `self.parse_attributes()`.
- Checks for and consumes the `"FN"` token, setting the function’s qualifier if present.
- Extracts the function name from the `"IDENTIFIER"` token.
- Consumes the `"LPAREN"` token and parses function parameters using `self.parse_parameters()`.
- Consumes the `"RPAREN"` token.
- Checks for and consumes the `"MINUS"` and `"GREATER_THAN"` tokens to parse the return type if specified.
- Parses additional attributes after the return type.
- Parses the function body using `self.parse_block()`.
- Constructs and returns a `FunctionNode` with the parsed information.


.. _parse_parameters-method-1:

parse_parameters Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses the parameter list for a function definition from the source
  code, handling type annotations and attributes.

| **Parameters:**
| - None

| **Returns:**
| - `List[VariableNode]`: A list of `VariableNode` instances
  representing the parameters, including their types, names, and
  attributes.

| **Method Details:**

- Initializes an empty list `params` to store parsed parameters.
- Iterates through tokens until it encounters a `RPAREN` token (end of parameter list).
- **Attributes:** Calls `self.parse_attributes()` to parse any attributes associated with the parameter.
- **Type Handling:** Checks if the current token is a valid type (`FLOAT`, `INT`, `UINT`, `BOOL`, `IDENTIFIER`):
  - Extracts the type and handles optional type annotations indicated by a `COLON` token.
  - Retrieves the parameter name from the `IDENTIFIER` token if present.
  - Parses and appends attributes specific to the parameter.
  - Creates and adds a `VariableNode` to the `params` list.
- **Comma Handling:** Ensures commas are correctly placed and raises an error for trailing commas.
- **Error Handling:** Raises `SyntaxError` for unexpected tokens or incorrect syntax in the parameter list.


| **Errors Raised:**
| - `SyntaxError` for unexpected tokens, trailing commas, or incorrect
  syntax in the parameter list.

parse_attributes Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a sequence of attribute tokens from the source code, extracting
  their names and arguments.

| **Parameters:**
| - None

| **Returns:**
| - `List[AttributeNode]`: A list of `AttributeNode` instances
  representing the parsed attributes.

| **Method Details:**

- Initializes an empty list `attributes` to store parsed attributes.
- Continuously checks if the current token is of type `ATTRIBUTE`.
- **Attribute Content:** Strips the surrounding `[[` and `]]` from the attribute content to extract the core information.
- **Parsing Attributes:** Splits the content by `(` to separate the attribute name from its arguments:
  - **Name Extraction:** The part before `(` is the attribute name.
  - **Arguments Extraction:** The part inside the parentheses is split by commas to get a list of arguments.
- **Creating AttributeNode:** Creates an `AttributeNode` instance with the name and arguments, and appends it to the `attributes` list.
- **Consuming Token:** Calls `self.eat("ATTRIBUTE")` to advance to the next token.


| **Errors Raised:**
| - No specific errors are raised by this method. It assumes attributes
  are well-formed according to the defined token patterns.

parse_block Method
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a block of statements, which can start with either a colon or
  an opening brace, and continues until it encounters a closing brace or
  the end of the file.

| **Parameters:**
| - None

| **Returns:**
| - `List[StatementNode]`: A list of `StatementNode` instances
  representing the parsed statements within the block.

| **Method Details:**

1. **Block Start:**

   - **Colon (`:`) or Brace (`{`):**
     - If the current token is `COLON`, it is consumed to denote the start of the block.
     - If the current token is `LBRACE`, it is consumed to denote the start of the block.
     - Raises a `SyntaxError` if neither `COLON` nor `LBRACE` is found.


2. **Parsing Statements:**

   -  Initializes an empty list `statements` to store the parsed
      statements.
   -  Continues to parse statements until encountering `RBRACE` or
      `EOF`.

3. **Block End:**

   -  **`Closing Brace (`}\ `):`** If a closing brace is
      encountered, it is consumed to denote the end of the block.

4. **Return Statements:**

   -  Returns the list of parsed statements.

| **Errors Raised:**
| - `SyntaxError`: Raised if the block does not start with a `COLON`
  or `LBRACE`, or if unexpected tokens are found while parsing
  statements.

parse_statement Method
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a single statement from the input code. The type of statement
  to be parsed is determined based on the current token.

| **Parameters:**
| - None

| **Returns:**
| - `StatementNode`: The parsed statement, which can be one of several
  types including variable declarations, function definitions, control
  flow statements, or expressions.

| **Method Details:**
| 1. **Variable Declarations or Assignments:**
   - **Token Types:** `FLOAT`, `INT`, `UINT`, `BOOL`, `IDENTIFIER`, `LET`, `VAR`
   - Calls `parse_variable_declaration_or_assignment` to handle variable-related statements.

2. **Function Definitions:**

   -  **`Token Type:`** `FN`
   -  Calls `parse_function` to handle function definitions.

3. **Control Flow Statements:**

   -  **`If Statements:`** Token type `IF`

      -  Calls `parse_if_statement` to handle `if` statements.

   -  **For Loops:** Token type `FOR`

      -  Calls `parse_for_statement` to handle `for` loops.

   -  **While Loops:** Token type `WHILE`

      -  Calls `parse_while_statement` to handle `while` loops.

   -  **Switch Statements:** Token type `SWITCH`

      -  Calls `parse_switch_statement` to handle `switch`
         statements.

4. **Return Statements:**

   -  **Token Type:** `RETURN`
   -  Calls `parse_return_statement` to handle return statements.

5. **Structures:**

   -  **Token Type:** `STRUCT`
   -  Calls parse_struct to handle `struct` definitions.

6. **Expression Statements:**

   -  **`Fallback:`** If none of the above tokens are matched, it
      defaults to `parse_expression_statement` to handle any remaining
      expressions.

| **Errors Raised:**
| - `SyntaxError`: Not directly raised in this method but could be
  raised by the called methods if there are issues with the statements
  being parsed.

parse_variable_declaration_or_assignment Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses either a variable declaration or an assignment statement based
  on the current token.

| **Parameters:**
| - None

| **Returns:**
| - `VariableDeclarationNode` or `AssignmentNode`: Returns a node
  representing either a variable declaration with an optional initial
  value or an assignment statement.

| **Method Details:**

1. **Variable Declaration:**

   - **Token Types:** `LET`, `VAR`
   - **Process:**
     - **Type:** Determines the variable type from the token (`LET` or `VAR`).
     - **Name:** Extracts the variable name from the next `IDENTIFIER` token.
     - **Type Annotation (Optional):** If a `COLON` is present, it indicates a type annotation, which is processed but not used further.
     - **Initial Value (Optional):** If an `EQUALS` token is present, it indicates the start of an initial value expression. The expression is parsed and assigned to the variable.
     - **Semicolon (Optional):** Consumes the `SEMICOLON` if it is present, marking the end of the statement.


2. **Assignment:**

   -  **`Fallback:`** If the current token does not indicate a
      variable declaration, it defaults to `parse_assignment` to
      handle assignment statements.

| **Errors Raised:**
| - `SyntaxError`: Not directly raised in this method but may be
  raised by `parse_expression` or `parse_assignment` if there are
  issues with the provided expressions or assignments.

parse_if_statement Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an `if` statement, including its optional `else` block.

| **Parameters:**
| - None

| **Returns:**
| - `IfNode`: Returns a node representing the parsed `if` statement,
  including its condition, `if` body, and optional `else` body.

| **Method Details:**

1. **Start Parsing:**

   - **Token Type:** `IF`
     - **Process:** Consumes the `IF` token to identify the start of the `if` statement.
   - **Left Parenthesis:** `LPAREN`
     - **Process:** Consumes the `LPAREN` token to start the condition expression.
   - **Condition Expression:**
     - **Method:** Calls `parse_expression` to parse the condition of the `if` statement.
   - **Right Parenthesis:** `RPAREN`
     - **Process:** Consumes the `RPAREN` token to close the condition expression.
   - **If Block:**
     - **Method:** Calls `parse_block` to parse the block of statements that execute if the condition is true.


2. **Optional Else Block:**

   -  **Token Type:** `ELSE`

      -  **`Process:`** If the next token is `ELSE`, it is consumed
         and the `else` block is parsed using `parse_block`.

3. **Return Statement:**

   -  **Returns:** An `IfNode` object with the condition, `if`
      body, and optionally the `else` body.

| **Errors Raised:**
| - `SyntaxError`: Not directly raised in this method but may be
  triggered by `parse_expression` or `parse_block` if there are
  issues with the syntax.

parse_for_statement Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `for` loop statement, including initialization, condition,
  update, and loop body.

| **Parameters:**
| - None

| **Returns:**
| - `ForNode`: Returns a node representing the parsed `for` loop
  statement, including its initialization, condition, update expression,
  and body.

| **Method Details:**

1. **Start Parsing:**

   - **Token Type:** `FOR`
     - **Process:** Consumes the `FOR` token to identify the start of the `for` loop statement.
   - **Left Parenthesis:** `LPAREN`
     - **Process:** Consumes the `LPAREN` token to start parsing the `for` loop components.


2. **Initialization:**

   -  **Method:** Calls `parse_variable_declaration_or_assignment`
      to parse the initialization expression of the loop (e.g., variable
      declarations or assignments).
   -  **Token Type:** `SEMICOLON`

      -  **Process:** Consumes the `SEMICOLON` token to separate
         initialization from the loop condition.

3. **Condition:**

   -  **Method:** Calls `parse_expression` to parse the loop
      condition.
   -  **Token Type:** `SEMICOLON`

      -  **Process:** Consumes the `SEMICOLON` token to separate the
         condition from the update expression.

4. **Update:**

   -  **Method:** Calls `parse_expression` to parse the update
      expression (e.g., increment or decrement).
   -  **Token Type:** `RPAREN`

      -  **Process:** Consumes the `RPAREN` token to close the `for`
         loop header.

5. **Body:**

   -  **Method:** Calls `parse_block` to parse the block of statements
      that execute during each iteration of the loop.

6. **Return Statement:**

   -  **Returns:** A `ForNode` object with initialization, condition,
      update expression, and body.

| **Errors Raised:**
| - `SyntaxError`: Not directly raised in this method but may be
  triggered by `parse_variable_declaration_or_assignment`,
  `parse_expression`, or `parse_block` if there are issues with the
  syntax.

parse_while_statement Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `while` loop statement, including its condition and loop
  body.

| **Parameters:**
| - None

| **Returns:**
| - `WhileNode`: Returns a node representing the parsed `while` loop
  statement, including its condition and body.

**Method Details:**

1. **Start Parsing:**

   - **Token Type:** `WHILE`
     - **Process:** Consumes the `WHILE` token to identify the start of the `while` loop statement.
   - **Left Parenthesis:** `LPAREN`
     - **Process:** Consumes the `LPAREN` token to start parsing the loop condition.


2. **Condition:**

   -  **Method:** Calls `parse_expression` to parse the loop condition
      (the expression that controls the loop’s execution).
   -  **Token Type:** `RPAREN`

      -  **Process:** Consumes the `RPAREN` token to close the
         condition.

3. **Body:**

   -  **Method:** Calls `parse_block` to parse the block of statements
      that execute as long as the condition is true.

4. **Return Statement:**

   -  **Returns:** A `WhileNode` object with the condition and body of
      the `while` loop.

| **Errors Raised:**
| - `SyntaxError`: Not directly raised in this method but may be
  triggered by `parse_expression` or `parse_block` if there are
  syntax issues.

`parse_switch_statement` Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `switch` statement, including its expression and cases.

| **Parameters:**
| - None

| **Returns:**
| - `SwitchNode`: Returns a node representing the parsed `switch`
  statement, including its expression and cases.

| **Method Details:**

1. **Start Parsing:**

   - **Token Type:** `SWITCH`
     - **Process:** Consumes the `SWITCH` token to identify the start of the `switch` statement.
   - **Left Parenthesis:** `LPAREN`
     - **Process:** Consumes the `LPAREN` token to begin parsing the `switch` expression.


2. **Expression:**

   -  **Method:** Calls `parse_expression` to parse the expression
      that the `switch` statement evaluates.
   -  **Token Type:** `RPAREN`

      -  **Process:** Consumes the `RPAREN` token to close the
         expression.

3. **Block:**

   -  **Left Brace:** `LBRACE`

      -  **Process:** Consumes the `LBRACE` token to start parsing the
         block of cases.

4. **Cases:**

   -  **Method:** Calls `parse_switch_case` to parse each case within
      the `switch` block.
   -  **Loop:** Continues to parse cases until encountering a `RBRACE`
      token.

5. **End of Block:**

   -  **Right Brace:** `RBRACE`

      -  **Process:** Consumes the `RBRACE` token to close the
         `switch` block.

6. **Return Statement:**

   -  **Returns:** A `SwitchNode` object with the `switch`
      expression and a list of cases.

| **Errors Raised:**
| - `SyntaxError`: Not directly raised in this method but may be
  triggered by `parse_expression` or `parse_switch_case` if there
  are syntax issues.

parse_switch_case Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `case` or `default` branch within a `switch` statement.

| **Parameters:**
| - None

| **Returns:**
| - `SwitchCaseNode`: Returns a node representing the parsed `case`
  or `default` branch, including its condition (if applicable) and
  block of statements.

| **Method Details:**

1. **Case Branch:**

   - **Token Type:** `CASE`
     - **Process:** Consumes the `CASE` token to start parsing a `case` branch.
   - **Expression:**
     - **Method:** Calls `parse_expression` to parse the condition for the `case`.
   - **Colon:** `COLON`
     - **Process:** Consumes the `COLON` token to separate the condition from the block of statements.
   - **Block:**
     - **Method:** Calls `parse_block` to parse the statements that follow the `case` condition.


2. **Default Branch:**

   -  **Token Type:** `DEFAULT`

      -  **Process:** Consumes the `DEFAULT` token to start parsing
         the default branch.

   -  **Colon:** `COLON`

      -  **Process:** Consumes the `COLON` token to separate the
         `default` from the block of statements.

   -  **Block:**

      -  **Method:** Calls `parse_block` to parse the statements that
         follow the `default` keyword.

3. **Error Handling:**

   -  **SyntaxError:** Raises an error if the token does not match
      `CASE` or `DEFAULT`.

| **Errors Raised:**
| - `SyntaxError`: If the token is not `CASE` or `DEFAULT`.

`parse_return_statement` Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a `return` statement within a function, which specifies the
  value to be returned.

| **Parameters:**
| - None

| **Returns:**
| - `ReturnNode`: Returns a node representing the `return`
  statement, including the value to be returned.

| **Method Details:**
| 1. **Return Keyword:** - **Token Type:** `RETURN` - **Process:**
  Consumes the `RETURN` token to start parsing the return statement.

2. **Expression:**

   -  **Method:** Calls `parse_expression` to parse the value or
      expression to be returned.

3. **Semicolon:**

   -  **Token Type:** `SEMICOLON` (optional)

      -  **Process:** Consumes the `SEMICOLON` token if present to
         terminate the return statement.

parse_expression_statement Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an expression statement, which consists of a single expression
  followed by a semicolon.

| **Parameters:**
| - None

| **Returns:**
| - `ExpressionNode`: Returns the parsed expression node.

| **Method Details:**
| 1. **Expression:** - **Method:** Calls `parse_expression` to parse
  the expression part of the statement.

2. **Semicolon:**

   -  **Token Type:** `SEMICOLON`

      -  **Process:** Consumes the `SEMICOLON` token to complete the
         statement.

| **Errors Raised:**
| - **SyntaxError:** If the `SEMICOLON` token is not present after the
  expression.

.. _parse_expression-method-1:

parse_expression Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an expression, which can be an assignment or other types of
  expressions depending on the implementation of `parse_assignment`.

| **Parameters:**
| - None

| **Returns:**
| - `AssignmentNode` or other expression node types: Returns the
  result of parsing an assignment or expression.

| **Method Details:**
| 1. **Delegation:** - **Method:** Calls `parse_assignment` to handle
  the parsing of assignments and potentially other expressions.

| **Errors Raised:**
| - **SyntaxError:** Depending on the implementation of
  `parse_assignment`, it may raise errors related to invalid syntax or
  tokens.

.. _parse_assignment-method-1:

parse_assignment Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses an assignment expression, including assignments with compound
  operators and ternary conditional expressions.

| **Parameters:**
| - None

| **Returns:**
| - `AssignmentNode` or `TernaryOpNode`: Returns an
  `AssignmentNode` if an assignment is parsed, or a `TernaryOpNode`
  if a ternary operation is detected.

| **Method Details:**
| 1. **Initial Parsing:** - **Method:** Starts by parsing the left-hand
  side of the assignment using `parse_logical_or`.

2. **Assignment Operators Handling:**

   -  **Condition:** Checks for assignment operators (`EQUALS`,
      `PLUS_EQUALS`, `MINUS_EQUALS`, `MULTIPLY_EQUALS`,
      `DIVIDE_EQUALS`).
   -  **Action:** If an assignment operator is found, it captures the
      operator and parses the right-hand side recursively.
   -  **Return:** Returns an `AssignmentNode` that encapsulates the
      left-hand side, right-hand side, and operator.

3. **Ternary Conditional Expressions Handling:**

   -  **Condition:** If a ternary operator (`QUESTION`) is found after
      the initial left-hand side parsing.
   -  **Action:** Parses the true and false branches of the ternary
      expression.
   -  **Return:** Returns a `TernaryOpNode` if a ternary operation is
      detected.

4. **Fallback:**

   -  **Return:** Returns the parsed left-hand side if no assignment or
      ternary operation is found.

| **Errors Raised:**
| - **SyntaxError:** May raise errors during parsing if unexpected
  tokens are encountered.

parse_logical_or Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses logical OR expressions, handling multiple chained OR
  operations.

| **Parameters:**
| - None

| **Returns:**
| - `BinaryOpNode`: Returns a `BinaryOpNode` representing the
  logical OR expression.

| **Method Details:**
| 1. **Initial Parsing:** - **Method:** Begins by parsing the left-hand
  side of the OR expression using `parse_logical_and`.

2. **Chained OR Handling:**

   -  **Condition:** Checks if the current token is an `OR` operator.
   -  **Action:** If an `OR` operator is found, it captures the
      operator, then parses the right-hand side of the OR expression
      using `parse_logical_and`.
   -  **Update:** Updates the `left` operand to a `BinaryOpNode`
      that combines the current `left` and `right` with the `OR`
      operator.

3. **Loop:**

   -  **Action:** Repeats the process to handle additional chained OR
      operators, if present.

4. **Return:**

   -  **Return:** Returns the final `BinaryOpNode` representing the
      logical OR expression.

| **Errors Raised:**
| - **SyntaxError:** May raise errors if unexpected tokens are
  encountered, although not explicitly handled in this method.

parse_logical_and Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses logical AND expressions, handling multiple chained AND
  operations.

| **Parameters:**
| - None

| **Returns:**
| - `BinaryOpNode`: Returns a `BinaryOpNode` representing the
  logical AND expression.

| **Method Details:**
| 1. **Initial Parsing:** - **Method:** Begins by parsing the left-hand
  side of the AND expression using `parse_equality`.

2. **Chained AND Handling:**

   -  **Condition:** Checks if the current token is an `AND` operator.
   -  **Action:** If an `AND` operator is found, it captures the
      operator, then parses the right-hand side of the AND expression
      using `parse_equality`.
   -  **Update:** Updates the `left` operand to a `BinaryOpNode`
      that combines the current `left` and `right` with the `AND`
      operator.

3. **Loop:**

   -  **Action:** Repeats the process to handle additional chained AND
      operators, if present.

4. **Return:**

   -  **Return:** Returns the final `BinaryOpNode` representing the
      logical AND expression.

| **Errors Raised:**
| - **SyntaxError:** May raise errors if unexpected tokens are
  encountered, although not explicitly handled in this method.

parse_equality Method
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses equality expressions, handling both equality (`==`) and
  inequality (`!=`) operations.

| **Parameters:**
| - None

| **Returns:**
| - `BinaryOpNode`: Returns a `BinaryOpNode` representing the
  equality or inequality expression.

| **Method Details:**
| 1. **Initial Parsing:** - **Method:** Begins by parsing the left-hand
  side of the equality expression using `parse_relational`.

2. **Chained Equality Handling:**

   -  **Condition:** Checks if the current token represents an equality
      (`==`) or inequality (`!=`) operator.
   -  **Action:** If such an operator is found, it captures the
      operator, then parses the right-hand side of the equality
      expression using `parse_relational`.
   -  **Update:** Updates the `left` operand to a `BinaryOpNode`
      that combines the current `left` and `right` with the equality
      or inequality operator.

3. **Loop:**

   -  **Action:** Continues to handle additional chained equality or
      inequality operators, if present.

4. **Return:**

   -  **Return:** Returns the final `BinaryOpNode` representing the
      equality or inequality expression.

| **Errors Raised:**
| - **SyntaxError:** May raise errors if unexpected tokens are
  encountered, although not explicitly handled in this method.

parse_relational Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses relational expressions, handling operations such as less than
  (`<`), greater than (`>`), less than or equal to (`<=`), and
  greater than or equal to (`>=`).

| **Parameters:**
| - None

| **Returns:**
| - `BinaryOpNode`: Returns a `BinaryOpNode` representing the
  relational expression.

| **Method Details:**
| 1. **Initial Parsing:** - **Method:** Begins by parsing the left-hand
  side of the relational expression using `parse_additive`.

2. **Chained Relational Handling:**

   -  **Condition:** Checks if the current token represents a relational
      operator (`<`, `>`, `<=`, `>=`).
   -  **Action:** If such an operator is found, it captures the
      operator, then parses the right-hand side of the relational
      expression using `parse_additive`.
   -  **Update:** Updates the `left` operand to a `BinaryOpNode`
      that combines the current `left` and `right` with the
      relational operator.

3. **Loop:**

   -  **Action:** Continues to handle additional chained relational
      operators, if present.

4. **Return:**

   -  **Return:** Returns the final `BinaryOpNode` representing the
      relational expression.

| **Errors Raised:**
| - **SyntaxError:** May raise errors if unexpected tokens are
  encountered, although not explicitly handled in this method.

.. _parse_additive-method-1:

parse_additive Method
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses additive expressions, handling addition (`+`) and subtraction
  (`-`) operations.

| **Parameters:**
| - None

| **Returns:**
| - `BinaryOpNode`: Returns a `BinaryOpNode` representing the
  additive expression.

| **Method Details:**
| 1. **Initial Parsing:** - **Method:** Begins by parsing the left-hand
  side of the additive expression using `parse_multiplicative`.

2. **Chained Additive Handling:**

   -  **Condition:** Checks if the current token represents an additive
      operator (`+`, `-`).
   -  **Action:** If such an operator is found, it captures the
      operator, then parses the right-hand side of the additive
      expression using `parse_multiplicative`.
   -  **Update:** Updates the `left` operand to a `BinaryOpNode`
      that combines the current `left` and `right` with the additive
      operator.

3. **Loop:**

   -  **Action:** Continues to handle additional chained additive
      operators, if present.

4. **Return:**

   -  **Return:** Returns the final `BinaryOpNode` representing the
      additive expression.

| **Errors Raised:**
| - **SyntaxError:** May raise errors if unexpected tokens are
  encountered, although not explicitly handled in this method.

.. _parse_multiplicative-method-1:

parse_multiplicative Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses multiplicative expressions, handling multiplication (`*`) and
  division (`/`) operations.

| **Parameters:**
| - None

| **Returns:**
| - `BinaryOpNode`: Returns a `BinaryOpNode` representing the
  multiplicative expression.

| **Method Details:**
| 1. **Initial Parsing:** - **Method:** Begins by parsing the left-hand
  side of the multiplicative expression using `parse_unary`.

2. **Chained Multiplicative Handling:**

   -  **Condition:** Checks if the current token represents a
      multiplicative operator (`*`, `/`).
   -  **Action:** If such an operator is found, it captures the
      operator, then parses the right-hand side of the multiplicative
      expression using `parse_unary`.
   -  **Update:** Updates the `left` operand to a `BinaryOpNode`
      that combines the current `left` and `right` with the
      multiplicative operator.

3. **Loop:**

   -  **Action:** Continues to handle additional chained multiplicative
      operators, if present.

4. **Return:**

   -  **Return:** Returns the final `BinaryOpNode` representing the
      multiplicative expression.

| **Errors Raised:**
| - **SyntaxError:** May raise errors if unexpected tokens are
  encountered, although not explicitly handled in this method.

parse_unary Method
~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses unary operations, such as unary plus (`+`) and unary minus
  (`-`), and delegates to `parse_primary` for other expressions.

| **Parameters:**
| - None

| **Returns:**
| - `UnaryOpNode` or result of `parse_primary`: Returns a
  `UnaryOpNode` for unary operations or the result of
  `parse_primary` for other expressions.

| **Method Details:**
| 1. **Unary Operation Handling:** - **Condition:** Checks if the
  current token represents a unary operator (`+`, `-`). -
  **Action:** If a unary operator is found, it captures the operator and
  recursively parses the operand using `parse_unary`. - **Return:**
  Creates and returns a `UnaryOpNode` with the captured operator and
  the parsed operand.

2. **Primary Expression Handling:**

   -  **Condition:** If no unary operator is present, delegates to
      `parse_primary` to handle the expression.
   -  **Return:** Returns the result of `parse_primary`, which handles
      basic expressions (e.g., literals, variables).

| **Errors Raised:**
| - **SyntaxError:** May raise errors if unexpected tokens are
  encountered, although not explicitly handled in this method.

.. _parse_primary-method-1:

parse_primary Method
~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses primary expressions, which include literals, variables, type
  annotations, and function calls.

| **Parameters:**
| - None

| **Returns:**
| - A `VariableNode`, a literal value, or a parsed function call or
  identifier.

**Method Details:**

1. **Literals and Variables:**

   -  **Condition:** Checks if the current token is a literal type
      (`INT`, `FLOAT`, `BOOL`, `STRING`) or `NUMBER`.

      -  **Action:**

         -  For literal types, if followed by an `IDENTIFIER`, it
            creates a `VariableNode` with optional type annotation.
         -  For `NUMBER`, it returns the literal value.

      -  **Return:** Constructs and returns a `VariableNode` or
         literal value.

2. **Parentheses Handling:**

   -  **Condition:** Checks if the current token is an opening
      parenthesis (`LPAREN`).

      -  **Action:** If so, it parses the enclosed expression and
         expects a closing parenthesis (`RPAREN`).
      -  **Return:** Returns the parsed expression enclosed by
         parentheses.

3. **Function Calls or Identifiers:**

   -  **Condition:** Handles cases where the current token indicates a
      function call or an identifier.

      -  **Action:** Calls `parse_function_call_or_identifier` to
         parse further.
      -  **Return:** Result of `parse_function_call_or_identifier`.

4. **Top-Level Keywords:**

   -  **Condition:** If the current token is a top-level keyword
      (`FN`, `STRUCT`, `CLASS`, `LET`, `VAR`).

      -  **Action:** Raises a `SyntaxError` since such keywords should
         not appear in expressions.

5. **Unexpected Tokens:**

   -  **Condition:** Handles any unexpected token.

      -  **Action:** Raises a `SyntaxError` for unexpected tokens in
         the expression context.

**Errors Raised:** - **SyntaxError:** Raised for unexpected tokens
or top-level keywords encountered in the expression context.

parse_vector_constructor Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Description:**
| Parses a vector constructor expression from the current token stream.
  This typically involves handling a list of expressions enclosed in
  parentheses, representing the components of a vector.

| **Parameters:**
| - **`type_name:`** A string representing the type of the vector
  (e.g., `vec2`, `vec3`).

| **Returns:**
| - A `VectorConstructorNode` instance with the vector type and its
  components.

**Method Details:**

1. **Opening Parenthesis:**

   -  **Condition:** Checks if the current token is an opening
      parenthesis (`LPAREN`).
   -  **Action:** Eats the `LPAREN` token.

2. **Parsing Arguments:**

   -  **Action:** Initializes an empty list `args` to store the
      components of the vector.
   -  **Loop:** While the current token is not a closing parenthesis
      (`RPAREN`):

      -  **Action:** Parses an expression and appends it to `args`.
      -  **Condition:** If a comma (`COMMA`) follows an expression,
         eats the comma.

3. **Closing Parenthesis:**

   -  **Condition:** Checks if the current token is a closing
      parenthesis (`RPAREN`).
   -  **Action:** Eats the `RPAREN` token.

4. **Return Statement:**

   -  **Return:** Constructs and returns a `VectorConstructorNode`
      with `type_name` and the parsed `args`.

**Errors Raised:** - **None:** The method assumes correct syntax for
vector constructors and handles it accordingly. However, additional
error handling may be required if the input is not as expected.

**parse_function_call Method**

-  **Description:**

   -  Parses function call expressions from the current token stream.
      This involves handling function arguments enclosed in parentheses.

-  **Parameters:**

   -  `name`: The name of the function being called.

-  **Returns:**

   -  A `FunctionCallNode` instance representing the function call
      with its arguments.

-  **Method Details:**

   1. **Opening Parenthesis:**

      -  **Condition:** Checks if the current token is an opening
         parenthesis (`LPAREN`).
      -  **Action:** Eats the `LPAREN` token.

   2. **Parsing Arguments:**

      -  Initializes an empty list `args` to store the function
         arguments.
      -  While the current token is not a closing parenthesis
         (`RPAREN`):

         -  Parses an expression and appends it to `args`.
         -  If a comma (`COMMA`) follows an expression, eats the
            comma.

   3. **Closing Parenthesis:**

      -  **Condition:** Checks if the current token is a closing
         parenthesis (`RPAREN`).
      -  **Action:** Eats the `RPAREN` token.

   4. **Return Statement:**

      -  Constructs and returns a `FunctionCallNode` with the
         specified `name` and the parsed `args`.

-  **Errors Raised:**

   -  None: The method assumes correct syntax for function calls and
      handles it accordingly. Additional error handling may be required
      if the input is not as expected.

**parse_member_access Method**

-  **Description:**

   -  Parses member access expressions from the current token stream.
      This involves handling dot notation for accessing object members
      (e.g., `object.member`).

-  **Parameters:**

   -  `object`: The object from which the member is accessed.

-  **Returns:**

   -  A `MemberAccessNode` instance representing the accessed member.

-  **Method Details:**

   1. **Dot Token:**

      -  **Condition:** Checks if the current token is a dot
         (`DOT`).
      -  **`Action:`** Eats the dot token.

   2. **Member Identifier:**

      -  **Condition:** Ensures that the next token is an identifier
         (`IDENTIFIER`).
      -  **`Action:`** Retrieves the member name from the current
         token.
      -  **`Action:`** Eats the identifier token.

   3. **Function Call Check:**

      -  **Condition:** If the next token is an opening parenthesis
         (`LPAREN`), it indicates a function call.
      -  **`Action:`** Calls the `parse_function_call` method with
         the member name.

   4. **Nested Member Access Check:**

      -  **Condition:** If the next token is another dot (`DOT`),
         it indicates nested member access.
      -  **`Action:`** Recursively calls the `parse_member_access`
         method with the updated `MemberAccessNode`.

   5. **Return Statement:**

      -  Constructs and returns a `MemberAccessNode` with the
         specified `object` and the parsed `member`.

-  **Errors Raised:**

   -  None: The method assumes correct syntax for member access and
      handles it accordingly. Additional error handling may be required
      if the input is not as expected.

**parse_decorator Method**

-  **Description:**

   -  Parses decorator expressions from the current token stream.
      Decorators are typically used in Python to modify or enhance
      functions or classes.

-  **Returns:**

   -  A `DecoratorNode` instance representing the decorator with its
      name and arguments (if any).

-  **Method Details:**

   1. **Decorator Token:**

      -  **Condition:** Checks if the current token is a decorator
         (`DECORATOR`).
      -  **`Action:`** Eats the decorator token.

   2. **Decorator Name:**

      -  Retrieves the decorator name from the current token.

   3. **Parsing Arguments (if present):**

      -  If the next token is an opening parenthesis (`LPAREN`), it
         indicates decorator arguments.
      -  Initializes an empty list `args` to store the decorator
         arguments.
      -  While the current token is not a closing parenthesis
         (`RPAREN`):

         -  Parses an expression and appends it to `args`.
         -  If a comma (`COMMA`) follows an expression, eats the
            comma.

      -  Eats the closing parenthesis (`RPAREN`).

   4. **Return Statement:**

      -  Constructs and returns a `DecoratorNode` with the specified
         `name` and the parsed `args`.

-  **Errors Raised:**

   -  None: The method assumes correct syntax for decorators and handles
      it accordingly. Additional error handling may be required if the
      input is not as expected.
