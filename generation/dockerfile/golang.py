GOLANG_TEMPLATES_DIR = "templates/golang"
GOLANG_TEMPLATE_DOCKERFILE = "dockerfile_go_1_21.j2"
GOLANG_DOCKER_PREFIX = "Dockerfile"
GOLANG_BACKENDS = {
    "beego": {"framework": "beego"},
    "chi": {"framework": "chi"},
    "echo": {"framework": "echo"},
    "fiber": {"framework": "fiber"},
    "gin": {"framework": "gin"},
    "gokit": {"framework": "gokit"},
    "kratos": {"framework": "kratos"},
}
GOLANG_OUTPUT_DIR = "dockerfiles/golang"


def get_configuration():
    return {
        "template_dir": GOLANG_TEMPLATES_DIR,
        "output_dir": GOLANG_OUTPUT_DIR,
        "backends": GOLANG_BACKENDS,
        "template_dockerfile": GOLANG_TEMPLATE_DOCKERFILE,
        "docker_prefix": GOLANG_DOCKER_PREFIX,
    }
