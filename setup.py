import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-inventory",
    version="0.0.4",
    author="Brian Alexander",
    author_email="brian@dadgumsalsa.com",
    description="A simple Django app for managing an inventory log of items.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/balexander85/django-inventory",
    packages=setuptools.find_packages(),
    install_requires=["pillow"],
    include_package_data=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Framework :: Django :: 2.*",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
