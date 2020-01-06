import string
import random

@app.route('/')
def randLet():
    return random.choice(string.ascii_lowercase))

@app.route('/')
def randLet():
    return random.choice(string.ascii_uppercase))

#render_template('home.html', random_letter=random.choice(string.ascii_uppercase))