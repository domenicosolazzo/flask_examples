# Example that shows how to use the logger inside a flask app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occured (%d apples)', 42)
    app.logger.error('An error occurred')
    
    return 'Hello, World'

if __name__ == '__main__':
    app.debug = True
    app.run( )