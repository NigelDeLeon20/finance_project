#Treasurer & Auditor things
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import duckdb

#Database 
scope = [
     "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\craig nigel de leon\repos\finance_project\credentials.json.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Musikalista_Finances_2026-2027").sheet1
raw_data = sheet.get_all_records()
df = pd.DataFrame(raw_data)

#error handling if file is empty
if not raw_data:
    print("File is empty.")
else:
    df = pd.DataFrame(raw_data)
    print("Data found.")

    query = "SELECT * FROM df LIMIT 5"
    print(duckdb.query(query).to_df())



# # Title border
# def header(title):
#     padding = 4
#     border_width = len(title) + padding
#     border = "=" * border_width

#     print(border)
#     print(f"= {title} =")
#     print(border)

# def treasurer():
#     while True:
#         header("     Treasurer Menu     ")
#         print("1. Budget Tracker \n2. Event Transaction \n3. Check Form Filing Deadlines \n4. Back \n5. Exit") 
#         match input("Input your choice: ").strip():
#             case '1' :
#                     budget_tracker()
#             case '2':
#                     event_transaction()
#             case '3' :
#                     check_form_calendar()
#             case '4': #Back to Main Menu
#                     return True
#             case '5': #Exit program
#                     return False
#             case _:
#                     print("Invalid input, try again thank you!")  

# def budget_tracker():
#     while True:
#         header("Budget Tracker")
#         print("1. CSAO Depository \n2. Student Collection \n3. Back")

#         match input("Input: ").strip():
#             case '1':
#                 csao_depository()
#             case '2':
#                 student_collection()
#             case '3':
#                 return True
#             case '4':
#                 return False
#             case _:
#                 print("Invalid input, try again thank you!")
        
# def csao_depository():
#     print("CSAO Depository")

# def student_collection():
#     print("Student Collection")

# def event_transaction():
#     print("transaction")

# def check_form_calendar():
#     print("form calendar...")

# def cash_disbursements():
#     print("cash disbursements...")

# def auditor():
#     header("     Auditor Menu     ")
#     print("1. View Financial Records")
#     print("2. Generate Report")
#     print("3. Exit")


# #Main menu and Navigation
# def main():
#     run = True
#     while run:
#         header("     Main menu     ")
        
#         position = input("Input your position: \n 1. Treasurer \n 2. Auditor \n 3. Exit \n Input: ").strip()
#         match position:
#             case 1 | "1" | "Treasurer" | "treasurer":
#                 # Fixed: If treasurer returns False, break the main loop to exit
#                 if not treasurer():
#                     print("Exiting program... \nThank you, see you again!")
#                     run = False
#             case 2 | "2" | "Auditor" | "auditor":  # Fixed: Added "2" string option
#                 if not auditor():
#                     print("Exiting program... \nThank you, see you again!")
#                     run = False
#             case 3 | "3" | "Exit" | "exit":
#                 print("Exiting program... \nThank you, see you again!")
#                 run = False
                
#             case _:
#                 print("Invalid input. Please try again.")

# if __name__ == "__main__":
#     main()