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

- Note: This step is included to build the model locally, as the size of `model.pkl` exceeds normal fetch and push limits. If you have [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files) installed, you can fetch the `model.pkl` file in the repository and would not need to run the model build.

### Run Web App

1. Enter app folder from terminal: `cd app`
2. Run the Flask app: `flask run` or `python3 -m flask run`
3. The web app is now ready to use. Once user inputs are submitted, a housing price prediction is displayed in dollars.

## Languages & Tools

- Frontend: HTML/CSS
- Backend: [Flask](https://flask.palletsprojects.com/en/stable/)
- Data Exploration: [Python](https://www.python.org/), pandas, numpy, matplotlib, seaborn
- Model Generation: [Python](https://www.python.org/), scikit-learn
- Large File Storage: [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files)

## Source

Prediction model is trained on data from the 1990 census. More information on the dataset can be found here: [https://www.kaggle.com/datasets/camnugent/california-housing-prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
