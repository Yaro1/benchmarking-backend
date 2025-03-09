import os
import re
from jinja2 import Environment, FileSystemLoader

# Paths
FUNCTIONS_FILE = "functions/golang/logic.go"
TEMPLATES_DIR = "golang/templates/frameworks"
OUTPUT_DIR = "backends/golang"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Jinja2 Environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

# Framework to Template Mapping
TEMPLATES = {
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
    with open(file_path, 'r') as f:
        content = f.read()
    # Match function signatures like: func Compute(numbers []int) int
    return re.findall(r'func\s+(\w+)\s*\(', content)

def generate_services():
    functions = extract_functions(FUNCTIONS_FILE)
    print(f"✅ Extracted Functions: {functions}")

    for framework, template_file in TEMPLATES.items():
        template = env.get_template(template_file)
        output = template.render(functions=functions)

        output_file = os.path.join(OUTPUT_DIR, f"{framework}_service.go")
        with open(output_file, "w") as f:
            f.write(output)
        
        print(f"🚀 Generated service for {framework}: {output_file}")

if __name__ == "__main__":
    generate_services()
