# -*- coding: utf-8 -*-

import sys
import subprocess

ERROR_COUNT = 5 if sys.python_version >= (3.8) else 0


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


def test_incorrect_fixture(absolute_path):
    """End-to-End test to check that incorrect code raises warning."""
    filename = absolute_path('fixtures', 'incorrect.py')
    process = subprocess.Popen(
        ['flake8', '--disable-noqa', '--select', 'FPO', filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, _ = process.communicate()

    assert stdout.count(b'FPO100') == ERROR_COUNT, stdout


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
