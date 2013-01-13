from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

def generate_good_secret_key():
    import os
    return os.urandom(24)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'] )
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index') )
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

app.secret_key = generate_good_secret_key()

if __name__ == '__main__':
    app.debug = True
    app.run()

