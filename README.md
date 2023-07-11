# ML Pipeline Template

This repository serves as a template for creating machine learning pipelines. It provides a structured framework and guidelines to help you organize your machine learning projects effectively.

[![Build Status](https://img.shields.io/travis/taiocean1213/ml_pipeline_template/master.svg)](https://travis-ci.org/github/taiocean1213/ml_pipeline_template)
[![Code Coverage](https://img.shields.io/codecov/c/github/taiocean1213/ml_pipeline_template/master.svg)](https://codecov.io/gh/taiocean1213/ml_pipeline_template)
[![License](https://img.shields.io/github/license/taiocean1213/ml_pipeline_template.svg)](https://github.com/taiocean1213/ml_pipeline_template/blob/master/LICENSE)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The ML Pipeline Template is designed to streamline the development and deployment of machine learning models. It provides a set of best practices and a modular structure that allows for easy experimentation, model training, and evaluation.

## Features

- Structured framework for organizing machine learning projects.
- Pre-defined stages and modules for data preparation, model training, evaluation, and deployment.
- Easy customization to fit specific machine learning projects.

## Installation

To get started with the ML Pipeline Template, follow these steps to deploy the server:

1. Clone the repository:
```bash
$ git clone https://github.com/taiocean1213/ml_pipeline_template.git
```

1. Go into the repository:
```bash
$ cd ml_pipeline_template
```

1. Create and activate the virtual environment:
```bash
$ python3 -m venv venv;source venv/bin/activate
```

1. Install the required dependencies:
```bash
(venv)$ pip install -r requirements.txt
```

1. Run the DVC pull command:
```bash
(venv)$ dvc pull 
```

Now the `src/deployment/main.py` is ready to be ran using the python command:
```bash
(venv)$ python3 src/deployment/main.py
```

## Getting Started

1. Navigate to the project root directory in the terminal:
```bash
$ cd ml_pipeline_template
```

2. Install the required dependencies:
```bash
$ pip install -r requirements.txt
```

## Usage

The ML Pipeline Template provides a set of pre-defined stages and modules that can be customized to fit your specific machine learning project. Here are the main components of the template:

- `data_preparation`: Contains scripts and utilities for data preprocessing and feature engineering.
- `model_training`: Includes scripts for model training and evaluation.
- `model_evaluation`: Provides tools for model evaluation and performance metrics.
- `deployment`: Contains scripts and configurations for deploying the trained model.

For more detailed instructions and code examples, please refer to the [documentation](#documentation).

## Documentation

The documentation provides detailed instructions, explanations, and code examples for each component and stage of the ML Pipeline Template. Please refer to the [documentation](documentation.md) for more information.

## Contributing

Contributions to the ML Pipeline Template are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Please make sure to follow the [contribution guidelines](CONTRIBUTING.md). Note: this link has not been created yet.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Pushing to Remotes

To push your changes and assets to remotes, follow these steps:

1. Add a remote named 'myremote' using the command:
```bash
$ dvc remote add -d myremote gdrive://1dtuVBTTqiuw4weaAPAqBDBEBzAq6Jfe-?usp=sharing
```
This adds a remote named 'myremote' with the Google Drive remote storage URL.

2. Add the data file 'assets/data/digits.csv' and the model file 'assets/models/model.joblib' to DVC using the command:
```bash
$ dvc add assets/data/digits.csv assets/models/model.joblib
```
This command creates DVC metafiles for tracking the data and model files.

3. Commit the changes to DVC using:
```bash
$ dvc commit
```
This versionizes the data and model files in DVC.

4. Push the data and models to the remote using:
```bash
$ dvc push
```
This command pushes the data and models to the remote storage specified by 'myremote'.

5. Add and commit the changes to Git using the commands:
```bash
$ git add .
$ git commit -a -m "Updated Model"
```
This adds and commits the changes, including the DVC metafiles, to your Git repository.

6. Push the changes to the Git remote using:
```bash
$ git push
```
This pushes the changes to the Git remote, including the DVC metafiles and the updated data and models.


## Pulling to Remotes

To pull changes and assets from remotes, follow these steps:

1. Clone the Git repository using the command:
```bash
$ git clone <git-repo-url>
```
Replace <git-repo-url> with the actual URL of the Git repository.

2. Add a remote named 'myremote' using the command:
```bash
$ dvc remote add -d myremote gdrive://1dtuVBTTqiuw4weaAPAqBDBEBzAq6Jfe-?usp=sharing
```
This adds a remote named 'myremote' with the Google Drive remote storage URL.

3. Pull the data and models from the remote using the command:
```bash
$ dvc pull myremote
```
This command retrieves the latest data and models from the remote storage.

4. Checkout a specific version using the command:
```bash
$ git checkout <versionHash>
```
Replace <versionHash> with the hash of the specific version you want to checkout.

5. Checkout the data and models using the command:
```bash
$ dvc checkout
```

# References

1. DVC Documentation: [Managing Data Files](https://dvc.org/doc/start/data-and-model-versioning)
2. DVC Documentation: [Managing Models](https://dvc.org/doc/start/data-and-model-versioning#managing-model-versions)
3. DVC Documentation: [Managing Remotes](https://dvc.org/doc/command-reference/remote/add)
4. DVC Documentation: [Pulling and Pushing](https://dvc.org/doc/command-reference/pull)
5. Git Documentation: [Git Clone](https://git-scm.com/docs/git-clone)
6. Git Documentation: [Git Checkout](https://git-scm.com/docs/git-checkout)
