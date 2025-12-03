import gspread

gc = gspread.service_account(filename='C:/Users/ACER/OneDrive/Documents/GitHub/handybot/mysa.json') #must change on Linux Terminal
sheet = gc.open(SPREADSHEET_NAME) #spreadsheet where the service account already has the editor access
worksheet = sheet.worksheet(WORKSHEET_NAME) #worksheet name in the spreadsheet

# Logic: In a selected column/s get each cells in a row. If there's a value, iterate to the next row. If there's none, update it with a value. End. 
if worksheet.cell(1, 1).value is None:
worksheet.col_values(1)