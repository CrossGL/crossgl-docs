# Doxygen Outputs

This directory is reserved for product-specific Doxygen configuration and generated XML.

Use one subdirectory per product:

```text
docs/doxygen/<product-slug>/
```

Generated `html/` and `xml/` directories are ignored by git. Commit product-specific Doxygen configuration only when the shared site needs to consume it.
