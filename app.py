from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def mpesa_callback():
    data = request.json
    print("Payment Callback Received:", data)  # Debugging
    with open("payments.log", "a") as f:
        f.write(str(data) + "\n")  # Save logs
    return jsonify({"message": "Callback received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render uses port 10000
