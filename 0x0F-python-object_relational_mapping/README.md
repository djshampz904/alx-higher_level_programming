# Python object relational mapping
## Description
This project is about Object Relational Mapping (ORM) using SQLAlchemy. It covers how to connect to a MySQL database and perform CRUD operations on a table using SQLAlchemy. It also covers how to create a relationship between two tables and how to perform CRUD operations on a table with a relationship to another table.
### Files
#### <a>0-select_states.py</a>
- This Python script lists all `State` objects from the database `hbtn_0e_6_usa`.
- Usage: `./0-select_states.py`
- Output: `1: California, 2: Arizona, 3: Texas, ...`
- Note: the output is sorted by `id`
#### <a>1-filter_states.py</a>
- This Python script lists all `State` objects from the database `hbtn_0e_6_usa` that contain the letter `a`.
- Usage: `./1-filter_states.py`
- Output: `2: Arizona, 3: Texas, 4: California, ...`
- Note: the output is sorted by `id`
#### <a>2-my_filter_states.py</a>
- This Python script takes in an argument and displays all values in the `states` table of the database `hbtn_0e_6_usa` where `name` matches the argument.
- Usage: `./2-my_filter_states.py <state_name>`
- Output: `2: Arizona, 3: Texas, 4: California, ...`
- Note: the output is sorted by `id`
#### <a>3-my_safe_filter_states.py</a>
- This Python script takes in an argument and displays all values in the `states` table of the database `hbtn_0e_6_usa` where `name` matches the argument. It is safe from MySQL injection.
- Usage: `./3-my_safe_filter_states.py <state_name>`
- Output: `2: Arizona, 3: Texas, 4: California, ...`
- Note: the output is sorted by `id`
- Note: this script uses MySQL `execute()` to execute SQL queries
#### <a>4-cities_by_state.py</a>
- This Python script lists all `City` objects from the database `hbtn_0e_4_usa`.
- Usage: `./4-cities_by_state.py`
- Output: `1: San Francisco, 2: San Jose, 3: Los Angeles, ...`
- Note: the output is sorted by `id`
- Note: this script uses MySQL `execute()` to execute SQL queries
- Note: this script uses the module `relationship` to create a relationship between `State` and `City`
#### <a>5-filter_cities.py</a>
- This Python script takes in the name of a state as an argument and lists all `City` objects of that state.
- Usage: `./5-filter_cities.py <state_name>`
- Output: `1: San Francisco, 2: San Jose, 3: Los Angeles, ...`
- Note: the output is sorted by `id`
- Note: this script uses MySQL `execute()` to execute SQL queries
- Note: this script uses the module `relationship` to create a relationship between `State` and `City`
#### <a>model_state.py</a>
- This Python file contains the class definition of a `State` and an instance `Base` of `declarative_base()`.
- Note: this script uses the module `declarative_base` to create a base class for declarative class definitions
  - 
- Note: this script uses the module `SQLAlchemy` to connect to a MySQL database
#### <a>6-model_state.py</a>
- This Python file contains the class definition of a `State` and an instance `Base` of `declarative_base()`.
- Usage: `./6-model_state.py`
- Note: this script uses the module `declarative_base` to create a base class for declarative class definitions
- Note: this script uses the module `SQLAlchemy` to connect to a MySQL database
#### <a>7-model_state_fetch_all.py</a>

