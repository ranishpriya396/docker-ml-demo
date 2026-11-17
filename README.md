# Docker ML Demo - Laptop Price Prediction

A Machine Learning web application built using Flask, Scikit-Learn, and Docker to predict laptop prices based on hardware specifications.

## Features

- Machine Learning Price Prediction
- Flask Web Interface
- Responsive UI with CSS
- Scikit-Learn Model
- Docker Support
- GitHub Ready Project Structure

## Tech Stack

- Python 3.12
- Flask
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Docker
- Git & GitHub

## Project Structure

```text
docker-ml-demo/
│
├── data/
│   └── laptop_data.csv
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── __init__.py
│   ├── train_model.py
│   └── predict.py
│
├── flask_app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── style.css
│
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Dataset Features

| Feature | Description |
|----------|-------------|
| Brand | Laptop Brand |
| CPU | Processor Type |
| RAM_GB | RAM Size |
| Storage_GB | Storage Capacity |
| Screen_Inch | Screen Size |
| Performance_Score | Performance Rating |
| Price_USD | Target Variable |

## Installation

### Clone Repository

```bash
git clone https://github.com/ranishpriya396/docker-ml-demo.git
```

```bash
cd docker-ml-demo
```

### Create Virtual Environment

```bash
python -m venv venvdocker
```

Activate environment:

#### Windows

```bash
venvdocker\Scripts\activate
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Train Model

```bash
python src/train_model.py
```

Output:

```text
Model Saved Successfully
```

Model will be saved in:

```text
models/model.pkl
```

## Run Flask Application

```bash
python flask_app/app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Docker Setup

### Build Docker Image

```bash
docker build -t docker-ml-demo .
```

### Run Container

```bash
docker run -p 5000:5000 docker-ml-demo
```

Open:

```text
http://localhost:5000
```

## Sample Input

```text
Brand: Dell
CPU: i7
RAM: 16
Storage: 512
Screen Size: 15.6
Performance Score: 85
```

## Output

```text
Predicted Laptop Price: $1450.75
```

## Future Improvements

- Model Evaluation Dashboard
- Docker Hub Deployment
- CI/CD using GitHub Actions
- Cloud Deployment
- Improved UI Design
- Feature Engineering

## Author

Ranish Priya

GitHub:
https://github.com/ranishpriya396
