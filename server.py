from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load the JSON data once
with open('data/data.json') as f:
    recycling_data = json.load(f)

@app.route('/')
def macro():
    return render_template('macro.html', data=recycling_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/borough/<name>')
def micro(name):
    borough_data = [item for item in recycling_data if item['Borough'].lower() == name.lower()]
    return render_template('micro.html', borough=name.title(), data=borough_data)

@app.route('/api/data')
def api_data():
    return jsonify(recycling_data)

if __name__ == '__main__':
    app.run(debug=True)
