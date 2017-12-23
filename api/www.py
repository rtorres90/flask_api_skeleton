"""API logic."""

from flask import request, jsonify

from app import app


@app.route('/cat', methods=['PUT'])
def put_test():
    """To call this method use the following command on your terminal.
curl -H "Content-Type: application/json" -i -X PUT -d '{"name":"don gato","age":"13"}' localhost:80/cat
"""
    try:
        json_data = request.get_json(force=True)
        print json_data
        resp = jsonify({'data': 'Success'})
        resp.status_code = 201
    except Exception as e:
        resp = jsonify({'data': str(e)})
        resp.status_code = 500

    return resp


@app.route('/cats', methods=['GET'])
def get_tests():
    """To call this this method use the following command on your terminal.
curl -i -X GET localhost:80/cats
"""
    response = {
        'name': 'Leoncio',
        'age': 5
    }
    resp = jsonify({'data': {'cats': response}})

    return resp, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
