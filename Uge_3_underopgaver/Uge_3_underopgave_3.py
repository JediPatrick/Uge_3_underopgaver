import re
import csv
from pathlib import Path
import logging

def isWholeNumber(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

def isAFloat(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def containsLetters(s): 
    return bool(re.search(r'[a-zA-Z]', s))

def isValidEmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email) is not None

# the function is delibradly consertative and does not try to fix data to make sure its not taking some scenarios into account 
def checkRowIntegrity(row):
    errorMessage = ""
    errorType = "Warn"
    try:
        if not isWholeNumber(row['customer_id']):
            if row['customer_id'] == "":
                errorMessage += f"CustomerID is empty. "
            else:
                errorMessage += f"CustomerID is invalid {row['customer_id']}. "
        if not isinstance(row['name'], str) and containsLetters(row['name']):
            if row['name'] == "":
                errorMessage += f"Name is empty. "
            else:
                errorMessage += f"Name is invalid {row['name']}. "
        if not isValidEmail(row['email']):
            if row['email'] == "":
                errorMessage += f"Email is empty. "
            else:
                errorMessage += f"Email is invalid {row['email']}. "
        if not isAFloat(row['purchase_amount']):
            if row['purchase_amount'] == "":
                errorMessage += f"Purchase amount is empty. "
            else:
                errorMessage += f"Purchase amount is invalid {row['purchase_amount']}. "

    except Exception as e:
        errorMessage = f'Something unexpected happened. Error: {str(e)}'
        errorType = "Error"

    finally:
        return (errorMessage, errorType)

def underOpgaveTre():
    logging.basicConfig(
    filename=f'log_underopgave_3.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',  
    level=logging.INFO # Minimum log level to capture
)

    file_path = Path('source_data.csv')

    # Check if file exists
    if file_path.is_file():
        data = []
        logging.info("File exist and loaded.")
        with open('source_data.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row_number, row in enumerate(reader, start=2):  # start=2 so the line number is the same as in the csv                
                error = checkRowIntegrity(row)
                if error[0] == "":
                    validRow = {'customer_id': row['customer_id'], 'name': row['name'], 'email': row['email'], 'purchase_amount': row['purchase_amount']}
                    data.append(validRow)
                    print(f"CustomerId: {row['customer_id']}, Name: {row['name']}, Email: {row['email']}, Purchase amount: {row['purchase_amount']}  ")
                else: 
                    if error[1] == "Error":
                        logging.error(f'Error in line {row_number} error: {error[0]}')
                    elif error[1] == "Warn": 
                        logging.error(f'Data is not validin in line {row_number}. Reason: {error[0]}')
        if len(data) > 0:
            fieldnames = ['customer_id', 'name', 'email', 'purchase_amount']
            with open('output_data.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
                
    else:
        logging.warning("File does not exist.")