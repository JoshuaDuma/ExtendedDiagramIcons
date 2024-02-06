import os
from setuptools import setup, find_packages

def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, "__init__.py")) as f:
        locals = {}
        exec(f.read(), locals)
        return locals["__version__"]

def generate_package_data(package_name, resource_dir):
    """
    Generate the package_data dictionary for setuptools setup function.
    It scans the resource_dir for all subdirectories and files to include.

    :param package_name: Name of the Python package
    :param resource_dir: Directory containing resources relative to the package
    :return: A dictionary suitable for the package_data argument in setup()

    # Example usage:
    # This would be used in your setup.py file.
    # package_data = generate_package_data('my_package', 'my_package/resources')

    # Note: This code is for demonstration and should be adjusted according to your actual package structure.
    # The function must be run in an environment where it can access the filesystem of the package.
    """
    package_data = {package_name: []}
    for root, dirs, files in os.walk(resource_dir):
        for file in files:
            if file.endswith('.png'):  # Only select .png files
                # Construct the path relative to the package
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, package_name)

                # Add the relative path to the package_data
                package_data[package_name].append(relative_path)

    return package_data

package_name = 'ExtendedDiagramIcons'  # Replace with your actual package name
basedir = os.path.dirname(__file__)
resource_directory = os.path.join(basedir, "resources")  # Adjust the path to your resources directory

package_data = generate_package_data(package_name, resource_directory)
print("---------------------")
print(package_data)
setup(
    name="ExtendedDiagramIcons",
    version=get_version(),
    author="Joshua Duma",
    author_email="joshua.duma@trader.ca",
    description="This is intended to be used in a project that uses the diagrams (diagrams as code) python package as an extention of the icons.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    package_data=package_data,
    repository="https://github.com/JoshuaDuma/ExtendedDiagramIcons",
    packages=find_packages(),
    install_requires=[
        "diagrams>=0.23.4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)