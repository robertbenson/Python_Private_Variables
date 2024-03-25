import openpyxl
from openpyxl.styles import Font, Color
import pandas as pd
from Singleton import Singleton


def main():
    singleton = Singleton()

    # Create a new Excel workbook
    workbook = openpyxl.Workbook()

    # Select the default sheet (usually named 'Sheet')
    ws = workbook.active

    # Add data to the Excel sheet
    data = [
        ["Name", "Age", "City"],
        ["John", 28, "New York"],
        ["Alice", 24, "San Francisco"],
        ["Bob", 32, "Los Angeles"]
    ]
    for row in data:
        ws.append(row)
        singleton.increment_counter()

    # Save the workbook to a file
    workbook.save("my_excel_file.xlsx")
    # Print a success message
    print("Excel file created successfully!")
    print("Counter = ", singleton.get_counter()-1)




if __name__ == '__main__':
    main()
