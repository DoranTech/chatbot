Chatbot using OpenAI
====================

This chatbot is designed to be embeded into GUIs or other python scripts.


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

This package is intended to use Chat GPT 3.5 as an API. User needs an account and generating an API key [here](https://platform.openai.com/api-keys) and store it an environment variable named `OPENAI_API_KEY`

```
OPENAI_API_KEY=aa-b1b1b1b1b1b1
```


Begin by importing the chatb package

```python
import chatb
```

Testing
--------------------
Testing is performed using Tox. For more detailed information about the coverage use:

```
coverage report -m
```