# -*- coding: utf-8 -*-

"""

.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'

# local libraries
from common.firstPerson import FirstPerson
# third parties libraries
from flask import request
from flask_restful import Resource

class Match(Resource):
    """
    """
    def __init__(self):
        """
        """
        self.firstPerson = FirstPerson()

    def post(self):
        """HTTP POST Request
        """
        json_data = request.get_json(force=True)

        # reading the request's body
        try:
            utterances = json_data['utterances']
        except KeyError as e:
            return {}

        freq = self.firstPerson.match(utterances)

        return {
            "match": freq
        }
