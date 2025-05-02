# 💰 Bank Fund Prediction Web App

This is a Flask-based web application that predicts a bank fund output using a pre-trained machine learning model. Built with **scikit-learn** and **Flask**, the app features a responsive UI powered by **Tailwind CSS** and is ready for deployment using **Gunicorn** on platforms like **Heroku**.

---

## 🧠 Key Features

- Machine Learning model served via Flask
- Responsive frontend with Tailwind CSS
- HTML templating with Jinja2
- Model loading via `joblib`
- Ready for cloud deployment (Gunicorn + Procfile)
- Predictive results rendered interactively

---

## 🗃️ Suggested Project Structure

Here’s a recommended scalable structure:

```

bank-fund-app/
├── app.py                     # Main Flask app
├── model/
│   └── model.sav              # Serialized ML model
├── templates/
│   └── index.html             # Web template (Tailwind CSS)
├── static/                    # Place for static files (optional)
├── requirements.txt           # Pip dependencies
├── environment.yml            # Conda environment file
├── Procfile                   # For deployment
├── LICENSE
└── README.md

```

> 🔎 Consider separating logic further (e.g., `routes/`, `utils/`, `config.py`) for large apps.

---

## ⚙️ Getting Started with Conda

### 1. Clone the Repository

```bash
git clone https://github.com/2black0/Bank-Fund-Prediction-Web-App.git
cd Bank-Fund-Prediction-Web-App
```

### 2. Create Conda Environment

```bash
conda env create -f environment.yml
conda activate bank-fund-env
```

### 3. Run Locally

```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000/`.

---

## 🐍 `environment.yml`

Use this file to create the conda environment:

```yaml
name: bank-fund-env
channels:
  - defaults
dependencies:
  - python=3.8
  - flask=2.0.1
  - gunicorn=20.1.0
  - joblib=1.0.1
  - numpy=1.21.2
  - pandas=1.3.3
  - scikit-learn=0.24.2
  - scipy=1.7.1
```

You can export from your current env anytime with:

```bash
conda env export --no-builds > environment.yml
```

---

## 🌐 Deployment

Prepare for deployment with Gunicorn:

```bash
gunicorn app:app
```

Ensure `Procfile` contains:

```
web: gunicorn app:app
```

Ready for platforms like **Heroku**, **Render**, or **Railway**.

---

## 🧠 Machine Learning

The ML model (`model.sav`) is trained using scikit-learn and accepts a single numerical input.

You may replace the model with your own using:

```python
import joblib
joblib.dump(my_model, 'model/model.sav')
```

---

## 💡 Web UI

The UI (`index.html`) includes:

* Input form for total fund
* Real-time prediction result
* Institutional logos in footer

Tailwind CSS is loaded via CDN — no additional setup needed.

---

## 📜 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for full details.

---

## 👨‍💻 Author

Created by **Ardy Seto**
Feel free to fork, contribute, or modify for your own use.