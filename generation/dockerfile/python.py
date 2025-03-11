PYTHON_TEMPLATE_DIR = "templates/python"
PYTHON_TEMPLATE_DOCKERFILE = "dockerfile_py_39.j2"
PYTHON_DOCKER_PREFIX = "Dockerfile"
PYTHON_BACKENDS = {
    "fastapi": {"framework": "fastapi", "dependencies": "fastapi uvicorn"},
    "flask": {"framework": "flask", "dependencies": "flask"},
    "django": {"framework": "django", "dependencies": "django"},
    "starlette": {"framework": "starlette", "dependencies": "starlette uvicorn"},
    "sanic": {"framework": "sanic", "dependencies": "sanic"},
    "tornado": {"framework": "tornado", "dependencies": "tornado"},
    "bottle": {"framework": "bottle", "dependencies": "bottle"},
}
PYTHON_OUTPUT_DIR = "dockerfiles/python"


def get_configuration():
    return {
        "template_dir": PYTHON_TEMPLATE_DIR,
        "output_dir": PYTHON_OUTPUT_DIR,
        "backends": PYTHON_BACKENDS,
        "template_dockerfile": PYTHON_TEMPLATE_DOCKERFILE,
        "docker_prefix": PYTHON_DOCKER_PREFIX,
    }
