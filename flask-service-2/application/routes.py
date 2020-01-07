from application import app
import string
import random

@app.route('/', methods=['POST'])
def randLet():
    return chr(random.randrange(97, 102))

@app.route('/upper')
def upperLet():
    return random.choice(string.ascii_uppercase)

#render_template('home.html', random_letter=random.choice(string.ascii_uppercase))
