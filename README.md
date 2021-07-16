# flake8-positional-only

[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![Build Status](https://travis-ci.org/sobolevn/flake8-positional-only.svg?branch=master)](https://travis-ci.org/sobolevn/flake8-positional-only)
[![Coverage](https://coveralls.io/repos/github/sobolevn/flake8-positional-only/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/flake8-positional-only?branch=master) [![Python Version](https://img.shields.io/pypi/pyversions/flake8-positional-only.svg)](https://pypi.org/project/flake8-positional-only/)
[![PyPI version](https://badge.fury.io/py/flake8-positional-only.svg)](https://pypi.org/project/flake8-positional-only/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Flake8 plugin to forbid positional-only arguments in python3.8+

Why? Because they bring more confusion than help for a regular project.


## Installation

```bash
pip install flake8-positional-only
```


## Code example

What code is considered correct?

Any good old Python function and method definitions
with any parameters except positional-only parameters.

What code is considered incorrect?

```python
def function(param, /):
    ...
```

Basically, we forbid positional-only
arguments in functions, methods, generators, coroutines, and lambdas.
In other words: everywhere they can potentionally be defined.

We don't check how they are used:
you can still pass whatever parameters you want.


## Error codes

|  Error code  |           Description           |
|:------------:|:-------------------------------:|
|    FPO100    | Found positional-only arguments |


## License

MIT.
