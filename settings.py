''' Module which helps shopkeeper to update creds '''
import json
from flask import request, render_template, Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        d = {}
        with open('creds.json') as f:
            d = json.loads(f.read())
            # print(d)
        return render_template('settings.html', **d)
    else:
        with open('creds.json', 'w') as f:
            f.write(json.dumps(request.form))
        return 'Changes saved successfully'
        