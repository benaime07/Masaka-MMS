from flask import Flask, render_template
from config import Config
from extensions import db
from models.equipment import Equipment

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

from routes.equipment import equipment_bp
app.register_blueprint(equipment_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    