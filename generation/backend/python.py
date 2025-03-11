import importlib
import inspect

PYTHON_SUFFIX = "app.py"
PYTHON_FUNCTIONS_FILE = "functions/python/logic.py"
PYTHON_TEMPLATES_DIR = "templates/python/frameworks"
PYTHON_OUTPUT_DIR = "backends/python"
PYTHON_BACKEND_TEMPLATES = {
    "fastapi": "FastAPI.py.j2",
    "flask": "Flask.py.j2",
    "django": "Django.py.j2",
    "starlette": "Starlette.py.j2",
    "sanic": "Sanic.py.j2",
    "tornado": "Tornado.py.j2",
    "bottle": "Bottle.py.j2",
}


def load_functions():
    """Loads functions dynamically from a Python file."""
    module_name = "logic"
    spec = importlib.util.spec_from_file_location(module_name, PYTHON_FUNCTIONS_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    functions = {
        name: func for name, func in inspect.getmembers(module, inspect.isfunction)
    }
    return functions


PYTHON_FUNCTIONS = list(load_functions().keys())


def get_configuration():
    return {
        "output_dir": PYTHON_OUTPUT_DIR,
        "backend_templates": PYTHON_BACKEND_TEMPLATES,
        "functions": PYTHON_FUNCTIONS,
        "templates_dir": PYTHON_TEMPLATES_DIR,
        "suffix": PYTHON_SUFFIX,
    }
