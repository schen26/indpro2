from application import app
import requests

#get random letter and random number from service 2 and 3 respectively
#link this service to SQL somehow
#the output of this is then linked to service 1

@app.route('/')
def hit_or_miss():
    random_letter=requests.post('http://service2:5001').text
    random_number=requests.post('http://service3:5002').text



    coordination = random_letter + random_number
    list_of_hits = ['a1', 'b2', 'c3', 'd4']


    if coordination in list_of_hits:
        return "You hit my battleship!"
    else:
        return "You miss my battleship!"
