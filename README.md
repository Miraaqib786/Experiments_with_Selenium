# STEP 1: Create Your Project Folder
### Create a folder for this experiment, e.g:
    - mkdir DevOps_Experiment_12
    - cd DevOps_Experiment_12
# Part A: Web App Code (JavaScript + HTML)
    - File: app.html
# Part B: Containerization with Docker
- File: Dockerfile
# Build & Run the Container
- docker build -t greeting-app .
- docker run -d -p 8080:80 --name greeting-app-container greeting-app
# Free the port:
- netstat -aon | findstr :8080
- taskkill /PID <PID_HERE> /F
# Remove the old container:
- docker rm -f greeting-app-container
# Part C: Selenium Test Automation
- File: test_app_container.py
# Run the Selenium Script
- python test_app
