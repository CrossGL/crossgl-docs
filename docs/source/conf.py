from __future__ import annotations

import os
import sys
import types
from datetime import date
from pathlib import Path

DOCS_REPO = Path(__file__).resolve().parents[2]
WORKSPACE = DOCS_REPO.parent


def add_source_path(env_name: str, *candidates: Path) -> Path | None:
    configured = os.getenv(env_name)
    paths = [Path(configured)] if configured else []
    paths.extend(candidates)
    for path in paths:
        resolved = path.expanduser().resolve()
        if resolved.exists():
            sys.path.insert(0, str(resolved))
            return resolved
    return None


def product_index_exists(slug: str) -> bool:
    product_dir = DOCS_REPO / "docs" / "source" / "products" / slug
    return any((product_dir / f"index.{suffix}").exists() for suffix in ("rst", "md"))


crossgl_translator_source = add_source_path(
    "CROSSGL_TRANSLATOR_SOURCE",
    DOCS_REPO / "_external" / "CrossGL-Translator",
    WORKSPACE / "CrossGL-Translator",
)
dyson_source = add_source_path(
    "DYSON_SOURCE",
    DOCS_REPO / "_external" / "dyson",
    WORKSPACE / "dyson",
)
infrintia_source = add_source_path(
    "INFRINTIA_SOURCE",
    DOCS_REPO / "_external" / "infrintia",
    WORKSPACE / "infrintia",
)
enable_infrintia_autoapi = bool(infrintia_source and product_index_exists("infrintia"))

try:
    import dill  # noqa: F401
except ImportError:
    dill_stub = types.ModuleType("dill")
    dill_stub.settings = {}
    dill_stub.dumps = lambda value: b""
    dill_stub.loads = lambda value: None
    sys.modules["dill"] = dill_stub

project = "CrossGL Documentation"
author = "CrossGL"
copyright = f"{date.today():%Y}, CrossGL"

extensions = [
    "breathe",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

if enable_infrintia_autoapi:
    extensions.append("autoapi.extension")
    tags.add("has_infrintia_source")

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

html_theme = "furo"
html_title = "CrossGL Docs"
html_static_path = ["_static"]
html_css_files = ["crossgl.css", "custom.css"]

autodoc_default_options = {
    "show-inheritance": True,
}
autosummary_generate = True
autodoc_mock_imports = [
    "accelerate",
    "asyncpg",
    "firebase_admin",
    "fastapi",
    "google",
    "google.auth",
    "google.cloud",
    "google.cloud.sql.connector",
    "httpx",
    "langchain_community",
    "langchain_core",
    "langchain_huggingface",
    "numpy",
    "pydantic",
    "redis",
    "sqlalchemy",
    "starlette",
    "structlog",
    "tensorflow",
    "torch",
    "tqdm",
    "transformers",
    "uvicorn",
]
suppress_warnings = [
    "sphinx_autodoc_typehints.forward_reference",
    "docutils",
]

breathe_projects = {
    "crossgl-translator": str(
        DOCS_REPO / "docs" / "doxygen" / "build" / "crossgl-translator" / "xml"
    ),
    "dyson": str(DOCS_REPO / "docs" / "doxygen" / "build" / "dyson" / "xml"),
    "infrintia": str(DOCS_REPO / "docs" / "doxygen" / "build" / "infrintia" / "xml"),
}
breathe_default_project = "crossgl-translator"

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

if enable_infrintia_autoapi:
    autoapi_type = "python"
    autoapi_dirs = [
        str(infrintia_source / "app"),
        str(infrintia_source / "host_agent"),
        str(infrintia_source / "sdk"),
    ]
    autoapi_root = "products/infrintia/autoapi"
    autoapi_add_toctree_entry = True
    autoapi_keep_files = False
    autoapi_options = [
        "members",
        "undoc-members",
        "show-inheritance",
        "show-module-summary",
        "imported-members",
    ]
    autoapi_ignore = [
        "*/.mypy_cache/*",
        "*/.pytest_cache/*",
        "*/.ruff_cache/*",
        "*/__pycache__/*",
        "*/tests/*",
        "*/venv/*",
        "*/worker_envs/*",
    ]
