# CrossGL Documentation

This repository builds the public documentation site for CrossGL products.

The site is intentionally structured so product teams can work in parallel:

- Shared Sphinx configuration lives in `docs/source/conf.py`.
- Product documentation lives under `docs/source/products/<product-slug>/`.
- The product index uses a globbed toctree, so adding a new product subtree does not require editing shared navigation.
- Product-specific Doxygen configuration or generated XML should live under `docs/doxygen/<product-slug>/`.

## Build locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
make strict
```

The rendered site is written to `docs/_build/html`.

## Product Sources

The Sphinx build can read product source trees from either sibling checkouts or
CI checkouts under `_external/`:

- `../CrossGL-Translator` or `_external/CrossGL-Translator`
- `../dyson` or `_external/dyson`
- `../infrintia` or `_external/infrintia`

Override paths with the matching source environment variable, such as
`CROSSGL_TRANSLATOR_SOURCE`, `DYSON_SOURCE`, or `INFRINTIA_SOURCE`, when building
from a different workspace layout.
