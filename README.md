### Structure
The Selenium Project is divided in 3 main parts:
    1. Pascal Triangle 
        - which contains the code for the function requested the first excercise
        - and the automated tests
        - tests can be run using this command in the PascalTriangle directory: 
    2. Paranthesis
        - which contains the code for the function requsted in the second excercise
        - the automated tests 
        - tests can be run using this command in the Paranthesis directory: python3 -m unittest test_pascal_triangle.py
    3. src 
       - which is divided in 3 main directories: pages, tests and utils
            - 'tests' contains the test classes
            - 'pages' contains the pages reflecting the POM
            - and utils

### Prerequisites
- Python 3.x installed on your system.
- Mozilla Browser installed
- **pip** for package management

### Install Dependencies

1. Clone the repository
2. Navigate to the project directory and install dependencies with pip:
     pip3 install -r requirements.txt

### Run the tests
Run the tests in the root directory using the following command
    pytest