## Finance API

This is a REST API project created using python, Django and Django Rest Framework.

## Running the code

To run the project, run `python manage.py runserver`

### Env

- To access the local env, go to http://localhost:8000
- To manage items, to go the admin panel at http://localhost:8000/admin

## More about it

### Migrations

- Create admin user: `python manage.py createsuperuser`
- Create migrations: `python manage.py makemigrations finance_api`
- Migrate db: `python manage.py migrate`

### PipEnv

This projects uses PipEnv to organize the python dependencies.

To install PipEnv, you need to have python and pip already installed (_the recommended version of python is python 3.9_).

```sh
pip install pipenv
```

After installing, make sure you can execute `pipenv` from your terminal.

If not, you will need to add it to your path variable, such as:

```sh
# find out where your python dependencies are installed
export PYTHON_PATH=`python3 -m site --user-base`

#after having the path, update your PATH variable with your python path
export PATH=$PATH:$PYTHON_PATH/bin
```

#### Running in developer mode

```sh
# install dependencies
pipenv install --dev

# then you can run anything in the project, everything should be already installed
pipenv run python3 sync.py
```

### Debugging with the dev server in VS Code

1. Set the Python interpreter to use the local pipenv environment.
   - First, run `pipenv --venv` from the terminal to get the path to your interpreter
   - In VS Code, `cmd+shift+p` and select `Python: select interpreter`
   - Select the `+ Enter interpreter path...` option
   - Enter the path that got from running `pipenv --venv` in the first step
2. Add a launch file at `.vscode/launch.json` with the following contents:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug Flask Server",
         "type": "python",
         "request": "launch",
         "module": "flask",
         "env": {},
         "args": ["run", "--no-debugger"],
         "jinja": true,
         "justMyCode": true
       }
     ]
   }
   ```
3. Go to the debug tab in VS Code, select the `Debug Flask Server` option and click the start (▶️) button to start the server. You should be able to set breakpoints in code and hit them while debugging.
