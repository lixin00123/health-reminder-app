# Release Notes – IWM1 (Iteration 1)

**Project:** Health Reminder App  
**Version:** 0.1.0  

---

## 1. Overview
This is the first development iteration (IWM1) of the Health Reminder App.  
The goal of this iteration was to establish the project foundation, set up the repository, implement basic reminder functionality, and prepare the environment for further development.

---

## 2. Implemented Features

### ✔ Project Setup
- Created GitHub repository  
- Added project structure (`src/`, `tests/`, `.github/workflows/`)  
- Created virtual environment  
- Added `requirements.txt`  
- Added `.gitignore` to clean pycache and IDE files  

### ✔ Core Application Logic
- Implemented basic CLI menu in `app.py`  
- Added reminder model  
- Implemented add reminder functionality  
- Implemented JSON-based data persistence in `storage.py`  

### ✔ Development Environment
- Added `pytest.ini` and initial unit test structure  
- Installed packages: `pytest`, `flake8`  

### ✔ CI/CD Progress
- Set up GitHub Actions workflow structure  
- CI file initialized (`ci.yml`)  
- Configured Python environment installers  

---

## 3. Known Issues / Limitations
- No delete reminder function yet  
- View reminders function incomplete  
- No integration tests  
- Dockerfile not added yet  
- Menu options minimal  
- CI pipeline not fully automated  
- No coverage report  

---

## 4. Planned Work for Next Iteration (IWM2)
- Implement delete reminder  
- Implement view reminders  
- Add full test suite (unit + integration)  
- Implement complete GitHub Actions CI  
- Add Dockerfile and containerization  
- Improve code formatting (flake8 compliance)  
- Refactor code for readability  
- Add project screenshots and documentation  

---

## 5. Status Summary
Iteration 1 successfully established the project foundation.  
All core components exist, and the system is ready for feature expansion and DevOps integration in IWM2.

