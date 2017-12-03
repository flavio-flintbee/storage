import logging

from flask import Flask
from handlers.switchboard import get_switchboard
from handlers.report import get_report
from handlers.deletereport import delete_report
from handlers.addreport import add_report

app = Flask(__name__)

get_switchboard(app)
get_report(app)
delete_report(app)
add_report(app)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500