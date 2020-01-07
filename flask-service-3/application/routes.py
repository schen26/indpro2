from application import app
import random


@app.route('/')
def randNumA():
    return random.randint(1, 5)

@app.route('/more')
def randNumB():
    return random.randint(1, 10)



