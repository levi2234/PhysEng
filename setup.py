from setuptools import setup, find_packages

# Read the contents of the requirements.txt file
with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="PhysEng",  # Replace with your project's name
    version="0.0.1",  # Version of your project
    author="Levi van Es",  # Your name
    author_email="levi2234@hotmail.com",  # Your email address
    description="A physics engine project",  # Short description
    long_description=open("Readme.md").read(),  # Long description from README
    long_description_content_type="text/markdown",  # Content type of long description
    url="https://github.com/levi2234/Progresspal",  # URL to your project's repository
    packages=find_packages(
        where="src"
    ),  # Automatically find packages in the src directory
    package_dir={"": "src"},  # Source code is under src
    package_data={
        "PhysEng": [
            "*.txt",
            "*.json",
            "*.html",
            "*.css",
            "*.js",
            "*.png",
            "*.ico",
            "*.jpg",
            "*.jpeg",
            "*.svg",
            "*.gif",
            "*.py",
            "",
        ],
    },  # Include all files in the package
    python_requires=">=3.9",  # Minimum Python version required
    install_requires=required,
    extras_require={  # Optional dependencies
        "dev": [
            "pytest-cov",  # Coverage for pytest
            # Add other development tools here
        ],
    },
    classifiers=[  # Classifiers for the project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "ProgressPal=ProgressPal.cli:CLI",
        ],
    },
)
