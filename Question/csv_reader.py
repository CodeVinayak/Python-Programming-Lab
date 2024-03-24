import pandas as pd

def read_csv_file(file_path, delimiter=',', encoding='utf-8'):
    """
    Reads a CSV file with flexibility for handling various scenarios.

    Args:
        file_path (str): The path to the CSV file.
        delimiter (str, optional): The delimiter used in the CSV file (default is ',').
        encoding (str, optional): The encoding of the CSV file (default is 'utf-8').

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the data from the CSV file.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
        Exception: If there is an issue reading the CSV file.

    Example:
        df = read_csv_file('example.csv', delimiter=';', encoding='latin1')
    """
    try:
        # Read CSV file into a Pandas DataFrame
        df = pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)

        # Additional processing or error handling can be added as needed

        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at '{file_path}' does not exist.")

    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file: {str(e)}")

# Example Usage:
file_path = 'Code\Question\SCOPE FACULTY LIST.csv'
data_frame = read_csv_file(file_path, delimiter=';', encoding='utf-8')
print(data_frame.head())
