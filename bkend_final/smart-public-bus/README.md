# Smart Public Bus

## Overview
The Smart Public Bus project aims to provide real-time information about public buses, including crowd levels and estimated time of arrival (ETA). This application is built using FastAPI and is designed to be efficient and easy to use.

## Project Structure
```
smart-public-bus
├── app
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── routers
│   │   │   ├── buses.py
│   │   │   └── health.py
│   │   └── deps.py
│   ├── models
│   │   └── bus.py
│   ├── schemas
│   │   ├── bus.py
│   │   └── estimations.py
│   ├── services
│   │   ├── crowd_estimator.py
│   │   └── eta_estimator.py
│   └── core
│       └── config.py
├── tests
│   ├── test_buses.py
│   └── test_estimators.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Features
- **Live Bus Data**: Access real-time information about buses.
- **Crowd Level Estimation**: Get estimates of the crowd levels on buses.
- **ETA Calculation**: Calculate the estimated time of arrival for buses at specific stops.
- **Health Check**: Verify the status of the application.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd smart-public-bus
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
uvicorn app.main:app --reload
```
You can then access the API at `http://127.0.0.1:8000`.

## API Endpoints
- **GET /buses/**: Retrieve live bus data.
- **GET /buses/{id}/crowd**: Estimate the crowd level for a specific bus.
- **GET /buses/{id}/eta**: Get the ETA for a specific bus.
- **GET /buses/{id}/telemetry**: Retrieve telemetry data for a specific bus.
- **GET /health**: Check the health status of the application.

## Testing
To run the tests, use the following command:
```
pytest
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.