from flask import Flask, render_template, request

import pickle
with open('title_details.pkl', 'rb') as f:
    title_details = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    idx=0
    return render_template('home.html', books=list(title_details.values())[idx:idx+100])



if __name__ == '__main__':
    app.run(debug=True)

