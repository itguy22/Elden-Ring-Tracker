#!/bin/bash

# Run database migrations
flask db upgrade

# Start the Flask application
flask run
