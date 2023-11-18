Chatbot using OpenAI
====================

This chatbot is design to be embeded into GUIs or other python scripts.


## Development Setup
A virtual environment is needed to reproduce the same development environment for all developers. Python 3.10 is the recommanded version. This can be done using the following commands:
```shell
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements-dev.txt
pre-commit install
```

How To Use
--------------------

This package is intended to help understand the true cost of a mortgage. It also can help you easily compare between different mortgages.

Begin by importing the loan class

```python
from finance import balance_sheet
```

Testing
--------------------
Testing is performed using Tox. For more detailed information about the coverage use:

```
coverage report -m
```