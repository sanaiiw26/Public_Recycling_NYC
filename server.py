from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open('data/data.json') as f:
    recycling_data = json.load(f)

@app.route('/')
def home():
    return render_template('about.html', data=recycling_data)

@app.route('/macro')
def macro():
    return render_template('macro.html', data=recycling_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/borough/<name>')
def micro(name):
    # Filter data for the borough (case-insensitive)
    filtered = [item for item in recycling_data if item['borough'].lower() == name.lower()]

    # Aggregate bins by site_type
    site_aggregation = {}
    for item in filtered:
        stype = item['site_type']
        if stype not in site_aggregation:
            site_aggregation[stype] = {'paper_bins': 0, 'mgp_bins': 0, 'total_bins': 0}
        site_aggregation[stype]['paper_bins'] += item.get('paper_bins', 0)
        site_aggregation[stype]['mgp_bins'] += item.get('mgp_bins', 0)
        site_aggregation[stype]['total_bins'] += item.get('total_bins', 0)

    # Convert to list for template
    site_data = [
        {'site_type': k, **v} for k, v in site_aggregation.items()
    ]

    return render_template('micro.html', borough=name.upper(), data=site_data)

@app.route('/api/data')
def api_data():
    return jsonify(recycling_data)

if __name__ == '__main__':
    app.run(debug=True)


