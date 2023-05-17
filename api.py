from flask import Flask, jsonify, request
from project136 import data

api = Flask(__name__)

@api.route('/')
def get_status():
    return jsonify({
        'message':'Success'
    })

@api.route('/get_content')
def get_contents():
    return jsonify({
        'data':data
    })

@api.route('/get_details')
def get_details():
    name = request.args.get('name')
    planet = next(i for i in data if i['name'] == name)
    return jsonify({
        'planet_data':planet,
        'status':'success'
    })

if __name__ == '__main__':
    api.run(debug=True)