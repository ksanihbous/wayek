from app import app, scrap
from flask import render_template, send_file ,flash, url_for
from flask import request
from app.forms import LoginForm
import requests, re, json , random , urllib
from bs4 import BeautifulSoup, SoupStrainer
_session = requests.session()

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html',title='LESSON')
	
@app.route('/image',methods=['POST','GET'])
def rest_image():
	this_query = request.args['query']
	this_rest = scrap.img(this_query)
	return json.dumps(this_rest, indent=4)
	
@app.route('/instagram',methods=['POST','GET'])
def rest_insta():
	this_user = request.args['username']
	this_rest = scrap.instaprofile(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/twitter',methods=['POST','GET'])
def rest_twitters():
	this_user = request.args['username']
	this_rest = scrap.twitterprofile(this_user)
	return json.dumps(this_rest, indent=4)

@app.route('/sifatnama',methods=['POST','GET'])
def rest_sifat():
	this_name = request.args['nama']
	this_rest = scrap.sifatnama(this_name)
	return json.dumps(this_rest, indent=4)

@app.route('/cctv',methods=['POST','GET'])
def rest_cctv():
	this_code = request.args['code']
	this_rest = scrap.cctv(this_code)
	return json.dumps(this_rest, indent=4)

@app.route('/artinama',methods=['POST','GET'])
def rest_artinamax():
	this_nama = request.args['nama']
	this_rest = scrap.artinama(this_nama)
	return json.dumps(this_rest, indent=4)

@app.route('/kbbi',methods=['POST','GET'])
def rest_kbbix():
	this_arti = request.args['arti']
	this_rest = scrap.kbbi(this_arti)
	return json.dumps(this_rest, indent=4)

@app.route('/maps',methods=['POST','GET'])
def rest_map():
	this_city = request.args['city']
	this_rest = scrap.maps(this_city)
	return json.dumps(this_rest, indent=4)

@app.route('/bitly/shorten',methods=['POST','GET'])
def rest_bitlys():
	this_link = request.args['link']
	this_rest = scrap.bitly(this_link)
	return json.dumps(this_rest, indent=4)

@app.route('/bitly/click',methods=['POST','GET'])
def rest_bitlyss():
	this_link = request.args['link']
	this_rest = scrap.bitly2(this_link)
	return json.dumps(this_rest, indent=4)

@app.route('/sms',methods=['POST','GET'])
def rest_smss():
	this_noo = request.args['no']
	this_msg = request.args['pesan']
	this_rest = scrap.sms(this_noo,this_msg)
	return json.dumps(this_rest, indent=4)

@app.route('/bmkg',methods=['POST','GET'])
def rest_bmkgs():
	this_rest = scrap.bmkg()
	return json.dumps(this_rest, indent=4)

@app.route('/linetodaytopheadline',methods=['POST','GET'])
def rest_linetodays():
	this_rest = scrap.linetodayheadline()
	return json.dumps(this_rest, indent=4)

@app.route('/kutipan',methods=['POST','GET'])
def rest_quotess():
	this_rest = scrap.kutipan()
	return json.dumps(this_rest, indent=4)
