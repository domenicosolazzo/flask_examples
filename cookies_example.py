# Example that shows how to handle cookies with flask
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

# Read a cookie
@app.route('/read')
def reading_cookies():
    username = request.cookies.get('username')
    return 'Username %s' % str(username)

# It store a cookie
@app.route('/store')
def store_cookies():
    resp = make_response( render_template('index.html' ) )
    resp.set_cookie('username', 'the username' )
    return resp
if __name__ == "__main__":
    app.debug = True
    app.run()