# User Guide

## Introduction

Welcome to SmartCityNet, a comprehensive simulation of a smart city network infrastructure. This guide will help you get started with setting up and using the various components of the project.

## Prerequisites

- Python 3.x
- Node.js
- MongoDB
- ns-3
- OpenSSL

## Setup Instructions

### Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SmartCityNet.git
    cd SmartCityNet/backend
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure Django settings:
    ```bash
    cp config/settings.example.py config/settings.py
    ```
4. Run the server:
    ```bash
    python manage.py runserver
    ```

### Frontend Setup
1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Start the development server:
    ```bash
    npm start
    ```

### Network Simulation
1. Navigate to the network simulation directory:
    ```bash
    cd ../network_simulation
    ```
2. Run the ns-3 simulation:
    ```bash
    ./waf --run ns3_simulation
    ```

### Security Setup
1. Navigate to the security directory:
    ```bash
    cd ../security
    ```
2. Apply firewall rules:
    ```bash
    sudo ./firewall_rules.sh
    ```
3. Generate and install SSL certificates:
    ```bash
    python encrypt.py
    ```

## Usage

### Accessing the Web Interface
- Open your browser and navigate to `http://localhost:8000` for the backend.
- Access the frontend at `http://localhost:3000`.

### Managing IoT Devices
- Use the web interface to add, remove, and monitor IoT devices in the city.
- View real-time data from sensors and other devices.

### Monitoring Network Traffic
- Use the network management system to monitor traffic and performance.
- Analyze logs and performance metrics to optimize the network.

## Troubleshooting

### Common Issues
- **Server not starting:** Ensure all dependencies are installed and configuration files are correctly set up.
- **Network simulation errors:** Verify that ns-3 is correctly installed and all necessary libraries are available.
- **Security issues:** Ensure firewall rules and SSL certificates are correctly configured.

For further assistance, refer to the project documentation or contact the development team.

## Conclusion

Thank you for using SmartCityNet. We hope this project helps you understand and explore the complexities of network and communication systems in a smart city environment.
