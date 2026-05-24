from pathlib import Path

from setuptools import find_packages, setup


PROJECT_ROOT = Path(__file__).parent


def read_requirements() -> list[str]:
    requirements_file = PROJECT_ROOT / "requirements.txt"
    if not requirements_file.exists():
        return []

    requirements: list[str] = []
    for line in requirements_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        requirements.append(line)
    return requirements


setup(
    name="medical-rag-chatbot",
    version="0.1.0",
    description="An AI-powered medical chatbot built with a Retrieval-Augmented Generation architecture.",
    packages=find_packages(include=["src", "src.*"]),
    py_modules=["app"],
    install_requires=read_requirements(),
    python_requires=">=3.10",
)
