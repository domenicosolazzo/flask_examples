from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('template_example.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run( )