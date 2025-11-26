# Health Reminder App

A lightweight command-line application that helps users create, view, and delete health reminders.  
The project includes full test coverage, Docker support, CI/CD automation with GitHub Actions, and clean modular design.

---

## 🚀 Features

### ✔ Add a reminder  
Users can create reminders with:
- Title  
- Time (e.g., `"08:30 AM"`)  
- Repeat schedule (e.g., `"daily"`, `"weekly"`)

### ✔ View all reminders  
Displays all saved reminders from `reminders.json`.

### ✔ Delete a reminder  
Users can delete reminders by selecting an index.

### ✔ Data persistence  
All reminders are stored in JSON format using `storage.py`.

### ✔ Fully tested  
Unit tests and integration tests were implemented using **pytest**.

### ✔ Continuous Integration  
GitHub Actions pipeline performs:
- Python setup  
- Dependency installation  
- flake8 style check  
- pytest execution

### ✔ Docker Support  
The app runs in an isolated and reproducible Docker container.

---

## 🗂 Project Structure

health-reminder-app/
│
├── src/
│ ├── app.py # Main application interface
│ ├── reminders.py # Reminder manager (CRUD operations)
│ ├── storage.py # File storage (JSON read/write)
│ └── reminders.json # Local JSON database
│
├── tests/
│ ├── test_reminders.py # Unit tests for reminders module
│ └── test_integration.py # Full workflow integration test
│
├── screenshots/ # Demonstration images
│
├── Dockerfile # Docker environment definition
├── requirements.txt # Python dependencies
├── pytest.ini # pytest configuration
├── .gitignore # Clean project from unnecessary files
└── .github/workflows/ci.yml # GitHub Actions CI pipeline




---

## 📸 Screenshots

Below are the key screenshots demonstrating application functionality and CI workflow:

| Screenshot | Description |
|-----------|-------------|
| `add_reminder.png` | Adding a new reminder |
| `view_reminders.png` | Viewing saved reminders |
| `delete_reminder.png` | Deleting a reminder |
| `app_running.png` | Main menu running |
| `pytest_all_tests_passed.png` | All tests passed |
| `docker_build.png` | Docker image build success |
| `docker_run.png` | Running the app in Docker |
| `exit_success.png` | App exit screen |
| `reminders_json_content.png` | JSON data file |
| `repository_structure.png` | Repository file layout |
| `push_success.png` | Git push success |
| `github_actions_success.png` | GitHub Actions CI success |

---

## 🧪 Running Tests

### Run all tests:
```bash
pytest -v



### Configuration

The project uses:

* `pytest.ini`
* Assertions for functional accuracy
* Integration testing for full app behavior

---

## 🐳 Running with Docker

### 1. Build the Docker image

```bash
docker build -t health-reminder-app .
```

### 2. Run the application

```bash
docker run -it health-reminder-app
```

---

## 🔧 Running Locally (without Docker)

```bash
python src/app.py
```

Make sure to install dependencies first:

```bash
pip install -r requirements.txt
```

---

## 🔄 Continuous Integration (GitHub Actions)

The CI pipeline validates every commit:

* Python 3.10 environment setup
* Install dependencies
* Run flake8 style checks
* Run pytest
* Ensure repository integrity

Workflow file:
`.github/workflows/ci.yml`

---

## 📦 Dependencies

```
pytest==7.4.4
flake8==6.1.0
```

Installed via:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Li Xin**
Master student, Al-Farabi Kazakh National University
Faculty of Information Technology

---

## 📜 License

This project is for academic use under the IWM practical assignment.
