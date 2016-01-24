from flask import Flask, request
import metrics_importation
import responses

app = Flask(__name__)

@app.route('/excel/import', methods=['POST'])
def sync_excel_with_data_base():
    file_path = request.json['file_path']
    metrics_importation.import_articles(file_path)
    metrics_importation.import_videos(file_path)
    return responses.get_json_status({'success':True},200)