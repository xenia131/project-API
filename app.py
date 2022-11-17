from flask import Flask, render_template
import connexion
from connexion.exceptions import OAuthProblem

app = connexion.App(__name__, specification_dir = './')
app.add_api('swagger.yml')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
