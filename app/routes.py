from app import app
from flask import render_template #esta libreria renderiza web en html

@app.route('/')
def index():
    return render_template('index.html')