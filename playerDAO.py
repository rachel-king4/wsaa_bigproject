# Football Player and Football Club DAO

# Author: Rachel King

import mysql.connector
import dbconfig as cfg
class PlayerDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    # to connect to mysql database
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    # to clost the connection
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    # to get all players from the player table    
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from player"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray
    
    # to get all clubs from the club table
    def getAllClubs(self):
        cursor = self.getcursor()
        sql="select * from club"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionaryClub(result))
        
        self.closeAll()
        return returnArray

    # to get a player from their id
    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from player where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    # to get a club from its id
    def findClubByID(self, id):
        cursor = self.getcursor()
        sql="select * from club where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionaryClub(result)
        self.closeAll()
        return returnvalue
    
    # to create a player in the player table
    def create(self, player):
        cursor = self.getcursor()
        sql="insert into player (name, age, nationality, club) values (%s,%s,%s,%s)"
        values = (player.get("name"), player.get("age"), player.get("nationality"), player.get("club"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        player["id"] = newid
        self.closeAll()
        return player

    # to create a club in the club table
    def createClub(self, club):
            cursor = self.getcursor()
            sql="insert into club (name, number_of_trophies_won, country) values (%s,%s,%s)"
            values = (club.get("name"), club.get("number_of_trophies_won"), club.get("country"))
            cursor.execute(sql, values)

            self.connection.commit()
            newid = cursor.lastrowid
            club["id"] = newid
            self.closeAll()
            return club

    # to update a player in the player table
    def update(self, id, player):
        cursor = self.getcursor()
        sql="update player set name= %s,age=%s, nationality=%s, club=%s  where id = %s"
        
        values = (player.get("name"), player.get("age"), player.get("nationality"), player.get("club"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    # to delete a player from the player table   
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from player where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    # to delete a club from the club table
    def deleteClub(self, id):
        cursor = self.getcursor()
        sql="delete from club where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    # to convert to dictionary for player table
    def convertToDictionary(self, resultLine):
        attkeys=['id','name','age', "nationality", "club"]
        player = {}
        currentkey = 0
        for attrib in resultLine:
            player[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return player

    # to convert to dictionary for club table
    def convertToDictionaryClub(self, resultLine):
        attkeys=['id','name','number_of_trophies_won', "country"]
        club = {}
        currentkey = 0
        for attrib in resultLine:
            club[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return club
        
playerDAO = PlayerDAO()