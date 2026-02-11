# HPE iLO Simulator - Usage Guide

This guide explains how to run and interact with the HPE iLO Simulator (API and Web UI) on your Mac M3 Pro.

## 1. Prerequisites
- **Docker Desktop**: Ensure Docker Desktop is running.
- **Python 3.9+**: For running local automation tests (optional).

## 2. Starting the Simulator
The simulator is containerized for easy deployment. Use Docker Compose to build and start the service:

```bash
# Build and start the container in detached mode
docker compose up -d --build
```

Wait a few seconds for the Flask server to initialize.

## 3. Accessing the Web UI
The simulator provides a modern iLO-styled web interface.

- **URL**: [http://localhost:5000](http://localhost:5000)
- **Login Credentials**:
  - **Username**: `admin`
  - **Password**: `password`

Once logged in, you will be redirected to the **Information Overview** dashboard showing the system health and details.

## 4. Interacting with the Redfish API
The simulator implements the DMTF Redfish standard. You can query system information using `curl` or any API client.

### Get System Details
```bash
curl http://localhost:5000/redfish/v1/Systems/1
```

### Expected Response Snippet
```json
{
    "Manufacturer": "HPE",
    "Model": "ProLiant DL380 Gen10",
    "PowerState": "On",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## 5. Running Automation Tests
If you have set up the `.venv`, you can run the Robot Framework tests:

```bash
# API Test
source .venv/bin/activate
robot tests/redfish_api.robot

# UI Test (requires Chrome)
robot tests/ilo_ui.robot
```

## 6. Stopping the Simulator and Web UI
To stop the simulator and shut down the Web UI/API, use one of the following methods depending on how you started it:

### Method A: Using Docker Compose (Recommended)
```bash
docker compose down
```

### Method B: Using Direct Docker Commands
If you started the container using `docker run`, use:
```bash
# Stop and remove the container
docker stop ilo-simulator && docker rm ilo-simulator
```

Once the container is stopped, the Web UI at `http://localhost:5000` will no longer be accessible.
