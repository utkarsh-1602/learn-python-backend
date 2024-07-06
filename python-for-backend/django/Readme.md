# Django 

- Django is a full-featured Python web framework for developing dynamic websites and applications. Using Django, you can quickly create Python web applications and rely on the framework to do a good deal of the heavy lifting.
- Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).
- Django follows the **MVT design pattern (Model View Template)**.
1. Model - The data you want to present, usually data from a database. The models are usually located in a file called `models.py`.

2. View - A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.The views are usually located in a file called `views.py`.

3. Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data. The templates of an application is located in a folder named `templates`.


- Django also provides a way to navigate around the different pages in a website. When a user requests a URL, Django decides which **view** it will send it to. This is done in a file called `urls.py`.
- Django was invented by Lawrence Journal-World in 2003, to meet the short deadlines in the newspaper and at the same time meeting the demands of experienced web developers. Initial release to the public was in July 2005.

 

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