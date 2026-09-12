# SauceDemo QA Testing

Manual testing project on the SauceDemo e-commerce website.

## Project Overview

This project demonstrates the software testing process, including test case creation, functional testing, negative testing, test execution, and defect reporting using Jira.

## Application Under Test

- **Application:** SauceDemo
- **Website:** https://www.saucedemo.com/

## Testing Scope

- Login
- Product listing and sorting
- Product detail
- Shopping cart
- Checkout process
- Input validation
- Order completion
- Logout

## Tools Used

- SauceDemo
- Jira
- GitHub
- Python
- Jira REST API
- GitHub REST API

## Test Execution Summary

| Metric | Result |
|---|---:|
| Total Test Cases | 28 |
| Passed | 27 |
| Failed | 1 |
| Pass Rate | 96.43% |
| Defects Found | 1 |

## Defect Found

**Bug ID:** SCRUM-23  
**Related Test Case:** TC-018  
**Title:** Postal Code Field Accepts Non-Numeric Characters During Checkout

The postal code field accepts invalid input such as `abc123` and allows the user to continue to the checkout overview page without displaying a validation message.

### Expected Result

The system should reject invalid postal code input and display an appropriate validation message.

### Actual Result

The system accepts the invalid input and allows the checkout process to continue.

## Repository Structure

```text
saucedemo-qa-testing/
├── README.md
├── jira-issues/
└── bug-reports/
```

## Author
ANGGI RAHMADILLAH
