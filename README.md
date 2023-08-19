# For minimalist Dash app: without script (a.k.a. '.exe') requirements

- If building a new project that depends on dash (and presumably using a venv), then pip install's `--user` option cannot be used. So just use:
    ```
    pip install pandas
    pip install dash
    ```

- If installing a module that depends on dash to a user's machine who does not have admin rights, then use: `pip install <module_name> --user`


# To run

- `& c:/Users/andyc/OneDrive/Desktop/repos/dash/.venv/Scripts/python.exe c:/Users/andyc/OneDrive/Desktop/repos/dash/src/test_dash.py`