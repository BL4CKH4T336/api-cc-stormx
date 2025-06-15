#!/usr/bin/env python3
from flask import Flask, jsonify
import re
import datetime
import random
import string
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
API_KEY = "darkwasd4rk"

def extract_card_details(card_input):
    match = re.search(r'(\d{16})\|(\d{2})\|(\d{2,4})\|(\d{3,4})', card_input)
    if match:
        return match.group(1), match.group(2), match.group(3), match.group(4)
    return None, None, None, None

def format_response(cc, mm, yy, cvv, time_taken):
    return {
        "cc": f"{cc}|{mm}|{yy}|{cvv}",
        "status": "Declined ❌",
        "response": "Soon",
        "result": "Declined 🚫",
        "time": time_taken,
        "gateway": "Site Based 1$"
    }

@app.route('/gate=site/key=<key>/cc=<cc_details>')
def check_cc(key, cc_details):
    if key != API_KEY:
        return jsonify({"error": "Invalid API key"}), 403

    cc, mm, yy, cvv = extract_card_details(cc_details)
    if not cc:
        return jsonify({"error": "Invalid CC format"}), 400

    if len(yy) == 2:
        yy = str(datetime.datetime.now().year // 100 * 100 + int(yy))

    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
    time_taken = str(end_time - start_time).split('.')[0]

    response_data = format_response(cc, mm, yy, cvv, time_taken)
    print(f"cc={cc}|{mm}|{yy}|{cvv}, status=DECLINED, response=Soon")
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)
