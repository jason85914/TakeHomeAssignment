# TakeHomeAssignment

## Project Description

This project is a Python API service that retrieves financial data from AlphaVantage API  for the recent two weeks, processes the data, and stores it in a local database. It also provides two API endpoints to retrieve financial data and statistics.

## Tech Stack

- Python 3
- Flask
- SQLAlchemy
- Pandas
- Docker

## How to Run

1. Clone the repository.
2. Set up a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.
4. Set up an AlphaVantage API key and store it securely.
5. Run `python get_raw_data.py` to retrieve and process financial data from AlphaVantage API and store it in the local database.
6. Build the Docker image using `docker build -t financial-api .`.
7. Run `docker-compose up` to start the API service and the database.

## Example: Checking Container Status

To check the status of the Docker container, you can use the `docker ps` command. This command will show you a list of all running containers, along with their container IDs and names.

`docker ps --format "table {{.ID}}\t{{.Names}}"`

This command will output a table with the container ID and name for each running container.

Once you have the container ID, you can use the docker exec command to run a command inside the container. For example, you can use the following command to send a GET request to the API and check if it is running:

`docker exec -it <container-id> curl "http://localhost:5000"`

You should replace <container-id> with the actual container ID. If the API is running, you should see the message "Connected!" in the output.

## Maintaining API Key

To maintain the API key securely, we recommend storing it in an environment variable or a configuration file that is not tracked by version control. In production, we recommend using a secure key management system like AWS KMS or HashiCorp Vault.

## Deliverables

- `model.py`: ORM model definition for `financial_data` table.
- `get_raw_data.py`: Python script to retrieve and process financial data from AlphaVantage API and store it in the local database.
- `Dockerfile`: Dockerfile to build the API service image.
- `docker-compose.yml`: Docker Compose file to set up the local development environment.
- `README.md`: Project description, tech stack, how to run the code, and how to maintain the API key.
- `requirements.txt`: Dependency libraries.
- `financial/`: Folder containing API implementation related codes.