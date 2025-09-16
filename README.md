# LeukoApp – Blood Cancer Detection Model

*A Laboratory Testing Application by Shawred Analytics*

## 📌 Overview

LeukoApp is a machine learning–powered application designed to assist laboratories in the **early detection of blood cancer** by analyzing blood smear images. Developed under **Shawred Analytics**, this tool provides a reliable and scalable way to support pathologists and lab technicians in diagnostic workflows.

The model leverages **deep learning** techniques to classify blood samples and identify abnormalities associated with leukemia and other blood disorders.

---

## 🚀 Features

* **Automated Blood Smear Analysis** – Upload and analyze blood cell images instantly.
* **Cancer Detection** – Identifies early-stage patterns associated with leukemia.
* **User-Friendly Interface** – Built with **Streamlit** for seamless interaction.
* **Laboratory-Oriented** – Designed to integrate into lab testing environments.
* **Scalable Deployment** – Can be extended to cloud or on-premise servers.

---

## 🏗️ Project Structure

```
LeukoApp/
│
├── app.py                 # Main Streamlit app
├── models/                # Pre-trained ML/DL models
├── data/                  # Sample dataset (if included)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── utils/                 # Helper scripts
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-org>/LeukoApp.git
cd LeukoApp
```

### 2. Create Virtual Environment

```bash
python -m venv leuko_env
source leuko_env/bin/activate    # For Linux/Mac
leuko_env\Scripts\activate       # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app locally:

```bash
streamlit run app.py
```

Upload a blood smear image and the model will predict whether the sample indicates **normal cells** or **potential leukemia presence**.

---

## 📊 Model Details

* **Architecture**: Convolutional Neural Networks (CNNs)
* **Frameworks**: TensorFlow / PyTorch (depending on your build)
* **Input Shape**: 224x224 RGB images
* **Output**: Binary / multi-class classification (Normal vs. Leukemia types)
* **Training Data**: Publicly available annotated blood cell datasets

---

## 🔬 Use Case in Labs

LeukoApp is built for laboratory testing environments where:

* Technicians upload digitized smear images.
* The system provides a **second opinion** for early detection.
* Reports assist doctors in faster decision-making.

---

## 📈 Impact

* **Social**: Assists pathologists with faster and more accurate diagnosis.
* **Economic**: Reduces diagnostic delays, saving hospital costs.
* **Target Audience**: Labs, hospitals, researchers, and diagnostic centers.

---

## 👥 Developed By

**Pavan Kumar Didde And Shaik Zuber**
**Shawred Analytics**

* Research & Development in AI for Healthcare
* Building solutions that bridge **data science and medical diagnostics**

---

## ⚠️ Disclaimer

LeukoApp is a **supportive diagnostic tool** and should not replace professional medical advice. All predictions must be validated by a certified medical professional.

---

Would you like me to make this **more technical (developer-focused)** with dataset links, model training steps, and performance metrics, or keep it **lab-user-friendly** with emphasis on usage and impact?

