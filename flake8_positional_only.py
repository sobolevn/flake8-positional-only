# -*- coding: utf-8 -*-

import ast
from typing import Iterator, List, Tuple

import pkg_resources

#: Name of our package in `pyproject.toml`:
pkg_name = "flake8-positional-only"

#: We store the version number inside the `pyproject.toml`:
pkg_version: str = pkg_resources.get_distribution(pkg_name).version


class _ArgumentsVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.violations: List[ast.arguments] = []

    def visit_arguments(self, node) -> None:
        positional_args = getattr(node, "posonlyargs", [])
        if positional_args:
            self.violations.append(positional_args[0])
        self.generic_visit(node)


class Checker(object):
    """Entrypoint to the app."""

    _FPO100 = "FP0100 Found positional-only arguments"

    name = pkg_name
    version = pkg_version

    def __init__(self, tree: ast.AST) -> None:
        """We request ``ast`` tree from ``flake8`` API."""
        self._tree = tree

    def run(self) -> Iterator[Tuple[int, int, str, type]]:
        """Returns found violations one by one."""
        visitor = _ArgumentsVisitor()
        visitor.visit(self._tree)

        for violation in visitor.violations:
            yield (
                violation.lineno,
                violation.col_offset,
                self._FPO100,
                type(self),
            )
