#!/bin/bash

# Set the script to exit on any error
set -e

# Define paths to the necessary files
PONG_ENV_PATH="./PongEnv/env_server.py"
MAVEN_PROJECT_PATH="./GRNEAT"
MAIN_CLASS="evolver.Evolver"  # Replace with the actual fully qualified main class name

# Step 1: Run the Python environment server in the background
echo "Starting Python environment server..."
python3 "$PONG_ENV_PATH" &  # Launch the Python server script
ENV_SERVER_PID=$!            # Store the process ID of the Python script

# Wait briefly to ensure the server has started
sleep 3

# Step 2: Run the Maven project
echo "Running Maven project..."
mvn -f "$MAVEN_PROJECT_PATH" exec:java -Dexec.mainClass="$MAIN_CLASS"

# Step 3: Kill the Python environment server after Maven finishes
echo "Stopping Python environment server..."
kill $ENV_SERVER_PID

echo "All tasks completed successfully!"