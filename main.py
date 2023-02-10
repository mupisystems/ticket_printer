from datetime import datetime
import os
import time
from flask import Flask
from flask import request
from subprocess import check_output

app = Flask(__name__)

@app.route("/imprimir")
def printer_connect():
    print(request.args)
    try:
        check_output("cmd /c type c:\\printer-temp\\ticket-printer.txt > \\\\localhost\\ticket-printer", shell=True)
    except:
        print('impressora não encontrada')
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    datetime_obj = datetime.now()
    print(f"datetime_obj = {datetime_obj}")
    print(f"datetime_obj type = {type(datetime_obj)}")

    folder_name = datetime_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    # ':' is not allowed in folder naming in Windows, so change it to '_'
    folder_name = folder_name.replace(':', '_')
    print(f"Folder name will be: {folder_name}")
    print(f"folder_name type = {type(folder_name)}")

    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")

    folder_directory = cwd + "\\" + folder_name
    print(f"Will try to create new folder : {folder_directory}")
    time.sleep(5)
    print("Finish!")
    app.run()