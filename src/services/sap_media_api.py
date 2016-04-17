from flask import Flask
import sys
from reports.publications.articles import report_per_year as report_year_articles
from reports.publications.videos import  report_per_year as report_year_videos
from reports.top_owner import report_per_period as report_top_owner
from reports.number_views import  report_per_period as report_number_views
from reports.infographic_publications import  report_per_period as report_infographic_publications
from reports.top_report import report_per_period as report_top
from reports.factor_report import report_per_period as report_factors

from uploadExcel import upload_api

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['xlsx', 'xlsm'])
app.register_blueprint(upload_api)


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
        return report_factors.generate_report_byquarter('Region', year, quarter, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/regions/<type>/<year>/per_month/<month>')
def get_report_regions_per_month(type, year, month):
    try:
        return report_factors.generate_report_bymonth('Region', year, month, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/regions/<type>/<year>')
def get_report_regions_per_year(type, year):
    try:
        return report_factors.generate_report_byyear('Region', year, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


#Move the needle
@app.route('/reports/high_value_themes/<type>/<year>/per_quarter/<quarter>')
def get_report_gca_per_quarter(type, year, quarter):
    try:
        return report_factors.generate_report_byquarter('High Value Themes', year, quarter, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/high_value_themes/<type>/<year>/per_month/<month>')
def get_report_gca_per_month(type, year, month):
    try:
        return report_factors.generate_report_bymonth('Needle', year, month, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/high_value_themes/<type>/<year>')
def get_report_gca_per_year(type, year):
    try:
        return report_factors.generate_report_byyear('Needle', year, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

#board_area
@app.route('/reports/board_area/<type>/<year>/per_quarter/<quarter>')
def get_report_area_per_quarter(type, year, quarter):
    try:
        return report_factors.generate_report_byquarter('BoardArea', year, quarter, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/board_area/<type>/<year>/per_month/<month>')
def get_report_area_per_month(type, year, month):
    try:
        return report_factors.generate_report_bymonth('BoardArea', year, month, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/board_area/<type>/<year>')
def get_report_area_per_year(type, year):
    try:
        return report_factors.generate_report_byyear('BoardArea', year, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


#customer yes no
@app.route('/reports/customerYN/<type>/<year>/per_quarter/<quarter>')
def get_report_customeryn_per_quarter(type, year, quarter):
    try:
        return report_factors.generate_report_byquarter('CustomerYN', year, quarter, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/customerYN/<type>/<year>/per_month/<month>')
def get_report_customeryn_per_month(type, year, month):
    try:
        return report_factors.generate_report_bymonth('CustomerYN', year, month, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


@app.route('/reports/customerYN/<type>/<year>')
def get_report_customeryn_per_year(type, year):
    try:
        return report_factors.generate_report_byyear('CustomerYN', year, type)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise