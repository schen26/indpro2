from application import app
import random


@app.route('/', methods=['POST'])
def randNumA():
    return str(random.randint(1, 5))

@app.route('/more')
def randNumB():
    return str(random.randint(1, 10))



