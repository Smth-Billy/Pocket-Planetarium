from flask import Flask, send_from_directory
import os

# Server sederhana untuk menjalankan project Shinta
app = Flask(__name__)

@app.route('/')
def index():
    # Mengarahkan ke file utama solar system
    return send_from_directory('.', 'planetarium.html')

if __name__ == '__main__':
    print("--- Server Berjalan! ---")
    print("Buka browser dan akses: http://127.0.0.1:5000")
    app.run(debug=True,host='0.0.0.0', port=5000)
