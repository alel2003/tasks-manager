# 🌟 Task-API

**Task-API is a RESTful API built for managing tasks and records. This project is developed using Django, Django REST Framework (DRF), Docker, and PostgreSQL as the database.

## 🚀 Quick Start Guide

Follow these steps to set up and run the Task-API on your local machine.

### 📂 1. Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/alel2003/tasks-manager.git
cd tasks-manager
```

### 🐍 2. Create a Virtual Environment

```bash
python3 -m venv env
# Activate the environment (Linux/Mac)
source env/bin/activate
# Activate on Windows
env\Scripts\activate
```

### 📦 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 🐳 3. Launch Docker Containers

```bash
sudo docker compose up -d --build
```

### 👤 4. Create Admin User

```bash
sudo docker exec task_api -it sh
python manage.py createsuperuser
```

### 🧪 5. Run Tests

```bash
sudo docker exec task_api -it sh
python manage.py test
```
