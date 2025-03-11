import os
from jinja2 import Environment, FileSystemLoader
import yaml

from golang import get_configuration as get_configuration_golang
from python import get_configuration as get_configuration_python


def generate_dockerfiles(
    template_dir, 
    output_dir, 
    backends, 
    template_dockerfile,
    docker_prefix,
):
    env = Environment(loader=FileSystemLoader(template_dir))
    os.makedirs(output_dir, exist_ok=True)
    template = env.get_template(template_dockerfile)
    for backend, info in backends.items():
        output = template.render(**info)
        output_file = os.path.join(output_dir, f"{docker_prefix}.{backend}")

        with open(output_file, "w") as f:
            f.write(output)

        print(f"✅ Generated Dockerfile: {output_file}")


if __name__ == "__main__":
    print("---------------------------------------------")
    print("Generation golang dockerfiles")
    generate_dockerfiles(**get_configuration_golang())
    print("---------------------------------------------")
    print("Generation python dockerfiles")
    generate_dockerfiles(**get_configuration_python())
    print("---------------------------------------------")
    print("Completed successfully!")
    print("---------------------------------------------")
