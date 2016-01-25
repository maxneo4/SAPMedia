from flask import Flask, request, render_template
import metrics_importation
from max_dev import maxrest
from business import reports

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

@app.route('/reports/publications_per_year')
def get_report_publications_per_year():
    rows_and_total = reports.get_rows_from_publications_per_year()
    print rows_and_total
    return render_template('report_publication_per_year.htm', rows_and_total=rows_and_total)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)