Product Documentation Workflow
==============================

This site is organized so product documentation can be developed in parallel.

Ownership rules
---------------

Each product owns one folder under ``docs/source/products``. Add product pages
inside that folder and keep generated or product-specific support files next to
that product when possible.

The shared landing page already discovers products with a globbed toctree. In
normal product work, avoid editing ``docs/source/index.rst``.

Recommended product layout
--------------------------

Use this shape for new products:

.. code-block:: text

   docs/source/products/<product>/
   ├── index.rst
   ├── getting-started.rst
   ├── architecture.rst
   └── api.rst

If a product needs Doxygen, place its Doxygen config under
``docs/doxygen/<product>/`` and write build output under
``docs/doxygen/build/<product>/`` so generated files stay out of source control.
