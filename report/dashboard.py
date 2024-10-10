from fasthtml.common import FastHTML, H1, serve
import matplotlib.pyplot as plt

# Import QueryBase, Employee, Team from employee_events
#### YOUR CODE HERE

# import the load_model function from the utils.py file
#### YOUR CODE HERE

"""
Below, we import the parent classes
you will use for subclassing
"""
from base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
    )

from combined_components import FormGroup, CombinedComponent




# Create a subclass of base_components/dropdown
# called `ReportDropdown`
#### YOUR CODE HERE
    
    # Overwrite the build_component method
    # ensuring it has the same parameters
    # as the Report parent class's method
    #### YOUR CODE HERE
        #  Set the `label` attribute so it is set
        #  to the `name` attribute for the model
        #### YOUR CODE HERE
        
        # Return the output from the
        # parent class's build_component method
        #### YOUR CODE HERE
    
    # Overwrite the `component_data` method
    # Ensure the method uses the same parameters
    # as the parent class method
    #### YOUR CODE HERE
        # Using the model argument
        # call the employee_events method
        # that returns the user-type's
        # names and ids


# Create a subclass of base_components/BaseComponent
# called `Header`
#### YOUR CODE HERE

    # Overwrite the `build_component` method
    # Ensure the method has the same parameters
    # as the parent class
    #### YOUR CODE HERE
        
        # Using the model argument for this method
        # return a fasthtml H1 objects
        # containing the model's name attribute
        #### YOUR CODE HERE
          

# Create a subclass of base_components/MatplotlibViz
# called `LineChart`
#### YOUR CODE HERE
    
    # Overwrite the parent class's `visualization`
    # method. Use the same parameters as the parent
    #### YOUR CODE HERE
    

        # Pass the `asset_id` argument to
        # the model's `event_counts` method to
        # receive the x (Day) and y (event count)
        #### YOUR CODE HERE
        
        # Use the pandas .fillna method to fill nulls with 0
        #### YOUR CODE HERE
        
        # User the pandas .set_index method to set
        # the date column as the index
        #### YOUR CODE HERE
        
        # Sort the index
        #### YOUR CODE HERE
        
        # Use the .cumsum method to change the data
        # in the dataframe to cumulative counts
        #### YOUR CODE HERE
        
        
        # Set the dataframe columns to the list
        # ['Positive', 'Negative']
        #### YOUR CODE HERE
        
        # Initialize a pandas subplot
        #### YOUR CODE HERE
        
        # call the .plot method for the
        # cumulative counts dataframe
        # pass the subplots ax to the .plot method
        #### YOUR CODE HERE
        
        # Set title and labels for x and y axis
        #### YOUR CODE HERE


# Create a subclass of base_components/MatplotlibViz
# called `BarChart`
#### YOUR CODE HERE

    # Create a `predictor` class attribute
    # assign the attribute to the output
    # of the `load_model` utils function
    #### YOUR CODE HERE

    # Overwrite the parent class `visualization` method
    # Use the same parameters as the parent
    #### YOUR CODE HERE

        # Using the model and asset_id arguments
        # pass the `asset_id` to the `.model_data` method
        # to receive the data that can be passed to the machine
        # learning model
        #### YOUR CODE HERE
        
        # Using the predictor class attribute
        # pass the data to the `predict_proba` method
        #### YOUR CODE HERE
        
        # Index the second column of predict_proba output
        # The shape should be (<number of records>, 1)
        #### YOUR CODE HERE
        
        
        # Below, create a `pred` variable set to
        # the number we want to visualize
        #
        # If the model's name attribute is "team"
        # We want to visualize the mean of the predict_proba output
        #### YOUR CODE HERE
            
        # Otherwise set `pred` to the first value
        # of the predict_proba output
        #### YOUR CODE HERE
        
        # Initialize a matplotlib subplot
        #### YOUR CODE HERE
        
        # Run the following code unchanged
        ax.barh([''], [pred])
        ax.set_xlim(0, 1)
        ax.set_title('Predicted Recruitment Risk', fontsize=20)
            
# Create a subclass of base_components/DataTable
# called `NotesTable`
#### YOUR CODE HERE

    # Overwrite the `component_data` method
    # using the same parameters as the parent class
    #### YOUR CODE HERE
        
        # Using the model and entity_id arguments
        # pass the entity_id to the model's .notes 
        # method. Return the output
        #### YOUR CODE HERE
    

class DashboardFilters(FormGroup):

    id = "top-filters"
    action = "/update_data"
    method="POST"

    children = [
        Radio(
            values=["Employee", "Team"],
            name='profile_type',
            hx_get='/update_dropdown',
            hx_target='#selector'
            ),
        ReportDropdown(
            id="selector",
            name="user-selection")
        ]
    
# Create a subclass of CombinedComponents
# called `Report`
#### YOUR CODE HERE

    # Set the `children`
    # class attribute to a list
    # containing all dashboard components
    # in the order the should be displayed
    #### YOUR CODE HERE

# Initialize a fasthtml app 
#### YOUR CODE HERE

# Initialize the `Report` class
#### YOUR CODE HERE



# Apply the app.get decorator
# to a function called `index`
# Set the route to the root
# of the url path
#### YOUR CODE HERE

    # Call the initialized report
    # pass None and an instance
    # of the QueryBase class as arguments
    # Return the result
    #### YOUR CODE HERE

# Apply the app.get decorator
# to a function called `_employee`
# Set the route to /employee
# and parameterize the employee id 
# to a string datatype
#### YOUR CODE HERE

    # Call the initialized report
    # pass the id and an instance
    # of the Employee class as arguments
    # Return the result
    #### YOUR CODE HERE

# Apply the app.get decorator
# to a function called `_team`
# Set the route to /team
# and parameterize the team id 
# to a string datatype
#### YOUR CODE HERE

    # Call the initialized report
    # pass the id and an instance
    # of the Team class as arguments
    # Return the result
    #### YOUR CODE HERE


@app.get('/update_dropdown{r}')
def update_dropdown(r):
    dropdown = DashboardFilters.children[1]
    print('PARAM', r.query_params['profile_type'])
    if r.query_params['profile_type'] == 'Team':
        return dropdown(None, Team())
    elif r.query_params['profile_type'] == 'Employee':
        return dropdown(None, Employee())


@app.post('/update_data')
async def update_data(r):
    from fasthtml.common import RedirectResponse
    data = await r.form()
    profile_type = data._dict['profile_type']
    id = data._dict['user-selection']
    if profile_type == 'Employee':
        return RedirectResponse(f"/employee/{id}", status_code=303)
    elif profile_type == 'Team':
        return RedirectResponse(f"/team/{id}", status_code=303)
    


serve()