from setuptools import setup, find_packages

setup(
    name="marimo-prompt-library",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.32.0",
        "python-dotenv>=1.0.0",
        "pytest>=8.3.0"
    ],
    python_requires=">=3.8",
)