from flask import render_template
from plo import plo

@plo.route('/')
def index():
    return render_template('index.html')
