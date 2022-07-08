import os

from flask import Flask, jsonify
import db
from models import Partidos, Test

from flask_apscheduler import APScheduler
import multiprocessing
import random
from matches import Matches

app = Flask(__name__)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

INTERVAL_TASK_ID = 'interval-task-id'

api_futbol = Matches()


def interval_task():
    input_test = Test(random.uniform(19, 31), 'Task-24-Day')
    db.session.add(input_test)
    db.session.commit()

scheduler.add_job(id=INTERVAL_TASK_ID, func=interval_task, trigger='interval',
                  seconds=int(os.getenv("INTERVAL_TASK", default=3600)))


@app.route('/pause-task')
def pause_interval_task():
    scheduler.pause_job(id=INTERVAL_TASK_ID)
    return 'Interval task paused', 200


@app.route('/resume-task')
def resume_interval_task():
    scheduler.resume_job(id=INTERVAL_TASK_ID)
    return 'Interval task resumed', 200


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


@app.route('/test/<int:value>')
def test_db(value):
    input_test = Test(value, 'test')
    db.session.add(input_test)
    db.session.commit()
    return jsonify({
       "valor": value
    })

@app.route('/test')
def test_get_db():
    json = {}
    data = db.session.query(Test).all()
    for info in data:
        aux = {info.id: {
               'test': info.test,
               'valor': info.value}
              }
        json.update(aux)

    return jsonify(json)


@app.route('/futbol')
def test_get_api_matches():
    return api_futbol.get_api_matches()


@app.route('/getfutbol')
def test_get_matches():
    return api_futbol.get_all_matches()



if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True, port=os.getenv("PORT", default=5000))
