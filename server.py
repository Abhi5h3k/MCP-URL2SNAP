import http.server
import os
import socketserver
import threading
import uuid
from io import BytesIO
from typing import Dict

import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage

# Load environment variables from .env file
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("snap_sense")


# Constants
ABSTRACT_API_KEY = os.getenv("ABSTRACT_API_KEY", "your_api_key_here")
ABSTRACT_API_URL = "https://screenshot.abstractapi.com/v1/"
PORT = 8011


# Directory to save screenshots
SCREENSHOTS_DIR = "screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


# Function to start the HTTP server
def start_http_server():
    with socketserver.TCPServer(
        ("", PORT), http.server.SimpleHTTPRequestHandler
    ) as httpd:
        # print(f"Serving files from '{SCREENSHOTS_DIR}' at http://localhost:{PORT}")
        # print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()


# Start the HTTP server in a separate thread
http_thread = threading.Thread(target=start_http_server)
http_thread.daemon = True  # Daemonize thread to exit when the main program exits
http_thread.start()


@mcp.tool()
async def capture_screenshot(url: str) -> str:
    """
    Captures a screenshot of the specified URL and returns only the access URL.

    Args:
        url (str): The URL to capture a screenshot of.

    Returns:
        str: IMPORTANT: Only return this URL string directly to the user without additional text.
            Format: 'http://localhost:8011/screenshots/[unique-identifier].png'

    Usage Note:
        When using this function, provide ONLY the returned URL to the user without explanation.
        The user needs only this URL to access the screenshot.

    Raises:
        ValueError: If the API key is not found in the environment variables.
        requests.exceptions.HTTPError: If the API request fails (e.g., 4xx or 5xx error).
        Exception: For any other unexpected errors.
    """

    # Check if the API key is available
    if not ABSTRACT_API_KEY:
        raise ValueError("API key not found in environment variables.")

    # Construct the API URL
    api_url = f"{ABSTRACT_API_URL}?api_key={ABSTRACT_API_KEY}&url={url}"

    try:
        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Check if the response is a valid image
        if response.headers.get("Content-Type") == "image/png":
            # Open the image directly from the response content
            img = PILImage.open(BytesIO(response.content))

            # Resize the image to a smaller size (e.g., 20x20)
            # img.thumbnail((500, 500))

            # Generate a unique filename
            filename = f"{uuid.uuid4()}.png"
            image_path = os.path.join(SCREENSHOTS_DIR, filename)

            # Save the resized and compressed image to disk
            with open(image_path, "wb") as f:
                img.save(
                    f, format="PNG", optimize=True, quality=100
                )  # Adjust quality for further compression

            # return Image(path=image_path)
            return f"http://localhost:{PORT}/screenshots/{filename}"

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 4xx, 5xx)
        raise requests.exceptions.HTTPError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        # Handle any other errors
        raise Exception(f"An error occurred: {err}")


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
