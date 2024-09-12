# Import the QueryBase class
# YOUR CODE HERE

# Import dependencies needed for sql execution
# YOUR CODE HERE

# Define a subclass of QueryBase
# called Employee
# YOUR CODE HERE

    # Set the class attribute `name`
    # to "employee"
    # YOUR CODE HERE


    # Define a method called `names`
    # that receives not arguments
    # This method should return a list of tuples
    # from an sql execution
    # YOUR CODE HERE
        
        # Query 3
        # Write an SQL query
        # that selects the full name and id for all employees
        # YOUR CODE HERE
    

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    # YOUR CODE HERE
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        # YOUR CODE HERE

    # YOUR CODE HERE
    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id):

        return f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """