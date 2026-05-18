Doxygen XML
===========

The Infrintia docs include Doxygen configuration so low-level API references can
be generated alongside Sphinx output when Doxygen is available.

Generate XML from the documentation repo root:

.. code-block:: bash

   make doxygen

The product configuration writes generated files to
``docs/doxygen/build/infrintia/xml``. Generated XML is ignored by git and can be
rebuilt at any time.

.. only:: has_infrintia_source

   Sphinx is configured with the Breathe project name ``infrintia``. Future
   pages can embed Doxygen directives with ``:project: infrintia``.

.. only:: not has_infrintia_source

   The Infrintia source checkout was not found. Set ``INFRINTIA_SOURCE`` or
   place the repo at ``../infrintia`` before generating XML.
