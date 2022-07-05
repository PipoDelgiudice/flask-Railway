import os

from flask import Flask, jsonify
from db import db
from models import Partidos, Test

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Hello Word": "Welcome to Pipo Flask app"})

@app.route('/api')
def index_api():
    return jsonify({
       "autor":"Pipo Del Giudice",
       "edad":26,
       "profesión":"Desarrollador Back-End"
    })

@app.route('/api/<int:value>')
def test_db(value):

    input_test = Test(value,'test')
    db.session.add(input_test)
    db.session.commit()
    return jsonify({
       "valor": value
    })

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True, port=os.getenv("PORT", default=5000))
