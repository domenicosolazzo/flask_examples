# This example shows how to deal with different routes in Flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show__user_profile(username):
    #show the user profile
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id. Id is an integer
    return 'Post %d' % post_id

@app.route('/post/float/<float:post_id>')
def show_post_float(post_id):
    return 'Post %f' % post_id

@app.route('/post/path/<path:path_url>')
def show_post_path( path_url ):
    return 'Post %s' % path_url
if __name__ == '__main__':
    app.debug = True
    app.run( )