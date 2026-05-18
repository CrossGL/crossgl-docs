# Overview

Dyson exposes two main product surfaces:

- A Python package for routing local functions or C++ snippets to remote compute targets.
- A serverless execution API for submitting isolated workloads and retrieving results.

The product documentation should stay focused on how users evaluate, configure, and operate Dyson. Source-derived API details belong in the Dyson repository's generated documentation so they stay close to the code and module docstrings.

## Documentation Ownership

Dyson-specific content in this repository lives under `docs/source/products/dyson/`. Shared build settings live outside the product subtree and should only change when the shared site behavior changes.
