import random

@app.route('/')
def randNumA():
    return render_template('home.html', random_number=random.randint(1, 10))

def randNumB():
    return render_template('home.html', random_number=random.randint(11, 20))