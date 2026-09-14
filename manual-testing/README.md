# Automation Testing - SauceDemo

This folder contains automated test scripts for the SauceDemo web application using Selenium WebDriver and Pytest.

The automation testing project supports functional testing and regression testing by executing repeatable test scenarios automatically.

## Objective

The objective of this automation project is to verify important SauceDemo functionality through automated browser testing.

Automation testing helps reduce repetitive manual testing and provides consistent and repeatable test execution.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| Pytest HTML | HTML test report generation |
| WebDriver Manager | Browser driver management |
| Git | Version control |
| GitHub | Source code repository |

## Automated Testing Scope

The automated test scenarios include selected SauceDemo functionality, such as:

- Successful login
- Product selection
- Add product to cart
- Shopping cart validation
- Checkout process
- Checkout form validation
- Order completion
- Logout

## Project Structure

```text
automation-testing/
│
├── tests/
│   └── Automated test scripts
│
├── reports/
│   └── Generated test reports
│
├── screenshots/
│   └── Screenshots generated during test execution
│
├── conftest.py
└── README.md
```

## Prerequisites

Before running the automation tests, make sure the following software is installed:

- Python 3.x
- Google Chrome
- Git
- Visual Studio Code or another code editor

## Installation

Open the terminal inside the `automation-testing` folder.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install selenium pytest pytest-html webdriver-manager
```

## Running the Tests

To run all automated tests:

```bash
pytest
```

To run the tests with detailed output:

```bash
pytest -v
```

To run a specific test file:

```bash
pytest tests/test_login.py -v
```

Replace `test_login.py` with the actual test file name available in the `tests` folder.

## Generate HTML Report

To generate an HTML test report:

```bash
pytest --html=reports/report.html --self-contained-html
```

The generated report will be stored in the `reports` folder.

Example:

```text
reports/
└── report.html
```

## Screenshot Evidence

Screenshots generated during test execution are stored in the screenshots folder.

Screenshots may be used as evidence for:

- Successful test execution
- Failed test execution
- Validation errors
- Unexpected application behavior
- Debugging test failures

## Automation Testing Flow

```text
Open Browser
     ↓
Open SauceDemo Website
     ↓
Execute Test Scenario
     ↓
Validate Expected Result
     ↓
Capture Screenshot if Necessary
     ↓
Close Browser
     ↓
Generate Test Report
```

## Example Test Scenario

### Successful Login

| Item | Description |
|---|---|
| Test Scenario | Verify successful login |
| Test Data | Valid username and password |
| Expected Result | User is redirected to the product page |
| Automation Tool | Selenium WebDriver |
| Test Framework | Pytest |

## Test Results

The automation test results can be reviewed through:

- Terminal output
- HTML test report
- Screenshots generated during execution

Example command:

```bash
pytest -v
```

## Benefits of Automation Testing

Automation testing provides several benefits:

- Faster test execution
- Repeatable testing process
- Reduced repetitive manual work
- Improved regression testing
- Consistent test results
- Easier defect verification
- Better testing documentation

## Relationship with Manual Testing

The automation testing project complements the manual testing process.

```text
Manual Test Case
       ↓
Manual Test Execution
       ↓
Defect Identification
       ↓
Bug Reporting in Jira
       ↓
Retesting
       ↓
Automation Script
       ↓
Regression Testing
```

## Notes

This project uses the SauceDemo demo website for learning and portfolio purposes.

The automation scripts may require updates if the website structure, browser version, or testing environment changes.
