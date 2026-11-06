# Nigeria Malaria Prevalence Predictor

A Streamlit application that estimates malaria prevalence for Nigerian states from the survey year, annual mean temperature, and total precipitation. It uses a pre-trained Random Forest model and displays the predicted prevalence as a percentage, together with a low, moderate, or high risk band.

This is a capstone project by a team of five data science mentees at EHA Clinics.

## Why use this project

- Explore a model-based prevalence estimate for any of Nigeria's 36 states or the FCT.
- Adjust the survey year, temperature, and precipitation interactively and see the prediction update.
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
2. Select a survey year from 2010 to 2030 (default: 2021). The selected year is passed to the model as `survey_year`; it identifies the survey year used for the estimate and is not a forecast horizon.
3. Set annual mean temperature (20–35 °C) and annual total precipitation (200–3,500 mm).
4. Read the predicted malaria prevalence (RDT %) and its displayed risk band:
   - Below 20%: low
   - 20% to below 45%: moderate
   - 45% or above: high

The values are model estimates, not measured prevalence. This deployment repository contains the app and pre-trained model artifacts; it does not include the model-training pipeline or source dataset.

## Project methodology

The project workflow covers data acquisition, climate enrichment, analysis, model development, and deployment. The ETL, analysis, and training steps below describe the wider capstone workflow; their notebooks and source data are not included in this deployment repository.

### 1. Data ETL pipeline

- **Extract:** Query the live Demographic and Health Surveys (DHS) API for Nigeria (`countryIds=NG`) to retrieve state-level malaria prevalence measured by rapid diagnostic tests (RDTs), using indicator `ML_PMAL_C_RDT`.
- **Transform:** Keep the survey year (`SurveyYear`), prevalence (`Value`), and confidence intervals. Normalize geographic names (for example, `.Kano` to `Kano`) and filter the records for Northern states.
- **Load:** Write the national and Northern-state data to `national_malaria_prevalence` and `northern_malaria_prevalence` tables in a local SQLite database, `malaria_north.db`, using pandas `to_sql`.

### 2. Climate feature enrichment

- **Geospatial cross-reference:** Use representative latitude and longitude coordinates for Nigeria's 36 states and the Federal Capital Territory (FCT).
- **Historical weather retrieval:** For each state and survey year, query the Open-Meteo Archive API for daily temperature and precipitation. Aggregate the daily observations into annual mean temperature (°C) and total precipitation (mm), which are used as model features.

### 3. Statistical analysis and EDA

Explore relationships between malaria prevalence and climate variables with regression plots and correlation heatmaps. The statistical analysis also examines skewness and kurtosis, tests normality with the Shapiro-Wilk test, and uses a Bayesian formulation to estimate the posterior probability of high malaria prevalence given low precipitation: `P(High Malaria | Low Rain)`.

### 4. Machine learning and deep learning

- **Random Forest regressor:** Train on survey year, climate measures, and one-hot encoded state features to predict continuous malaria prevalence. The deployed Streamlit app uses the pre-trained Random Forest model.
- **Multi-layer perceptron (MLP):** The training work also explores a TensorFlow/Keras feed-forward neural network, using standardized features, dropout regularization, and dense layers to model non-linear relationships between climate and malaria prevalence. The MLP is not the model served by this deployment app.

### 5. Streamlit application and Docker

- **Streamlit interface:** In `app.py`, users select a state, survey year (2010–2030), annual mean temperature, and annual total precipitation. The app passes these inputs to the pre-trained Random Forest and displays a prevalence estimate and risk band: low, moderate, or high. The selected year is a model input, not a forecast horizon.
- **Docker deployment:** `Dockerfile` and `docker-compose.yml` package and run the app in a Linux container, helping keep the deployment environment consistent across machines and cloud infrastructure.

## Help

For setup or application questions, open an issue in the repository where you obtained this code, if issue tracking is enabled, or contact the project team. The dependency list is in [`requirements.txt`](requirements.txt), and Docker configuration is in [`Dockerfile`](Dockerfile) and [`docker-compose.yml`](docker-compose.yml).

## Maintainers and contributors

The project is maintained by the EHA Clinics group 1 capstone project team. The following contributors and roles were provided:

- **Muhammad Kabir** — visualisation and deployment
- **Khalifa Ashiru Danliman** — statistics, machine learning, and slide development
- **Peace Yilmwen** — data acquisition and management
- **Faith** — data wrangling and exploratory data analysis (EDA)

The team has five mentees; the fifth member's name and contribution were not provided here.

### Contributing

Contributions from the project team are welcome. Before proposing a change, check existing issues or discuss the change with the maintainers. Keep changes focused, preserve the current app workflow, and test the app locally before submitting a pull request. Include an update to this README when setup or usage changes. No separate contribution guide is currently included.
