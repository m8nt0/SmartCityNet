# Setup Instructions

## Prerequisites

- Python 3.x
- Node.js
- MongoDB
- Hadoop
- Spark
- ns-3
- OMNeT++
- OpenSSL

## Setup Steps

### Backend

1. Navigate to the backend directory:
    ```bash
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

### Frontend

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

### Data Management

1. Navigate to the data management directory:
    ```bash
    cd ../data_management
    ```
2. Run the MongoDB setup script:
    ```bash
    python database_setup/setup_mongodb.py
    ```
3. Run the Cassandra setup script:
    ```bash
    python database_setup/setup_cassandra.py
    ```
4. Run the Hadoop job:
    ```bash
    python data_processing/hadoop_job.py
    ```
5. Run the Spark job:
    ```bash
    python data_processing/spark_job.py
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

### Security

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

## Troubleshooting

### Common Issues

- **Server not starting:** Ensure all dependencies are installed and configuration files are correctly set up.
- **Network simulation errors:** Verify that ns-3 is correctly installed and all necessary libraries are available.
- **Security issues:** Ensure firewall rules and SSL certificates are correctly configured.

For further assistance, refer to the project documentation or contact the development team.
