from flask import Flask, request
import metrics_importation
import sys
from max_dev import maxrest
from reports.publications.articles import report_per_year

app = Flask(__name__)

@app.route('/excel/import', methods=['POST'])
def sync_excel_with_data_base():
    file_path = request.json['file_path']
    metrics_importation.import_articles(file_path)
    metrics_importation.import_videos(file_path)
    return maxrest.build_json_response({'success':True},200)

@app.route('/')
def home():
    return 'HOME'

@app.route('/reports/publications/articles/per_year')
def get_report_publications_per_year():
    try:
        return report_per_year.generate_report()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise