from flask import render_template

# from google.cloud import datastore
from model.helloworld import HelloWorld

from experiments.helloworld import HelloWorldExperiment

def get_switchboard(app):
    @app.route('/')
    def switchboard():
        experiments = [
          #  HelloWorldExperiment()
        ]
        
      #  client = datastore.Client()
      #  query = client.query('HelloWorld')
       # results = list(query.fetch())

        results = HelloWorld.get_all()

        return render_template(
            "switchboard.html", 
            experiments = experiments,
            results = results
        )
        
    return switchboard