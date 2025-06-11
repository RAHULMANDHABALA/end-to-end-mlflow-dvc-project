# Kidney Disease Classification using Deep Learning, MLflow, and DagsHub

This repository provides a **production-ready, modular MLOps pipeline** for classifying kidney CT scan images using deep learning (VGG16) with full experiment tracking, model management, and data versioning. The project is designed for reproducibility, scalability, and easy collaboration.

---

## 🚀 Project Overview

- **Goal:** Automatically classify kidney CT scan images into disease categories using a deep learning model.
- **MLOps:** Implements best practices—modular pipelines, configuration management, experiment tracking (MLflow), and data versioning (DVC).
- **Cloud-Ready:** MLflow tracking is integrated with [DagsHub](https://dagshub.com/mandhabalarahul/kidney_disease_classification_DL_MLFLOW.mlflow) for remote experiment management.

---

## 📁 Directory Structure

```
kidney_disease_classification_DL_MLFLOW/
│
├── artifacts/                # Generated data, models, etc. (ignored by git)
│   ├── data_ingestion/
│   ├── prepare_base_model/
│   └── training/
├── config/
│   └── config.yaml           # All pipeline and path configs
├── params.yaml               # Model hyperparameters and training settings
├── src/
│   └── cnnClassifier/
│       ├── components/       # Core logic for each pipeline stage
│       ├── pipeline/         # Pipeline orchestration for each stage
│       ├── config/           # Configuration management
│       ├── entity/           # Data classes for configs
│       └── utils/            # Utility functions (YAML, JSON, etc.)
├── main.py                   # Main pipeline runner
├── requirements.txt          # Python dependencies
├── .gitignore
├── dvc.yaml                  # DVC pipeline (if using DVC)
└── README.md
```

---

## ⚙️ Pipeline Stages

1. **Data Ingestion**
    - Downloads and unzips kidney CT scan images.
    - Ensures idempotency: skips download if data already exists.
    - Data is versioned with DVC (not Git).

2. **Prepare Base Model**
    - Loads VGG16 with ImageNet weights.
    - Modifies the top layers for the kidney disease classification task.
    - Saves both the base and updated model architectures.

3. **Model Training**
    - Loads the prepared model.
    - Trains on the ingested dataset with augmentation.
    - Saves the trained model (`model.h5`).

4. **Model Evaluation**
    - Loads the trained model and evaluates on validation data.
    - Logs metrics and parameters to MLflow (DagsHub backend).
    - Optionally registers the model in the MLflow Model Registry.
  
![Screenshot 2025-06-10 032157](https://github.com/user-attachments/assets/d9268d05-f658-4352-b55d-aaeb69bab9e0)


---

## 🧑‍💻 How to Use

### 1. **Clone the Repository**
```sh
git clone https://github.com/RAHULMANDHABALA/kidney_disease_classification_DL_MLFLOW.git
cd kidney_disease_classification_DL_MLFLOW
```

### 2. **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 3. **Configure MLflow/DagsHub Credentials**
- Get your DagsHub token from [DagsHub Tokens](https://dagshub.com/user/settings/tokens).
- Set environment variables (Windows CMD example):
  ```sh
  set MLFLOW_TRACKING_URI=https://dagshub.com/mandhabalarahul/kidney_disease_classification_DL_MLFLOW.mlflow
  set MLFLOW_TRACKING_USERNAME=mandhabalarahul
  set MLFLOW_TRACKING_PASSWORD=your_dagshub_token
  ```
- Or add these lines at the top of `main.py` (not recommended for shared code):
  ```python
  import os
  os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/mandhabalarahul/kidney_disease_classification_DL_MLFLOW.mlflow"
  os.environ["MLFLOW_TRACKING_USERNAME"] = "mandhabalarahul"
  os.environ["MLFLOW_TRACKING_PASSWORD"] = "your_dagshub_token"
  ```

### 4. **Configure the Pipeline**
- Edit `config/config.yaml` for paths, MLflow URI, and other pipeline settings.
- Edit `params.yaml` for model hyperparameters (image size, batch size, epochs, etc.).

### 5. **Run the Pipeline**
```sh
python main.py
```
- The pipeline will execute all stages in order.
- Logs and artifacts will be saved in the `artifacts/` directory.
- Experiment results will be available in your [DagsHub MLflow UI](https://dagshub.com/mandhabalarahul/kidney_disease_classification_DL_MLFLOW.mlflow).

---

## 📊 Experiment Tracking

- **MLflow** is used for logging parameters, metrics, and models.
- **DagsHub** provides a remote MLflow server for collaborative experiment tracking.
- All runs, metrics, and models are visible at your [DagsHub MLflow UI](https://dagshub.com/mandhabalarahul/kidney_disease_classification_DL_MLFLOW.mlflow).

---

## 📦 Data & Model Versioning

- **DVC** is recommended for versioning large datasets and model files.
- Add data folders (e.g., `artifacts/data_ingestion/`) to `.gitignore` and track them with DVC.
- Example DVC commands:
  ```sh
  dvc add artifacts/data_ingestion/kidney-ct-scan-image
  git add artifacts/data_ingestion/kidney-ct-scan-image.dvc .gitignore
  git commit -m "Track data with DVC"
  dvc push
  ```

---

## 📝 Best Practices

- **Never commit large data or model files to Git.** Use DVC or Git LFS.
- **Keep credentials (tokens) out of code**—use environment variables.
- **Use modular code:** Each pipeline stage is isolated for easy debugging and reuse.
- **Track all experiments:** Use MLflow for every run, even failed ones, for full reproducibility.

---

## 🛠️ Troubleshooting

- **Push errors due to large files:**  
  Remove large files from Git history and use DVC.
- **MLflow authentication errors:**  
  Double-check your DagsHub username and token, and set them as environment variables.
- **Data not downloading:**  
  Ensure the data source URL in `config.yaml` is correct and accessible.

---
