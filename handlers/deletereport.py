import json

from google.appengine.ext import ndb
from flask import request, render_template

from model.helloworld import HelloWorld



def delete_report(app):
    @app.route('/delete_report')
    def delete():
        experiments = [
          #  HelloWorldExperiment()
        ]
        keystr = request.args.get('key')
        key = ndb.Key(urlsafe=keystr)
        key.delete()
        results = HelloWorld.get_all()
        return render_template(
            "switchboard.html", 
            experiments = experiments,
            results = results
        )
    return delete