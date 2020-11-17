# When you import a directory but you havent given a specific file name then it will import __init__.py by default


from controllers.auth_controller import auth                # Importing the auth blueprint

registerable_controllers = [
    auth,
]
