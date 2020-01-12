#get the coordination and the outcome on home.html 

from application import app
import requests
from flask import Flask, render_template
from application import db
from application.models import coordinates
#from sqlalchemy import Table, MetaData, create_engine

'''metadata=MetaData()
engine=create_engine('mysql://root:root@35.246.111.139/db')
connection = engine.connect()
getData= 'SELECT * FROM coordinates'
result_proxy = connection.execute(getData)
result = result
 metadata=MetaData()
        coordin=Table('coordiantes', metadata, autoload=True, autoload_with=engine)
        coordData=select([coordin])
        coordData=connection.execute(coordData).fetchall()''' 



@app.route("/", methods=['GET','POST'])
def hitMiss():
    count=0
    list_of_hits=['a1', 'b2', 'c3', 'd4']
    while count<25:
        list=[]
        hitMiss=requests.post('http://service4:5003')
        random_letter=hitMiss.json()["random_letter"]
        random_number=hitMiss.json()["random_number"]
        hitMiss=hitMiss.json()["hitMiss"]
        prevCoord=str(random_letter)+str(random_number)
        if prevCoord in list:
            continue
        else:
            list.append(prevCoord)
            count+=1
        coordData=coordinates.query.all()
        
        #if coordData
        #if list(set(coordData)).sort()==list_of_hits:
            #return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss="You've sunk my battleship!")
        if prevCoord in coordData:
            continue
        else:
            count+=1
            #break
            if coordData.count(prevCoord)>0:
                continue 
            else:
                prevCoord=coordinates(previous_coordinates=prevCoord)
                db.session.add(prevCoord)
                db.session.commit()
                break
            
    return render_template('home.html', random_letter=random_letter, random_number=random_number, hitMiss=hitMiss)


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

