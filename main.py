from escpos.printer import Network
from flask import Flask, request, jsonify

app = Flask(__name__)
host = '192.168.1.100'  # Printer IP Address

try:
    printer = Network(host=host)
except Exception as excp:
    print(excp)


def reconnect():
    global printer
    try:
        if not printer:
            printer = Network(host=host)
        if not printer.device:
            printer.open()
        return True
    except Exception as excp:
        print(excp)
        return False


@app.route('/imprimir', methods=['GET', 'POST'])
def printer_connect():
    # if request.method == 'POST' and request.is_json:
    if request.method == 'POST':
        global printer

        if (not printer or not printer.device) and not reconnect():
            return jsonify(status=404, data={'error': 'Unable to connect to printer'})

        header = request.args.get('header')
        footer = request.args.get('footer')
        code = request.args.get('code')
        client_name = request.args.get('client_name')
        qr_code = request.args.get('qr_code')
        created_date = request.args.get('created_date')
        services = request.args.get('services')

        # print(header)
        # print(footer)
        # print(code)
        # print(client_name)
        # print(qr_code)
        # print(created_date)
        # print(services)

        # Print text
        if header:
            printer.set(font="a", height=2, align="center")
            printer.text(header + '\n')
            printer.set(font="a", height=2, align="left")
        if client_name:
            printer.text(client_name + '\n')
        if code:
            printer.text(code + '\n')
        if created_date:
            printer.text(created_date + '\n')
        if services:
            printer.text(services + '\n')

        # Print QR Code
        if qr_code:
            printer.qr(content=qr_code)

        if footer:
            printer.text(footer + '\n')

        #  Cut paper
        printer.cut()

        return jsonify(status=200)
    return jsonify(status=404)


if __name__ == '__main__':
    app.run()
