from flask import Flask, request
import metrics_importation
import sys
from max_dev import maxrest, root_path
from reports.publications.articles import report_per_year as report_year_articles
from reports.publications.videos import  report_per_year as report_year_videos
from reports.top_owner import report_per_period as report_top_owner
from reports.number_views import  report_per_period as report_number_views
from reports.infographic_publications import  report_per_period as report_infographic_publications
from reports.top_report import report_per_period as report_top
from reports.regions_report import report_per_period as report_regions

app = Flask(__name__)

@app.route('/excel/import', methods=['POST'])
def sync_excel_with_data_base():
    file_path = request.json['file_path']
    metrics_importation.import_articles(file_path)
    metrics_importation.import_videos(file_path)
    return maxrest.build_json_response({'success':True},200)


@app.route('/')
def home():
    return app.send_static_file('selector_report.html')


@app.route('/<path:path>')
def selector(path):
    print path
    return app.send_static_file(path)


@app.route('/reports/publications/articles/per_year/<year>')
def get_report_articles_per_year(year):
    try:
        return report_year_articles.generate_report(year)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

@app.route('/reports/publications/videos/per_year/<year>')
def get_report_videos_per_year(year):
    try:
        return report_year_videos.generate_report(year)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/top_contributor/<type>/<year>/per_quarter/<quarter>')
def get_report_topowner_per_quarter(type, year, quarter):
    try:
        return report_top_owner.generate_report_byquarter(year, quarter, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/top_contributor/<type>/<year>/per_month/<month>')
def get_report_topowner_per_month(type, year, month):
    try:
        return report_top_owner.generate_report_bymonth(year, month, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/top_contributor/<type>/<year>')
def get_report_topowner_per_year(type, year):
    try:
        return report_top_owner.generate_report_byyear(year, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

#Number of views
@app.route('/reports/number_views/<type>/<year>/per_quarter/<quarter>')
def get_report_number_views_per_quarter(type, year, quarter):
    try:
        return report_number_views.generate_report_byquarter(year, quarter, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/number_views/<type>/<year>/per_month/<month>')
def get_report_number_views_per_month(type, year, month):
    try:
        return report_number_views.generate_report_bymonth(year, month, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/number_views/<type>/<year>')
def get_report_number_views_per_year(type, year):
    try:
        return report_number_views.generate_report_byyear(year, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

#Infographic publications
@app.route('/reports/infographic_publications/<year>/per_quarter/<quarter>')
def get_report_infographic_publications_per_quarter(year, quarter):
    try:
        return report_infographic_publications.generate_report_byquarter(year, quarter)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/infographic_publications/<year>/per_month/<month>')
def get_report_infographic_publications_per_month(year, month):
    try:
        return report_infographic_publications.generate_report_bymonth(year, month)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/infographic_publications/<year>')
def get_report_infographic_publications_per_year(year):
    try:
        return report_infographic_publications.generate_report_byyear(year)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

#top reports
@app.route('/reports/top/<target>/<type>/<year>/per_quarter/<quarter>')
def get_report_top_per_quarter(target, type, year, quarter):
    try:
        if target == 'viewed':
            return report_top.generate_reportTopViewed_byquarter(year, quarter, type)
        if target == 'commented':
            return report_top.generate_reportTopCommented_byquarter(year, quarter, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/top/<target>/<type>/<year>/per_month/<month>')
def get_report_top_per_month(target, type, year, month):
    try:
        if target == 'viewed':
            return report_top.generate_reportTopViewed_bymonth(year, month, type)
        if target == 'commented':
            return report_top.generate_reportTopCommented_bymonth(year, month, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/top/<target>/<type>/<year>')
def get_report_top_per_year(target, type, year):
    try:
        if target == 'viewed':
            return report_top.generate_reportTopViewed_byyear(year, type)
        if target == 'commented':
            return report_top.generate_reportTopCommented_byyear(year, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


#regions
@app.route('/reports/regions/<type>/<year>/per_quarter/<quarter>')
def get_report_regions_per_quarter(type, year, quarter):
    try:
        return report_regions.generate_report_byquarter(year, quarter, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/regions/<type>/<year>/per_month/<month>')
def get_report_regions_per_month(type, year, month):
    try:
        return report_regions.generate_report_bymonth(year, month, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/regions/<type>/<year>')
def get_report_regions_per_year(type, year):
    try:
        return report_regions.generate_report_byyear(year, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise