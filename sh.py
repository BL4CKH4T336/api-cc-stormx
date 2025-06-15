from flask import Flask, request, jsonify, Response
import json, pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init()

app = Flask(__name__)

def check_card(ccx):
    ccx = ccx.strip()
    try:
        n, mm, yy, cvc = ccx.split("|")
    except:
        return {
            "status": "Invalid Format 🚫",
            "response": "Invalid card format. Use: NUMBER|MM|YY|CVV"
        }

    # Fake declined response always
    return {
        "status": "Declined 🚫",
        "response": "Tere mommy ki chut mai  thuk laga k cum inside kr k tere jaisa ek aur rand ppaida kruga"
    }

@app.route('/key=<key>/cc=<cc>')
def process_cc(key, cc):
    if key != "cytron":
        response_data = {
            "error": "Invalid key",
            "status": "Unauthorized 🚫"
        }
        json_str = json.dumps(response_data, ensure_ascii=False)
        return Response(
            response=json_str,
            status=401,
            mimetype='application/json; charset=utf-8'
        )

    result = check_card(cc)

    response_data = {
        "cc": cc,
        "status": result["status"],
        "response": result["response"]
    }

    json_str = json.dumps(response_data, ensure_ascii=False)
    return Response(
        response=json_str,
        status=200,
        mimetype='application/json; charset=utf-8'
    )

if __name__ == '__main__':
    banner = pyfiglet.figlet_format("CC Checker API")
    print(Fore.CYAN + banner + Style.RESET_ALL)
    print(Fore.GREEN + "[*] Server running on port 7777" + Style.RESET_ALL)

    app.run(host='0.0.0.0', port=7777)
