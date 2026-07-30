from flask import Blueprint, render_template, request, redirect, url_for
from models.equipment import Equipment
from extensions import db

equipment_bp = Blueprint('equipment', __name__)

@equipment_bp.route('/equipment')
def equipment_list():
    machines = Equipment.query.all()
    return render_template('equipment/list.html', machines=machines)

@equipment_bp.route('/equipment/add', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        machine = Equipment(
            machine_id=request.form['machine_id'],
            name=request.form['name'],
            department=request.form['department'],
            status=request.form['status'],
            serial_number=request.form['serial_number'],
            notes=request.form['notes']
        )
        db.session.add(machine)
        db.session.commit()
        return redirect(url_for('equipment.equipment_list'))
    return render_template('equipment/add.html')
