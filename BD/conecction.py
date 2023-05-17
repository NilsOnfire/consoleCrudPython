import mysql.connector as connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.connection = connector.connect(
                host='127.0.0.1', 
                user='root', 
                password='',
                database='university'
                
            )
            
        except Error as ex:
            print("connection error:",ex)
       


    def listCourses(self):
        if self.connection.is_connected():
            try:
                cursor=self.connection.cursor()
                cursor.execute("SELECT * FROM course ORDER BY name ASC")    
                rows = cursor.fetchall()
                return rows
            
            except Error as ex:
                print("Connection error:", ex) 
    
    
    def createCourse(self,course):
        if self.connection.is_connected():
            try:
                
                cursor = self.connection.cursor()
                query = "INSERT INTO course (name,credits) VALUES('{0}',{1})"
                cursor.execute(query.format(course[0],course[1]))
                self.connection.commit()
                print("Row inserted successfully\n")
            except Error as ex:
                print("Insertion error: {0}".format(ex))  
                
    def deleteCourse(self,codeCourse):
        if self.connection.is_connected():
            try:
                
                cursor = self.connection.cursor()
                query = "DELETE FROM course WHERE id = {}"
                cursor.execute(query.format(codeCourse))
                self.connection.commit()
                print("Course delete\n")
            except Error as ex:
                print("delete error: {0}".format(ex))  
    
    def updateCourse(self,course):
         if self.connection.is_connected():
            try:
                
                cursor = self.connection.cursor()
                query = "UPDATE course SET name = '{0}', credits = '{1}' WHERE id = {2} "
                cursor.execute(query.format(course[1],course[2],course[0]))
                self.connection.commit()
                print("Row updated successfully\n")
            except Error as ex:
                print("Insertion error: {0}".format(ex))  
                
                    
                      
                    
# co = DAO()
# data=co.listCourses()                
# print(data[0][1])