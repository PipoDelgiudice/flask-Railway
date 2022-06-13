from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Hello Word": "Welcome to Pipo Flask app"})

@app.route('/api')
def index():
    return jsonify({
   "autor":"Pipo Del Giudice",
   "edad":26,
   "profesión":"Desarrollador Back-End"
    })


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
