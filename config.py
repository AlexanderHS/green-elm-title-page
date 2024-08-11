import os
from dotenv import load_dotenv

# Attempt to load environment variables from .env file
if load_dotenv():
    print("Successfully loaded .env file")
else:
    print("Warning: .env file not found. Using default values.")

# Get SERVER_NAME from environment variable, with a default value if not set
SERVER_NAME = os.getenv("SERVER_NAME", "green-elm")
SERVER_ICON = f"{SERVER_NAME}.png"

# Print information about the server configuration
print(f"Server Name: {SERVER_NAME}")
print(f"Server Icon: {SERVER_ICON}")
