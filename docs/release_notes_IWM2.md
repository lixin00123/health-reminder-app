# Release Notes – IWM2 (Final Iteration)

**Project:** Health Reminder App  
**Version:** 1.0.0  
**Date:** 2025-11-26  
**Author:** Li Xin  

---

## 1. Overview
This is the second and final development iteration (IWM2).  
The focus of this phase was completing all core features, implementing testing, setting up CI/CD pipeline, adding Docker support, and preparing documentation.

---

## 2. New Features Implemented in IWM2

### ✔ Complete Application Features
- Added **delete reminder** functionality  
- Added **view reminders** functionality  
- Improved reminder formatting  
- Updated menu navigation  
- Refactored business logic in `reminders.py`  
- Improved JSON handling in `storage.py`  

### ✔ Data Management
- Fully implemented JSON persistence system  
- Added error handling for empty/invalid JSON  
- Ensured automatic file creation  

---

## 3. Testing Enhancements
### ✔ Unit Tests  
- Added full test coverage for storage and reminder logic  
- Test files:
  - `tests/test_reminders.py`
  - `tests/test_integration.py`

### ✔ Integration Tests  
- Verified add/view/delete workflow  
- Ensured menu functionality works end-to-end  

### ✔ Test Results  
- All tests passed successfully (pytest screenshot included)

---

## 4. CI/CD Pipeline (GitHub Actions)
### ✔ CI Pipeline includes:
- Install dependencies  
- Run flake8  
- Run pytest  
- Display test results  
- Triggered on push & pull request to master branch  

### ✔ All pipelines ran successfully  
Included screenshot: `github_actions_success.png`

---

## 5. Docker Integration
### ✔ Dockerfile added
- Python base image  
- Copy application  
- Install dependencies  
- Run CLI app  

### ✔ Docker commands tested
- `docker build` (success)  
- `docker run` (success)  
Screenshots included.

---

## 6. Bug Fixes
- Fixed JSON load errors  
- Fixed index off-by-one issues  
- Resolved merge conflicts  
- Cleaned invalid pycache entries  
- Improved input validation  

---

## 7. Documentation Completed
- README.md  
- Architecture diagram  
- Release notes (IWM1 & IWM2)  
- Added all required screenshots  

---

## 8. Final Status
The Health Reminder App is fully functional, stable, tested, and ready for evaluation.

**All project requirements (IWM1 + IWM2) have been met or exceeded.**

