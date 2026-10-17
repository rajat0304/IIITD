# 🌱 AgriSense — Satellite-Powered Agricultural Intelligence

**Transforming satellite imagery and environmental data into actionable agricultural insights using Machine Learning, Remote Sensing, and AI.**

AgriSense is an AI-powered agricultural intelligence platform designed to help farmers make data-driven decisions through satellite imagery, weather information, and machine learning models.

The platform aims to integrate data from NASA and ISRO-supported Earth observation sources with meteorological data and field-level information to monitor crop health, identify potential risks, and generate predictive insights.

Our goal is to move agriculture from reactive decision-making to **proactive, data-driven crop management**.

---

## 🚀 The Problem

Farmers face several challenges that affect crop productivity, resource utilization, and profitability:

- **Limited Crop Health Visibility:** Identifying crop stress across large agricultural areas is difficult through manual inspection alone.
- **Delayed Disease Detection:** Crop diseases and environmental stress may go unnoticed until visible damage occurs.
- **Inefficient Irrigation:** Watering decisions often lack localized, data-driven insights into crop conditions and weather.
- **Uncertain Yield Estimates:** Farmers lack accessible tools for estimating potential harvests using historical and environmental data.
- **Suboptimal Resource Utilization:** Water, fertilizers, and pesticides may be used inefficiently without reliable information about crop conditions.
- **Fragmented Agricultural Data:** Satellite imagery, weather forecasts, and field-level observations are rarely combined into a single decision-support system.

AgriSense aims to address these challenges by combining remote sensing, machine learning, and accessible software interfaces.

---

## 💡 Our Solution

AgriSense is designed as a multi-layer agricultural intelligence system that processes satellite and environmental data and delivers useful insights through a web dashboard and notification interface.

### Core Features

| Feature | Description |
|---|---|
| 🌿 Crop Health Monitoring | Analyze satellite imagery and vegetation indices to assess crop conditions. |
| 🦠 Plant Disease Classification | Classify crop diseases from plant images using a deep learning model. |
| 🌦️ Weather Intelligence | Incorporate rainfall, temperature, humidity, and weather forecasts into agricultural analysis. |
| 💧 Irrigation Recommendations | Generate data-driven recommendations using crop conditions and weather information. |
| 🧪 Disease and Pest Risk | Estimate potential disease or pest risks using environmental indicators and historical observations. |
| 🌾 Yield Prediction | Estimate potential harvests using historical data, vegetation indicators, and environmental features. |
| 🤖 AI Agricultural Assistant | Provide contextual agricultural information through a natural-language interface. |
| 🔔 Automated Alerts | Deliver timely notifications when monitored conditions indicate potential agricultural risks. |

*Note: These features represent the intended platform scope. Individual capabilities depend on data availability, model development, and validation.*

---

## 🏗️ System Architecture

AgriSense follows a modular, five-layer architecture.

### 1. Data Layer

Collect agricultural and environmental information from multiple sources.

**Planned data sources include:**

- **Sentinel-2:** Multispectral satellite imagery for vegetation monitoring.
- **NASA Earth Observation:** Satellite-derived environmental and land-surface information.
- **ISRO-Supported Earth Observation:** Satellite and geospatial data from suitable sources.
- **Weather APIs:** Temperature, rainfall, humidity, and weather forecasts.
- **Soil and Geospatial Datasets:** Soil characteristics, field boundaries, and location information.
- **Farmer Input:** Crop type, field location, farming practices, and relevant observations.

### 2. Data Ingestion and Preprocessing

Raw data is collected, cleaned, and transformed into a format suitable for machine learning.

Planned operations include:

- Automated data collection through APIs.
- Satellite image filtering and cloud masking.
- Image resizing and geospatial preprocessing.
- Vegetation index calculation, including NDVI.
- Temporal feature extraction.
- Integration of weather and field-level features.
- Storage of processed datasets for model inference.

### 3. Intelligence Layer

Machine learning models process the prepared data to generate agricultural insights.

| Component | Purpose |
|---|---|
| NDVI Engine | Analyze vegetation indices to monitor crop health. |
| Crop Disease Classifier | Identify disease categories from plant images. |
| Disease Risk Model | Estimate potential disease risk using environmental and historical data. |
| Yield Prediction Model | Estimate potential harvest yields using agricultural features. |
| Irrigation Intelligence | Support irrigation decisions using weather and crop-condition information. |
| NLP Assistant | Provide contextual answers based on available agricultural data. |

These components are modular and can be developed, evaluated, and deployed independently.

### 4. Backend and Processing Layer

The backend coordinates model inference, data access, scheduled processing, and communication with the frontend.

**Technologies and components:**

- **FastAPI:** REST API endpoints for model inference and frontend integration.
- **PyTorch:** Deep learning model loading and inference.
- **Celery:** Background processing for computationally intensive tasks.
- **Celery Beat:** Scheduling recurring processing jobs.
- **Object Storage:** Storage for satellite imagery, processed datasets, and model artifacts.
- **Database:** Storage for user information, field metadata, predictions, and historical results.

### 5. Delivery Layer

Insights are delivered through interfaces designed to make agricultural data accessible.

**Planned interfaces:**

- **Web Dashboard:** Crop health indicators, field-level analytics, predictions, and historical trends.
- **Telegram Bot:** Agricultural notifications, risk alerts, and conversational access to insights.

The goal is to present actionable information rather than require farmers to interpret raw satellite imagery or machine learning outputs themselves.

---

## 🧠 Machine Learning Approach

AgriSense uses a modular machine learning architecture, with different models serving different agricultural tasks.

### A. Plant Disease Classification

The current model prototype uses a ResNet50-based image classification architecture implemented with PyTorch.

The classification head consists of:

- ResNet50 backbone.
- Fully connected layer with 512 hidden features.
- ReLU activation.
- Dropout regularization with a probability of 0.2.
- Final classification layer with 94 output classes.

The model weights and associated class mapping are retrieved from Hugging Face.

**Model Repository:** [Saon110/bd-crop-vegetable-plant-disease-model](https://huggingface.co/Saon110/bd-crop-vegetable-plant-disease-model)

#### Inference Pipeline

1. Load an input plant image.
2. Convert the image to RGB format.
3. Resize and center-crop the image to the required dimensions.
4. Normalize the image using ImageNet mean and standard deviation values.
5. Run inference through the classification model.
6. Apply softmax to obtain class probabilities.
7. Return the top three predicted classes and their confidence scores.

The current class mapping covers multiple crops, including banana, cauliflower, corn, cotton, guava, mango, papaya, potato, rice, sugarcane, tea, tomato, and wheat.

### B. Satellite-Based Crop Intelligence

The planned satellite intelligence pipeline will process multispectral and temporal satellite observations.

#### Vegetation Monitoring

Use vegetation indices such as the Normalized Difference Vegetation Index (NDVI) to identify changes in vegetation conditions.

The NDVI formula is:

NDVI = (NIR - Red) / (NIR + Red)

NDVI can help characterize vegetation greenness and changes over time. However, it is not a direct measurement of crop yield or a definitive diagnosis of plant disease.

#### Crop Stress and Disease Risk

Combine vegetation indicators with weather conditions, historical observations, and other relevant features to estimate potential crop stress or disease risk.

#### Yield Estimation

Train predictive models using suitable historical yield records, crop information, environmental variables, and satellite-derived features.

#### Irrigation Intelligence

Combine rainfall forecasts, crop conditions, and additional information such as soil moisture and crop water requirements where reliable data is available.

These models require appropriate datasets, training, evaluation, and field-level validation before their predictions can be considered reliable.

---

## ⚙️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | PyTorch, Torchvision |
| Image Processing | Pillow, NumPy |
| Model Repository | Hugging Face Hub |
| Backend API | FastAPI |
| API Server | Uvicorn |
| Background Processing | Celery |
| Task Scheduling | Celery Beat |
| Weather Data | Weather APIs, including Open-Meteo |
| Satellite Data | Sentinel-2 and suitable NASA/ISRO-supported datasets |
| Frontend | HTML, CSS, JavaScript |
| Data Storage | Object storage and database |
| Version Control | Git, GitHub |

*The table describes the current and planned technology stack. Not every component has been integrated yet.*

---

## 📂 Project Structure

The repository can initially follow this structure:

```text
AgriSense/
│
├── model.py                 # Plant disease classification model
├── app.py                   # FastAPI application
├── requirements.txt         # Python dependencies
├── README.md
│
├── models/
│   └── README.md            # Model artifacts and documentation
│
├── data/
│   └── README.md            # Dataset documentation
│
├── test_images/
│   └── README.md            # Instructions for adding test images
│
├── services/
│   └── README.md            # Data ingestion and processing services
│
└── .gitignore
