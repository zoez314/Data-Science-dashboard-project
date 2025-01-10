import pytest
from pathlib import Path

# Define project_root to point to the absolute path of the project root
project_root = Path(__file__).resolve().parent.parent

# Apply the pytest fixture decorator to create a fixture for db_path
@pytest.fixture
def db_path():
    # Return a pathlib object for the `employee_events.db` file
    return project_root / 'python-package' / 'employee_events' / 'employee_events.db'

# Define a test function to check if the database file exists
def test_db_exists(db_path):
    # Use pathlib's `.is_file` method to assert the database file exists
    assert db_path.is_file(), f"Database file {db_path} does not exist"

# Define a test function to check if the database file is not empty
def test_db_file_nonempty(db_path):
    # Use pathlib's `.stat()` method to check the file size is greater than zero
    assert db_path.stat().st_size > 0, f"Database file {db_path} is empty"

# Apply the pytest fixture decorator to create a fixture for database connection
@pytest.fixture
def db_conn(db_path):
    from sqlite3 import connect
    # Return a connection object to the SQLite database
    return connect(db_path)

# Apply the pytest fixture decorator to create a fixture for table names
@pytest.fixture
def table_names(db_conn):
    # Fetch all table names from the SQLite master table
    name_tuples = db_conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    # Extract table names from the tuples and return them as a list
    return [x[0] for x in name_tuples]

# Define a test function to check if the `employee` table exists
def test_employee_table_exists(table_names):
    # Assert that the string 'employee' is in the list of table names
    assert 'employee' in table_names, "'employee' table does not exist in the database"

# Define a test function to check if the `team` table exists
def test_team_table_exists(table_names):
    # Assert that the string 'team' is in the list of table names
    assert 'team' in table_names, "'team' table does not exist in the database"

# Define a test function to check if the `employee_events` table exists
def test_employee_events_table_exists(table_names):
    # Assert that the string 'employee_events' is in the list of table names
    assert 'employee_events' in table_names, "'employee_events' table does not exist in the database"
