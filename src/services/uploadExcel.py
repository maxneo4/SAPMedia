from flask import request
from werkzeug import secure_filename
import metrics_importation
from max_dev import maxrest
import os
from flask import Blueprint, current_app


upload_api = Blueprint('upload_api', __name__)


@upload_api.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    year = request.form['year']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return import_excel(file_path, year)
    return "file not allowed"


def import_excel(file_path, year):
    metrics_importation.import_articles(file_path, year)
    metrics_importation.import_videos(file_path, year)
    return maxrest.build_json_response({'success':True},200)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']