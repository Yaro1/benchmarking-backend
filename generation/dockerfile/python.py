import os
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = "templates/python"
OUTPUT_DIR = "dockerfiles/python"

# Define dependencies for each backend
BACKENDS = {
    "fastapi": {"filename": "fastapi_app.py", "dependencies": ["fastapi", "uvicorn"]},
    "flask": {"filename": "flask_app.py", "dependencies": ["flask"]},
    "django": {"filename": "django_app.py", "dependencies": ["django"]},
    "starlette": {"filename": "starlette_app.py", "dependencies": ["starlette", "uvicorn"]},
    "sanic": {"filename": "sanic_app.py", "dependencies": ["sanic"]},
    "tornado": {"filename": "tornado_app.py", "dependencies": ["tornado"]},
    "bottle": {"filename": "bottle_app.py", "dependencies": ["bottle"]},
}

# Load Jinja2 templates
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def generate_dockerfiles():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    template = env.get_template("dockerfile_py_39.j2")

    for backend, info in BACKENDS.items():
        output = template.render(
            backend_filename=info["filename"],
            dependencies=" ".join(info["dependencies"])  # Install only necessary packages
        )
        output_file = os.path.join(OUTPUT_DIR, f"Dockerfile.{backend}")

        with open(output_file, "w") as f:
            f.write(output)

        print(f"✅ Generated Dockerfile: {output_file}")

if __name__ == "__main__":
    generate_dockerfiles()
