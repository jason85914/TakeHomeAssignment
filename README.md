# TakeHomeAssignment

## Project Description

This project is a Python API service that retrieves financial data from AlphaVantage API, processes the data, and stores it in a local database. It also provides two API endpoints to retrieve financial data and statistics.

## Tech Stack

- Python 3
- Flask
- SQLAlchemy
- Pandas
- Docker

## How to Run

1. Clone the repository
2. Set up a virtual environment and activate it
3. Install dependencies using `pip install -r requirements.txt`
4. Set up a local database using the schema defined in `schema.sql`
5. Set up an AlphaVantage API key and store it securely
6. Run `python get_raw_data.py` to retrieve and process financial data from AlphaVantage API and store it in the local database
7. Run docker-compose up to start the API service and the database
8. Access the API endpoints using a web browser or a tool like `curl`

## Maintaining API Key

To maintain the API key securely, we recommend storing it in an environment variable or a configuration file that is not tracked by version control. In production, we recommend using a secure key management system like AWS KMS or HashiCorp Vault.

## Deliverables

- `model.py`: ORM model definition for `financial_data` table
- `schema.sql`: SQL schema definition for `financial_data` table
- `get_raw_data.py`: Python script to retrieve and process financial data from AlphaVantage API and store it in the local database
- `Dockerfile`: Dockerfile to build the API service image
- `docker-compose.yml`: Docker Compose file to set up the local development environment
- `README.md`: Project description, tech stack, how to run the code, and how to maintain the API key
- `requirements.txt`: Dependency libraries
- `financial/`: Folder containing API implementation related codes