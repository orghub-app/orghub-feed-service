from flask import Flask, jsonify, request, Response, abort
from src.feed import get_feed

app = Flask(__name__)

@app.route('/')
def root():
  return jsonify({ 'message': 'Feed service up and running' })

@app.route('/feed', methods=['GET'])
def feed():
  if 'organizations' in request.args:
    organizations = request.args['organizations'].split(',')
    feeds = map(lambda org: get_feed(org, request.headers.get('Authorization')), organizations)
    feed = sum(feeds, [])
    return jsonify(sorted(feed, key=lambda item: item['created_at'], reverse=True))
  else:
    abort(404)

@app.route('/feed/<organization>', methods=['GET'])
def organization_feed(organization):
  feed = get_feed(organization, request.headers.get('Authorization'))
  return jsonify(feed)