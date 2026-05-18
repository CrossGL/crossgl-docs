Doxygen XML
===========

The docs build can generate Doxygen XML for CrossGL Translator and expose it to
Sphinx through Breathe.

Generate the XML from the documentation repo root:

.. code-block:: bash

   make doxygen

The Doxygen configuration writes generated files to
``docs/doxygen/build/crossgl-translator/xml``. That directory is ignored by git
and can be regenerated at any time.

When Doxygen XML exists, Breathe is configured with the project name
``crossgl-translator`` for future low-level reference pages.
