from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()


setup(
    name="",
    version="1.0",
    author=["Sivakumar Mahalingam", "Sabarinath Velayudham"],
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sivakumar-mahalingam/country-database/",
    project_urls={
        'Source': 'https://github.com/sivakumar-mahalingam/country-database',
        'Tracker': 'https://github.com/sivakumar-mahalingam/country-database/issues',
    },
    license="",
    python_requires=">=3.8",
    install_requires=[
        ""
    ],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
	    "Environment :: MacOS X",
	    "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
    	"Intended Audience :: Education",
    	"Natural Language :: English",
    	"Operating System :: OS Independent",
    ],
    keywords=[
        ""
    ]
)
