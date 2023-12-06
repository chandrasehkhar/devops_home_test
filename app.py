from flask import Flask, jsonify

app = Flask(__name__)

health_status = False
# hello endpoint
@app.route('/hello')
def hello():
    global health_status
    health_status = not health_status
    return jsonify({'message': 'hello world'})

# health endpoint
@app.route('/health')
def health():
    if health_status:
        resp = jsonify(health="Success")
        resp.status_code = 200
    else:
        resp = jsonify(health="unhealthy")
        resp.status_code = 500

    return resp


if __name__ == '__main__':
     app.run(debug=True)