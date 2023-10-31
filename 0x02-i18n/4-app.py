#!/usr/bin/env python3
"""
file  4-app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """create config class"""

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

app.config['LANGUAGES'] = ['en', 'fr']
app.config['SUPPORTED_LANGUAGES'] = ['en', 'fr']
app.config['DEFAULT_LANGUAGE'] = 'en'

@app.route("/", strict_slashes=False)
def index():
    """displays a basic hello world message"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """Gets best match locale according to request
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        if locale == fr:"""
    return 'fr'
    return request.accept_languages.best_match(app.config['SUPPORTED_LANGUAGES'], default=app.config['DEFAULT_LANGUAGE'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
