# Import any dependencies needed to execute sql queries
import pandas as pd
from sqlite3 import connect
from pathlib import Path

# Define a class called QueryBase
# that has no parent class
class QueryBase:
    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        # Return an empty list
        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):
        """
        Returns a pandas DataFrame with event counts by event_date
        for the given id (could be employee_id or team_id depending on the use case).
        """
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        query = f"""
        SELECT event_date, 
               SUM(positive_events) AS total_positive_events, 
               SUM(negative_events) AS total_negative_events
        FROM {QueryBase.name}
        WHERE {QueryBase.name}_id = {id}
        GROUP BY event_date
        ORDER BY event_date;
        """

        # Execute the query and return a pandas DataFrame
        connection = connect(db_path)
        df = pd.read_sql_query(query, connection)
        connection.close()
        return df

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id):
        """
        Returns a pandas DataFrame with note_date and note from the `notes` table
        for the given id (could be employee_id or team_id depending on the use case).
        """
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        query = f"""
        SELECT note_date, note
        FROM notes
        WHERE {QueryBase.name}_id = {id};
        """

        # Execute the query and return a pandas DataFrame
        connection = connect(db_path)
        df = pd.read_sql_query(query, connection)
        connection.close()
        return df

