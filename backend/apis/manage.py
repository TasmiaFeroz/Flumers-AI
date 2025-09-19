#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# The manage.py file is the entry point for executing Django administrative tasks.
# It provides a command-line interface for managing the Django project.

# Define the main function
# This function sets the default settings module and executes commands.
def main():
    """Run administrative tasks."""
    # Set the default settings module for the Django project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apis.settings')
    try:
        # Import the execute_from_command_line function to handle commands
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an error if Django is not installed or the environment is not set up correctly
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute the command-line arguments passed to the script
    execute_from_command_line(sys.argv)

# Check if the script is being run directly
if __name__ == '__main__':
    # Call the main function to start the administrative tasks
    main()
