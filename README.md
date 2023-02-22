# Setup Python/Pytest/PostgreSQL

## Create and activate a virtual environment

From the project's root directory:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

## Install dependencies

After the virtual environment has been created and activated, install the project's dependencies listed in `requirements.txt`

```bash
pip install -r requirements.txt
```

## Environmental Variables

This demo uses 3 environmental variable files.

  1. `.env` contains the variables for the default environment.
  2. `.test.env` contains the variables for the test environment.
  3. `./db-setup-files/.db.env` contains PostgreSQL database credentials used when starting the Docker container.

The first two files have the same structure:

``` text
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
DB_SSL=
```

The `.db.env` file contains only the information used creating the database container:
> NOTE: The variable names are set by PostgreSQL and need to remain consistent.

```text
POSTGRES_PASSWORD=
POSTGRES_USER=
```

## Database setup

### Run the database

Once the environmental variable files have been created, start the database container by running from the project root directory:

```bash
docker-compose up

# Use `docker-compose up --detach` to run the container in a headless process 
```

### Connect to the database

After running `docker-compose up`, you can connect to the database with pgAdmin or another management tool.

### Create database tables

This demo used a single database table `'items'`.  The SQL command to create the table is:

```sql
CREATE TABLE items (
    id SERIAL,
    item_name TEXT NOT NULL
);
```

## Run tests

Run the project's tests from the project root directory:

```bash
pytest .
```
