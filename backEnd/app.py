from flask import Flask
from flask_cors import CORS
from joueur_route import joueurs_bp
from tournoi_route import tournois_bp
from match_route import matchs_bp

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(joueurs_bp,url_prefix='/joueurs')
app.register_blueprint(matchs_bp,url_prefix='/matchs')
app.register_blueprint(tournois_bp,url_prefix='/tournois')


@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

