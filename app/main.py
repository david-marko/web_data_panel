from flask import Flask, request, jsonify, make_response
from sqlalchemy import create_engine
import datetime
import uuid
from user_agents import parse
import maxminddb

app = Flask(__name__)
reader = maxminddb.open_database('app/Geoacumen-Country.mmdb')

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///traffic.sqlite"
app.config['SECRET_KEY'] = "random string"

# app.app_context().push()


# db = SQLAlchemy(app)

# class traffic(db.Model):
#     id = db.Column('id', db.Integer, primary_key = True)
#     uuid = db.Column(db.String(100)) # Unique address incase of returning visitors
#     user_agent = db.Column(db.String(250))
#     os = db.Column(db.String(250))
#     device = db.Column(db.String(250)) 
#     ip = db.Column(db.String(100)) 
#     country = db.Column(db.String(100)) 
#     date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

#     def __init__(self, uuid, user_agent, os,device, ip, country):
#         self.uuid = uuid
#         self.user_agent = user_agent
#         self.os = os
#         self.device = device
#         self.ip = ip
#         self.country = country

@app.route('/')
def hello():
    name = request.cookies.get('u_id')
    if not name:
        u_id = uuid.uuid4().hex
    else:
        u_id = name
    # ua_string = request.user_agent.string
    # user_agent = parse(ua_string)
    # browser = user_agent.browser.family
    # os = user_agent.os.family
    # device = user_agent.device.family
    # ip = request.remote_addr
    # country = reader.get(ip)['country']['iso_code']
    # visit = traffic(u_id, browser,os, device, ip, country)
    # db.session.add(visit)
    # db.session.commit()
    resp = make_response(jsonify({'status': 'success'}))
    resp.set_cookie('u_id', u_id)
    return resp

@app.route('/test')
def test():
    return jsonify({'status':'success'})

# Routes - 
# - Installation
# - Authenticate
# - Webhook
# - Dashboard
# - Ajax_loader
# - Export to file

if __name__ == '__main__':
    # db.create_all()  
    app.run()