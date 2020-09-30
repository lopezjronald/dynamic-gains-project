from tkinter import messagebox

from DatabaseConnection import Database as db
from GetData import GetData

connection_to_database = db.connection_to_database()
cursor = db.database_cursor(connection_to_database)

answer = True
while answer == True:

    trade_records = GetData()
    chosen_file = trade_records.choose_file()

    try:
        with open(chosen_file, newline='') as opened_file:
            skipped_line = GetData.skip_line(opened_file)
            all_data_in_file = GetData.data_in_file(opened_file)
            db.import_data_to_database(all_data_in_file, cursor, connection_to_database)

    except:
        messagebox.showerror("Error", "Sorry. There was a problem with the file you have selected.")
        answer = messagebox.askyesno("Message", "Would you like to continue")
        if answer == False:
            db.disconnect_database(connection_to_database)
            exit()
        else:
            continue

    answer = messagebox.askyesno("Message", "Would you like to choose another file?")

db.disconnect_database(connection_to_database)
exit()
