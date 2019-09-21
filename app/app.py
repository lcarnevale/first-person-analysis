# -*- coding: utf-8 -*-

"""Web Server controller

.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'
__description__ = ''
__credits__ = ''


# standard libraries
import argparse
# local libraries
from resources.frequency import Frequency
from resources.match import Match
# third parties libraries
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Frequency, '/frequency')
api.add_resource(Match, '/match')


if __name__ == '__main__':
    description = ('%s\n%s' % (__author__, __description__))
    epilog = ('%s\n%s' % (__credits__, __copyright__))
    parser = argparse.ArgumentParser(
        description = description,
        epilog = epilog
    )

    args = parser.parse_args()

    app.run(host='0.0.0.0', port='5005', debug=True)
