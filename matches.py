import requests
import json
import db
import os
from models import Partidos, Test, Match
import datetime
from flask import jsonify
from collections import defaultdict
from dataclasses import asdict, dataclass, field

class Matches:

    def __init__(self):
        self.token = os.getenv('API_KEY_FOOTBALL', default='4741284c5065471faf674773967d83e5')

    def get_api_matches(self):
        #Se configura URL y head con api key
        uri = 'https://api.football-data.org/v4/competitions/2000/matches'
        headers = {'X-Auth-Token': self.token}

        response = requests.get(uri, headers=headers)
        if response.status_code == 200:
            resp = response.json()
            for match in resp['matches']:
              if not match['homeTeam']['name'] is None:
                if not self.store_db(match['id']):
                    print('====================='+match['utcDate']+'======================')
                    print('etapa: ' + match['stage'], match['group'])
                    print('Juega: ' + match['homeTeam']['name'], 'Contra' + match['awayTeam']['name'])
                    match = Partidos(match['id'],
                                     match['homeTeam']['name'],
                                     match['awayTeam']['name'],
                                     datetime.datetime.fromisoformat(match['utcDate'][:-1]).strftime('%Y-%m-%d %H:%M:%S'),
                                     self.get_store(match["score"]),
                                     match['status'])

                    db.session.add(match)
                    db.session.commit()
                else:
                    match_db = self.get_by_id(match['id'])
                    match_db.local = match['homeTeam']['name']
                    match_db.visitante = match['awayTeam']['name']
                    match_db.fecha = datetime.datetime.fromisoformat(match['utcDate'][:-1]).strftime('%Y-%m-%d %H:%M:%S')
                    match_db.score = self.get_store(match["score"])
                    match_db.status = match['status']
                    match_db.last_update = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                    db.session.commit()

            return jsonify({"Results": 'Successful'}), 200

        return jsonify({"Results": 'Fail to get data from API'}), 500


    def store_db(self, id_input):
        datos = db.session.query(Partidos).filter_by(id=id_input).first()
        if datos is not None:
            return True
        return False

    def get_by_id(self, id_input):
        return db.session.query(Partidos).filter_by(id=id_input).first()

    def get_all_matches(self):
        matches = db.session.query(Partidos).all()
        for each in matches:
            m = Match()
            m.id = each.id
            m.local = each.local
            m.visitante = each.visitante
            m.fecha = each.fecha
            m.last_update = each.last_update
            m.score = each.score
            m.Status = each.Status
            matches.append(m)
        return [asdict(m) for m in matches]

    def get_store(self, score):
        if score["fullTime"]["home"] is None and score["fullTime"]["away"] is None:
            return '0 - 0'
        else:
            return f'{score["fullTime"]["home"]} - {score["fullTime"]["away"]}'