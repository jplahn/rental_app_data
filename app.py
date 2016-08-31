import os

from flask import Flask

app = Flask(__name__)

@app.route('/city/<city>')
def get_city(city):
    return city

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
