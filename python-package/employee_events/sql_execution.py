from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
# YOUR CODE HERE


class QueryMixin:
    
    def run_query(self, query_string):
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result

def query(func):

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query

# Define a `pandas_query` decorator
# YOUR CODE HERE

    # Use the `wraps` decorator
    # YOUR CODE HERE
    # Define an inner function that receives
    # all positional and keyword arguments
    # YOUR CODE HERE
        
        # Call the function passed to the decorator
        # Pass all a positional and keyword arguments
        # to the function
        # YOUR CODE HERE
        
        # Open an sqlite connection to `db_path`
        # YOUR CODE HERE
        
        # pass the output of the called function
        # and the opened connection to
        # the pandas `read_sql` function
        # YOUR CODE HERE
        
        # close the connection
        # YOUR CODE HERE
        
        # Return the output of `read_sql`
        # YOUR CODE HERE
    
    # Return the inner function
    # YOUR CODE HERE

 