from flask import Blueprint, render_template
from app.models.developer import Developer

developer_bp = Blueprint('developer', __name__)

@developer_bp.route('/')
def index():
    dev = Developer()
    return render_template('index.html', developer=dev)
