# python-hello-world2

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/)
- pip

### Environment Setup

1. Create virtual environment:
    - Mac: `python -m venv [directory name (Ex. ".env")]`
    - Windows: `py -3 -m venv [directory name]`
2. Activate the virtual environment:
    - Mac: `source [directory name]/bin/activate`
    - Windows: `[directory name]\Scripts\activate.bat`
3. Install packages: `pip3 install requirements.txt`
4. Set Python notebook kernel to `.env`

### Build Model

1. Run All from `data_processing.ipynb`
2. A new file, `model.pkl`, should appear in your project

### Run Web App

1. Enter app folder from terminal: `cd app`
2. Run the Flask app: `flask run` or `python3 -m flask run`
3. A single value in the array should appear. This is the prediction for the hardcoded inputs from `app.py`.
