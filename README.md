# Nigeria Malaria Prevalence Predictor

A Streamlit application that estimates malaria prevalence for Nigerian states from annual mean temperature and total precipitation. It uses a pre-trained Random Forest model and displays the predicted prevalence as a percentage, together with a low, moderate, or high risk band.

This is a capstone project by a team of five data science mentees at EHA Clinics.

## Why use this project

- Explore a model-based prevalence estimate for any of Nigeria's 36 states or the FCT.
- Adjust temperature and precipitation interactively and see the prediction update.
- Run the application locally with Python or deploy it using Docker Compose.

The estimate is for exploration and educational purposes only. It is not a diagnosis, clinical decision, or substitute for official public-health data.

## Getting started

### Requirements

- Python 3.9 or later and pip, or
- Docker with the Docker Compose plugin.

The model files `malaria_climate_model.pkl` and `model_features.pkl` must be present in the project directory alongside `app.py`. Both are included in this repository.

### Run with Python

From the project directory, create and activate a virtual environment, then install the dependencies:

```shell
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```shell
source .venv/bin/activate
```

Install the requirements and start Streamlit:

```shell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed by Streamlit (typically <http://localhost:8501>).

### Run with Docker Compose

From the project directory, build the image and start the app:

```shell
docker compose up --build
```

Then open <http://localhost:8501>. Stop the service with `Ctrl+C`; to remove the stopped container, run:

```shell
docker compose down
```

## Using the application

1. Select a Nigerian state or the FCT from the sidebar.
2. Set annual mean temperature (20–35 °C) and annual total precipitation (200–3,500 mm).
3. Read the predicted malaria prevalence (RDT %) and its displayed risk band:
   - Below 20%: low
   - 20% to below 45%: moderate
   - 45% or above: high

The values are model estimates, not measured prevalence. This deployment repository contains the app and pre-trained model artifacts; it does not include the model-training pipeline or source dataset.

## Help

For setup or application questions, open an issue in the repository where you obtained this code, if issue tracking is enabled, or contact the project team. The dependency list is in [`requirements.txt`](requirements.txt), and Docker configuration is in [`Dockerfile`](Dockerfile) and [`docker-compose.yml`](docker-compose.yml).

## Maintainers and contributors

The project is maintained by the EHA Clinics capstone team. The following contributors and roles were provided:

- **Muhammad Kabir** — visualisation and deployment
- **Khalifa Ashiru Danliman** — statistics, machine learning, and slide development
- **Peace Yilmwen** — data acquisition and management
- **Faith** — data wrangling and exploratory data analysis (EDA)

The team has five mentees; the fifth member's name and contribution were not provided here.

### Contributing

Contributions from the project team are welcome. Before proposing a change, check existing issues or discuss the change with the maintainers. Keep changes focused, preserve the current app workflow, and test the app locally before submitting a pull request. Include an update to this README when setup or usage changes. No separate contribution guide is currently included.
