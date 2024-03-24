# A.Imagine you are working on a project that involves scraping data from various websites. However, some of the websites are returning HTTP error codes, causing your script to fail. Write a try-except block using Python that handles the requests and causing the code to raise a HTTPError exception and logs the error to a file.
# B.Assume you are writing a function that connects to a remote server to retrieve data. However, sometimes the server is not available, causing the function to raise a ConnectionError exception. Write a try-except block using Python that handles the ConnectionError exception and retries the connection a specified number of times before giving up.

import requests
# Define the URL and log file name for Part A
url_part_a = "https://example.com"
log_file_part_a = "http_error_log.txt"
# Define the URL and retry settings for Part B
url_part_b = "https://example.com"
max_retries = 3

try:
    # Part A: Handling HTTP errors and logging to a file
    try:
        # Make a request to the website for Part A
        response_a = requests.get(url_part_a)  
        # Check if the response contains an HTTP error
        response_a.raise_for_status()
        # Process the data here for Part A
    except requests.exceptions.HTTPError as http_error:
        # Log the error to a file for Part A
        with open(log_file_part_a, "a") as log_a:
            log_a.write(f"HTTP Error: {http_error}\n")
        print(f"HTTP Error: {http_error}")
    except requests.exceptions.RequestException as request_exception:
        print(f"Request Exception (Part A): {request_exception}")

    # Part B: Handling ConnectionErrors and retries
    for _ in range(max_retries):
        try:
            # Attempt to connect to the remote server for Part B
            response_b = requests.get(url_part_b)
            response_b.raise_for_status()
            # Process the data here for Part B
            break  # Successful connection, exit the loop for Part B
        except requests.exceptions.ConnectionError as connection_error:
            print(f"Connection Error (Part B): {connection_error}")
            print("Retrying...")
            continue
except requests.exceptions.RequestException as request_exception:
    print(f"Request Exception (Part B): {request_exception}")
else:
    print("Connection successful!")

