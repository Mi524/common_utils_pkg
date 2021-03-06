import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="common_utils_data", # Replace with your own username
    version="0.0.4",
    author="Tracy Tang",
    author_email="tracytang58@icloud.com",
    description="common functions used for data handling, including pandas operations and excel files operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mi524/common_utils_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
          'pandas>=1.2.0',
          'numpy',
          'openpyxl',
          'xlsxwriter',
          'xlwings',
          'html5lib',
          'lxml',
          'sqlalchemy>=1.3.22',
          'pymysql>=1.0.2',
          'mysql-client',
          'flashtext',
          'swifter>=1.0.7'
      ],
)