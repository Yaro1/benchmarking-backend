import re

GOLANG_SUFFIX = "service.go"
GOLANG_FUNCTIONS_FILE = "functions/golang/logic.go"
GOLANG_TEMPLATES_DIR = "templates/golang/frameworks"
GOLANG_OUTPUT_DIR = "backends/golang"
GOLANG_BACKEND_TEMPLATES = {
    "beego": "Beego.go.j2",
    "chi": "Chi.go.j2",
    "echo": "Echo.go.j2",
    "fiber": "Fiber.go.j2",
    "gin": "Gin.go.j2",
    "gokit": "GoKit.go.j2",
    "kratos": "Kratos.go.j2",
}


def extract_functions(file_path):
    """Extract function names dynamically from Go file."""
    with open(file_path, "r") as f:
        content = f.read()
    return re.findall(r"func\s+(\w+)\s*\(", content)


GOLANG_FUNCTIONS = extract_functions(GOLANG_FUNCTIONS_FILE)


def get_configuration():
    return {
        "output_dir": GOLANG_OUTPUT_DIR,
        "backend_templates": GOLANG_BACKEND_TEMPLATES,
        "functions": GOLANG_FUNCTIONS,
        "templates_dir": GOLANG_TEMPLATES_DIR,
        "suffix": GOLANG_SUFFIX,
    }
