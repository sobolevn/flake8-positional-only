# -*- coding: utf-8 -*-

import subprocess
import sys

import pytest


def test_correct_fixture(absolute_path):
    """End-to-End test to check that correct code works."""
    filename = absolute_path('fixtures', 'correct.py')
    process = subprocess.Popen(
        ['flake8', '--disable-noqa', '--select', 'FPO', filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = process.communicate()

    assert len(stdout) == 0, stdout


@pytest.mark.skipif(sys.version_info < (3, 8), reason='Syntax error')
def test_incorrect_fixture(absolute_path):
    """End-to-End test to check that incorrect code raises warning."""
    filename = absolute_path('fixtures', 'incorrect.py')
    process = subprocess.Popen(
        ['flake8', '--disable-noqa', '--select', 'FPO', filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = process.communicate()

    assert stdout.count(b'FPO100') == 5, stdout


@pytest.mark.skipif(sys.version_info < (3.8), reason='Syntax error')
def test_incorrect_fixture_noqa(absolute_path):
    """Checks that incorrect code does not raise warning with noqa."""
    filename = absolute_path('fixtures', 'incorrect.py')
    process = subprocess.Popen(
        ['flake8', '--select', 'FPO', filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = process.communicate()

    assert len(stdout) == 0, stdout
