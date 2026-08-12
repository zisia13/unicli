from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).parent.resolve()
readme_path = ROOT / "README.md"
long_description = (
    readme_path.read_text(encoding = "utf-8")
    if readme_path.is_file() and readme_path.stat().st_size > 0
    else "todo"
)

setup(
    name = "uniterm",
    version = "0.2.10",
    description = "A collection lib of CLI utilities - selects, banners, colors, and full terminal screens.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "zisia13",
    #? author_email = "nothing@nothing.com",
    url = "https://github.com/zisia13/uniterm",
    packages = find_packages(
        exclude = (
            "temp",
            "temp.*",
            "lib",
            "lib.*"
        )
    ),
    python_requires = ">=3.9",
    install_requires = [],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    zip_safe = False,
)
