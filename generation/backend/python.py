import os
import importlib.util
import inspect
from jinja2 import Environment, FileSystemLoader

USER_FUNCTIONS_FILE = "functions/python/logic.py"
TEMPLATE_DIR = "templates/python/frameworks"
OUTPUT_DIR = "backends/python"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
TEMPLATES = {
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
    spec = importlib.util.spec_from_file_location(module_name, USER_FUNCTIONS_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    functions = {name: func for name, func in inspect.getmembers(module, inspect.isfunction)}
    return functions


def generate_backends():
    functions = load_functions()
    function_names = list(functions.keys())

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for backend, template_file in TEMPLATES.items():
        template = env.get_template(template_file)
        output = template.render(functions=function_names)

        output_file = os.path.join(OUTPUT_DIR, f"{backend}_app.py")

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w") as f:
            f.write(output)

        print(f"✅ Generated {backend} backend at {output_file}")

if __name__ == "__main__":
    generate_backends()
