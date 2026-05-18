Architecture
============

CrossGL Translator is built around a two-direction pipeline.

Source ingestion
----------------

Source registries map file extensions and source names to lexer/parser pairs.
Native shader inputs such as HLSL, Metal, GLSL, Vulkan-style SPIR-V text
representations, CUDA, HIP, Rust, Mojo, and Slang can be parsed into backend
ASTs and converted back into CrossGL where reverse code generation exists.

CrossGL frontend
----------------

The CrossGL lexer and parser produce the canonical translator AST used by
target code generators. The AST lives in ``crosstl.translator.ast`` and keeps
shader stages, declarations, statements, expressions, resource bindings, and
backend attributes in one representation.

Target generation
-----------------

Backend generators under ``crosstl.translator.codegen`` consume the CrossGL AST
and emit target code. The registry normalizes backend aliases, resolves file
extensions, and lets plugins add new targets without changing the public
``crosstl.translate`` entry point.
