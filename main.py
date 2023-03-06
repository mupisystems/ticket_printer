from subprocess import check_output
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/imprimir', methods=['GET', 'POST'])
def printer_connect():
    # if request.method == 'POST' and request.is_json:
    if request.method == 'GET':
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

        width = 40
        text_ticket = []
        if header:
            text_ticket.append(header.center(width) + '\n\n')
        if created_date:
            text_ticket.append(created_date + '\n\n')
        if client_name:
            text_ticket.append('Cliente'.center(width) + '\n\n')
            text_ticket.append(client_name.center(width) + '\n\n')
        if code:
            text_ticket.append('Senha'.center(width) + '\n\n')
            text_ticket.append(code.center(width) + '\n\n')
        if services:
            text_ticket.append(services + '\n\n')
        if footer:
            text_ticket.append(footer + '\n\n')

        # if qr_code:
        #     img = qrcode.make(qr_code)
        #     img.save('QRCode.png')

        file = open('C:\printer-temp\ticket-printer.txt', 'w')
        file.writelines(text_ticket)
        file.close()

        check_output("cmd /c type c:\\printer-temp\\ticket-printer.txt > \\\\localhost\\ticket-printer", shell=True)

        return jsonify(status=200)
    return jsonify(status=404)


if __name__ == '__main__':
    app.run()
