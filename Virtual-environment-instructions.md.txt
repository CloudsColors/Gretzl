# Source GENERAL: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
# Source REQUIREMENTS: https://pip.pypa.io/en/latest/user_guide/#requirements-files

### Summary

- pip install venv
- python -m venv environment-name
- Activate environment with bash: source environment-name/Scripts/activate, in windows: .\environment-name	\Scripts\activate
- Deactivate the environment in bash/cmd: deactivate
- When inside of venv, install libraries with pip install X
- To create requirements list do: pip freeze > requirements.txt (needs to be done everytime you install a new library.
- To install requirements list do: pip install -r requirements.txt