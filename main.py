from CustomUser import *
import math  
# import pandas as pd 
# import numpy as np
# import warnings

def similarity(bob, anne):
    #get similar movie list
    simalarMovies=[]
    for m in bob.ratingList:
        if m in anne.ratingList:
            simalarMovies.append(m)
    print(simalarMovies)

    #get average rating for user 1
    avg=0
    count=0
    for m in bob.ratingList:
        if m in simalarMovies:
            count+=1
            avg = avg + bob.ratingList[m]
    user1AVG = avg / count

    #get average rating for user 2
    avg=0
    count=0
    for m in anne.ratingList:
        if m in simalarMovies:
            count+=1
            avg = avg + anne.ratingList[m]
    user2AVG = avg / count

    #get top sum
    topSum=0
    for movie in simalarMovies:
        topSum = topSum + ((bob.ratingList[movie] - user1AVG) * (anne.ratingList[movie] - user2AVG))
    print("TOPSUM " + str(topSum))

    #get user1 first half of bottom of equation
    bottomSUM1=0
    for m in bob.ratingList:
        if m in simalarMovies:
            bottomSUM1 = bottomSUM1 + ((bob.ratingList[m] - user1AVG)**2)
    print("bottomSUM1 " + str(bottomSUM1))

    #get user2 first half of bottom of equation
    bottomSUM2=0
    for m in anne.ratingList:
        if m in simalarMovies:
            bottomSUM2 = bottomSUM2 + ((anne.ratingList[m] - user2AVG)**2)
    print("bottomSUM2 " + str(bottomSUM2))

    finalScore = topSum / math.sqrt(bottomSUM1 * bottomSUM2)

    return finalScore


userlist=[]
dictt= {"Godfather": 3, "Avengers Endgame": 3, "Scar Face": 5, "Spy Kids": 5, "Twins": 1}
userlist.append(CustomUser("Josh", dictt))
userlist.append(CustomUser("Moiz", {"Godfather": 5, "Avengers Endgame": 5, "Scar Face": 5, "Spy Kids": 5}))
userlist.append(CustomUser("Jomama", {"Godfather": 4, "Avengers Endgame": 3, "Scar Face": 5, "Spy Kids": 5}))


movies={}
seen=[]
initlist=[]
for user in userlist:
    for movie in user.ratingList:
        if movie not in seen:
            seen.append(movie)
            rate=[]
            rate.append(user.ratingList[movie])
            movies[movie] = rate

        else:
            listtt = movies[movie]
            listtt.append(user.ratingList[movie])
        
    print(user.name)
    print(user.ratingList)
print("")
for movie in movies:
    print(movie + str(movies[movie]))
    print(len(movies[movie]))

print(similarity(CustomUser("Moiz", {"Book1": 3, "Book2": 4, "Book3": 5}), CustomUser("Josh", {"Book1": 5, "Book2": 4, "Book3": 3})))
