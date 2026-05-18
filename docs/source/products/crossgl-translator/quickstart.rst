Quickstart
==========

Install the translator package in editable mode from the product repository:

.. code-block:: bash

   pip install -e ../CrossGL-Translator

Translate a CrossGL shader from Python:

.. code-block:: python

   import crosstl

   output = crosstl.translate("examples/graphics/SimpleShader.cgl", backend="metal")
   print(output)

Or use the command-line interface:

.. code-block:: bash

   python -m crosstl._crosstl examples/graphics/SimpleShader.cgl --backend metal

Supported targets are registered through ``crosstl.translator.codegen`` and can
be inspected at runtime:

.. code-block:: python

   import crosstl

   print(crosstl.supported_backends())
   print(crosstl.supported_sources())
