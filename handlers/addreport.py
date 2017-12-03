from flask import request, render_template, redirect, url_for

from model.helloworld import HelloWorld

from experiments.helloworld import HelloWorldExperiment

def add_report(app):
	@app.route('/addreport', methods=['GET', 'POST'])
	def addreport():
	 	name = request.form.get('entitieName')
	 	if name == '':
	 		name = 'not defined'		
		lhw = HelloWorld()
		lhw.name = name
		lhw.put()
		return redirect(url_for('switchboard'))
	return addreport
