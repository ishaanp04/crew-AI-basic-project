# Project Setup and Usage Guide

## Installation and Initialization

Follow these steps to set up and run the application:

1. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

2. Activate the virtual environment:

   ```sh
   venv/Scripts/activate
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Navigate to the project directory:

   ```sh
   cd crewgooglegemini
   ```

5. Run the application and store raw logs:
   ```sh
   python crew.py > output_log_raw.txt
   ```

## Cleaning the Output Log

To clean up the output log, run:

```sh
python clean_the_output.py
```

## Output Files

- **new-blog-post.md**: Contains the actual output of the app.
- **output_log_clean.txt**: Stores terminal logs showing the thought process of the agents.
