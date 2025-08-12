This repository contains the test automation suite for running the smoke tests on the fleet web portal
## Setting up the test suite
### Prerequisites
1. Python version 3.8+

### Create and enable virtual environment(if needed)
Inside the repository root run the following commands
> pip install virtualenv

> virtualenv venv

> venv \Scripts\activate 

### Install requirements
> pip install -r requirements.txt

> playwright install

### Run tests
> pytest


### Allure Report
#### Generate Allure Report(Need node.js installed):
[comment out "addopts = --alluredir allure-results --allure-no-capture" in pytest.ini]

>npx allure generate ./allure-results -o ./allure-report

#### Open Report:

>npx allure open ./allure-report
