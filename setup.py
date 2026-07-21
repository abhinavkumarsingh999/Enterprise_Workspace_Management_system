from setuptools import setup, find_packages

setup(
    name="enterprise-workspace-scaffolding",
    version="0.1.0",
    packages=find_packages(include=["src","src.*"]),
    description="AI/ML Enterprise Workspace Scaffolding with Custom Logger",
    python_requires=">=3.10",
    install_requires=[],
    extras_require={
        "dev": ["pytest>=8.0"],
    },
)