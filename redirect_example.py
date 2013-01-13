# Example that shows how to handle redirect and aborts of requests.

from flask import Flask, abort, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    #never goes here....
# It handles 404 requests.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run()