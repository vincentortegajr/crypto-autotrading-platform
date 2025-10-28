#!/usr/bin/env python3
"""Launch the imagesorcery-mcp server as a module.

This wrapper exists because FastMCP's PythonStdioTransport expects a script
path ending with `.py`, while the package's console script entry point is the
module `imagesorcery_mcp`. Running the module via runpy preserves relative
imports inside the package.
"""

from runpy import run_module


def main() -> None:
    run_module("imagesorcery_mcp", run_name="__main__")


if __name__ == "__main__":
    main()
