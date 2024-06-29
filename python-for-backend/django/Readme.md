# Django 

- Django is a full-featured Python web framework for developing dynamic websites and applications. Using Django, you can quickly create Python web applications and rely on the framework to do a good deal of the heavy lifting.

## What is a virtual Environment ? 
- A virtual environment is an isolated environment that allows you to manage dependencies for a Python project.
- It ensures that the dependencies required by different projects are isolated from each other, avoiding conflicts between packages and versions.

        python3 -m venv my_env

- running the above command creates a new directory named `my_env` then it installs the copy of python intrepreter within the `my_env` directory. It also includes a copy of the standard library, ensuring that the virtual environment has everything needed to run Python scripts. It sets up the `pip` package manager in the virtual environment, allowing you to install additional packages.

        source my_env/bin/activate 

- The command source my_env/bin/activate is used to activate a virtual environment in Unix-based systems (like Linux and macOS). 

- It’s a good idea now to pin your dependencies. This records the versions of all the Python libraries currently installed in your virtual environment.

        (venv) $ python -m pip freeze > requirements.txt

Note : freeze Generates a list of installed packages and their versions

# Creating a sample Project 

Refer: https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-22-04#creating-a-sample-project

[Projected Created on Location: project1](./project1/)