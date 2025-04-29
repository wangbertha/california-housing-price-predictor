# California Housing Price Predictor

## Description

This is a web application that predicts the cost of a home in California, based on data from the [1990 census](https://www.kaggle.com/datasets/camnugent/california-housing-prices)

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
3. Install packages: `pip3 install -r requirements.txt`
4. Set Python notebook kernel to `.env`

### Build Model

1. Run All from `data_processing.ipynb`
2. A new file, `model.pkl`, should appear in your project

### Run Web App

1. Enter app folder from terminal: `cd app`
2. Run the Flask app: `flask run` or `python3 -m flask run`
3. A single value in the array should appear. This is the prediction from the user inputs, in dollars.

## Languages & Tools

- Frontend: HTML/CSS
- Backend: Flask
- Data Exploration: Python

## Source

Prediction model is trained on data from the 1990 census. More information on the dataset can be found here: [https://www.kaggle.com/datasets/camnugent/california-housing-prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
