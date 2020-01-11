#get the coordination and the outcome on home.html 

from application import app
import requests
from flask import Flask, render_template
from application import db
from application.models import coordinates 


@app.route("/", methods=['GET','POST'])
def hitMiss():
    count=0
    for i in range(25):#while count<25:'''
    hitMiss=requests.post('http://service4:5003')
        #random_letter=hitMiss.json()["random_letter"]
        #random_number=hitMiss.json()["random_number"]
        #hitMiss=hitMiss.json()["hitMiss"]
'''    if hitMiss.ok:
        random_letter=hitMiss.json()["random_letter"]
        random_number=hitMiss.json()["random_number"]
        hitMiss=hitMiss.json()["hitMiss"]
        prevCoord=str(random_letter)+str(random_number)
        #coordData=coordinates.query.all()
        #db.session.add(prevCoord)
        #db.session.commit()
        return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss=hitMiss)
'''        
    if prevCoord in coordData:
        continue
    else:
        break
    prevCoord=coordinates(previous_coordinates=prevCoord)
    db.session.add(prevCoord)
    db.session.commit()
            
    return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss=hitMiss)
    #return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss=hitMiss)

#    return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss=hitMiss)'''

'''    count=0
    while count<25:
        random_letter=requests.post('http://service2:5001').text
        random_number=requests.post('http://service3:5002').text
        hitMiss=requests.get('http://service4:5003').text

        prevCoord=str(random_letter)+str(random_number)
        coordData=coordinates.query.all()
        if prevCoord in coordData: 
            count += 1
            return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss=hitMiss)
        else:
            prevCoord=coordinates(previous_coordinates=prevCoord)
            db.session.add(prevCoord)
            db.session.commit()
            return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss=hitMiss)
   # return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss=hitMiss)'''

