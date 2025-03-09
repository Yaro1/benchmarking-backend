import os
from jinja2 import Environment, FileSystemLoader

# Directory paths
TEMPLATES_DIR = "golang/templates"
OUTPUT_DIR = "dockerfiles/golang"
SERVICES_DIR = "backends/golang"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def generate_dockerfiles():
    # List all generated services to determine frameworks
    service_files = [f for f in os.listdir(SERVICES_DIR) if f.endswith("_service.go")]

    for service_file in service_files:
        framework = service_file.split('_')[0]
        template = env.get_template("dockerfile_go_1_21.j2")

        # Render the template with framework name
        dockerfile_content = template.render(framework=framework)

        # Define output path for the Dockerfile
        output_path = os.path.join(OUTPUT_DIR, f"Dockerfile.{framework}")
        with open(output_path, "w") as f:
            f.write(dockerfile_content)

        print(f"✅ Dockerfile generated for {framework}: {output_path}")

if __name__ == "__main__":
    generate_dockerfiles()
