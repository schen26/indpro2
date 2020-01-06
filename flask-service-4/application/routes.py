from flask-service-2.rand_let import randLet
from flask-service-3.rand_num import randNum

#get random letter and random number from service 2 and 3 respectively
#link this service to SQL somehow
#the output of this is then linked to service 1

let=rand_let.query.all()
num=rand_num.query.all()



