1. Status
Development Phase: Production-Ready & Containerized.
Integration Level: Complete end-to-end pipeline. It spans automated API Extraction (DHS & Open-Meteo API), Transformation, Loading into an Airflow-compatible SQLite schema, and live container deployment via a Dockerized Streamlit dashboard with automated zip compiling and downloading in Google Colab.
2. Hypothesis
Core Assumption ($H_1$$H_1$): Malaria prevalence rates ($RDT \%$$RDT \%$) across Nigerian states are not purely geographical; they are driven by temporal trends over time (captured by survey_year) and structured ecological/climate variations (yearly mean temperature $T$$T$ and total annual precipitation $P$$P$).
Underlying Mechanism: Higher precipitation yields increased standing water (mosquito breeding vector replication), while variations in temperature accelerate or decelerate parasite development cycles, interacting uniquely within sub-national boundaries.
3. Config (Experimental Setup)
Dataset: 108 sub-national observation rows dynamically compiled across 36 Nigerian states + FCT over historical survey years (2015, 2018, 2021).
Feature Space ($X$$X$): ['survey_year', 'annual_mean_temp_c', 'annual_total_precipitation_mm', 'is_northern'] + 36 One-Hot Encoded State dummy variables.
Target Variable ($y$$y$): Continuous malaria prevalence percentage (prevalence_pct).
Models Tested:
Random Forest Regressor: 150 Estimators, bootstrap validation, MSE split criterion, random state 42.
Multi-Layer Perceptron (MLP): TensorFlow/Keras feed-forward network ($Densa(64, Relu) \rightarrow Dropout(0.2) \rightarrow Dense(32, Relu) \rightarrow Dropout(0.2) \rightarrow Dense(1)$$Densa(64, Relu) \rightarrow Dropout(0.2) \rightarrow Dense(32, Relu) \rightarrow Dropout(0.2) \rightarrow Dense(1)$), optimized using Adam ($lr=0.01$$lr=0.01$) over 150 epochs.
4. Outcome
Random Forest Performance (Evironmental Model):
Mean Absolute Error (MAE): ~8.67% (The model predicts state-level prevalence with an average absolute error of under 9 percentage points).
Root Mean Squared Error (RMSE): ~10.59%.
R-squared ($R^2$$R^2$): 0.165 (The general split shows a baseline explanation; indicating high residual variance across states when generalized across test subsets).
Deep Learning (MLP) Performance:
Mean Absolute Error (MAE): ~7.93% (Slightly superior predictive accuracy than the Random Forest baseline).
R-squared ($R^2$$R^2$): 0.121.
5. Learning
Data Scarcity vs. Complexity: With only 108 sample rows, Deep Learning (MLP) remains highly sensitive to parameter initialization and is susceptible to overfitting, despite having slightly lower MAE than Random Forest on the test slice.
Temporal Signaling: Including the continuous temporal variable survey_year enables the models to learn broad progression trends, preventing predictions from remaining statically bound to historical averages and allowing users to experiment with forward-looking climate projections (up to 2030).
Regional Disparity: Explicit regional modeling (e.g., separating Northern States, which exhibit an average baseline prevalence rate of 43.83% compared to the National average of 38.03%) is vital, validating the decision to structure distinct localized parameters in the Streamlit production portal.
