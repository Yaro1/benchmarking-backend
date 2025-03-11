import os

from golang import get_configuration as get_configuration_golang
from jinja2 import Environment, FileSystemLoader
from python import get_configuration as get_configuration_python


def generate_backends(
    output_dir,
    backend_templates,
    functions,
    templates_dir,
    suffix,
):
    env = Environment(loader=FileSystemLoader(templates_dir))
    os.makedirs(output_dir, exist_ok=True)
    for backend, template_file in backend_templates.items():
        template = env.get_template(template_file)
        output = template.render(functions=functions)

        output_file = os.path.join(output_dir, f"{backend}_{suffix}")

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w") as f:
            f.write(output)

        print(f"✅ Generated {backend} backend at {output_file}")


if __name__ == "__main__":
    print("---------------------------------------------")
    print("Generation golang backends")
    generate_backends(**get_configuration_golang())
    print("---------------------------------------------")
    print("Generation python backends")
    generate_backends(**get_configuration_python())
    print("---------------------------------------------")
    print("Completed successfully!")
    print("---------------------------------------------")
