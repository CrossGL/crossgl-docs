Python API Reference
====================

The generated Python reference is built from the Infrintia source tree with
Sphinx AutoAPI. It covers the broker package, host agent package, and SDK
package without importing heavy runtime dependencies during documentation
generation.

.. only:: has_infrintia_source

   .. toctree::
      :maxdepth: 2

      autoapi/index

.. only:: not has_infrintia_source

   The Infrintia source checkout was not found. Set ``INFRINTIA_SOURCE`` or
   place the repo at ``../infrintia`` before building this page.
