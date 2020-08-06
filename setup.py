import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="get_news",
      version="0.0.2",
      description="This is code with Rudra package",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="iNeuron",
      author_email="rudragthite@gmail.com",
      packages=setuptools.find_packages(),
      url="https://github.com/rudragthite/get_news",
      classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      install_requires=[
          "blessings ~= 1.7",
      ],

      extras_requires = {
        "dev":[
            "pytest>=3.7",
        ],
      },)