# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import importlib
import inspect

sys.path.insert(0, os.path.abspath('../../src'))    # 変換するソースコードがある場所を指定

project = 'koyurun'
copyright = '2024, koyuru'
author = 'koyuru'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',   # ソースコード読み込み用
    'sphinx.ext.napoleon',  # docstring パース用
    'sphinx.ext.linkcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "github_url": "https://github.com/Sassor/ssr-sv-enes-ana-v2",
}
html_static_path = ['_static']


def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None

    try:
        obj = importlib.import_module(info['module'])
        for part in info['fullname'].split('.'):
            obj = getattr(obj, part)
        sourcelines = inspect.getsourcelines(obj)
        startline = sourcelines[1]
        endline = startline + len(sourcelines[0]) - 1
    except Exception:
        return None

    filename = info['module'].replace('.', '/')

    print(f"Filename: {filename}")
    print(f"Sourceline: {sourcelines}")

    return f"https://github.com/honjoshosi/koyurun/tree/main/src/{filename}.py#L{startline}-L{endline}"
