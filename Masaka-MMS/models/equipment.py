from extensions import db

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='Active')
    purchase_date = db.Column(db.String(20))
    serial_number = db.Column(db.String(50))
    notes = db.Column(db.Text)
    