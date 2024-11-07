#!/usr/bin/python3
# Import required modules
from datetime import datetime

# Initialize data structures
clients = {}
jobs = {}
client_id_counter = 1
job_id_counter = 1


def display_menu():
    """Display the main menu options"""
    print("\n===== FREELANCE JOB MANAGER =====")
    print("\nOur app is designed to help you stay in control of your freelance business with three essential features:")
    print("1. Client Management")
    print("2. Job Management")
    print("3. Financial Overview")
    print("\nLet’s get started on simplifying your freelance workflow!")
    print("\nPress 4 to quit the App")
