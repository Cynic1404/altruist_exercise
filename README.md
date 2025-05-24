# Altruist UI Automation Exercise


## Note

This project is a **base structure for a broader UI test framework**.  
It has been **trimmed down to include only the parts necessary to run the current test task**.

The following components are part of a larger reusable architecture:
- `base/seleniumwebdriver.py` handles driver lifecycle and config injection
- `pages/google_finance.py` follows the Page Object Model pattern
- `conftest.py` supports customizable runtime options via CLI

This structure makes it easy to scale the framework with more test pages and suites as needed.



This is a Selenium + Pytest based automated test suite for verifying stock symbols on Google Finance.

## Installation

1. (Recommended) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configurable Options

This test framework supports runtime configuration via command-line options:

| Option     | Description                         | Default   |
|------------|-------------------------------------|-----------|
| `--browser`| Choose browser: `chrome`, `firefox` | `chrome`  |
| `--wait`   | Element wait timeout in seconds     | `5`       |

### Example Usage

```bash
pytest --browser=firefox --wait=10 --html=report.html
```

## Project Structure

```
.
├── base/
│   └── seleniumwebdriver.py   # App-level browser & helper logic
├── pages/
│   └── google_finance.py      # Page Object Model for Google Finance
├── test/
│   └── test_google.py         # Main test suite
├── conftest.py                # Fixtures and config options
├── requirements.txt
└── README.md
```


