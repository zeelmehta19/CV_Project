import sqlite3 
import os

conn = sqlite3.connect('job.db')

#NORMAL DATABASE IO OPERATIONS
class Utility:
    def __init__(self):
        pass
    def authenticate(self, fn,password):
        cursor = conn.cursor()
        sql = "SELECT * FROM users where fn = ? AND password = ?"
        cursor.execute(sql,(fn,password))
        row = cursor.fetchone()
        conn.commit()
        if(row):
            return row
        else:
            return False
        
    def forgotPassword(self,email):
        cursor = conn.cursor()
        sql = "SELECT password FROM users where email=?"
        cursor.execute(sql,(email,))
        row = cursor.fetchone()
        conn.commit()
        if(row):
            return row[0]
        else:
            return False
    
    def changePassword(self, fn,oldpass,newpass):
        cursor = conn.cursor()
        sql = "UPDATE users SET password = ? where fn = ?"
        cursor.execute(sql,(newpass,fn))
        conn.commit()
        return True
        
    def insertJob(self,title1,company1,salary1,jobtype1,location1,exp1,desc1,requirements,userId):
        cursor = conn.cursor()
        sql = "INSERT INTO jobs(title,company,salary,jobType,location,experience,description,requirements,postedBy) VALUES(?,?,?,?,?,?,?,?,?)"
        templst = ','.join(requirements)
        cursor.execute(sql,(title1,company1,salary1,jobtype1,location1,exp1,desc1,templst,userId))
        conn.commit()
        return True
    
    def fetchJobs(self):
        cursor = conn.cursor()
        sql = "SELECT * FROM jobs"
        cursor.execute(sql)
        row = cursor.fetchall()
        conn.commit()
        if(row):
            return row
        else:
            return False
    
    def fetchJobWhere(self,title):
        cursor = conn.cursor()
        sql = "SELECT * FROM jobs where title = ?"
        cursor.execute(sql,(title,))
        row = cursor.fetchall()
        conn.commit()
        if(row):
            return row
        else:
            return False
        
    def fetchJobWhereId(self,id):
        cursor = conn.cursor()
        sql = "SELECT * FROM jobs where postedBy = ?"
        cursor.execute(sql,(id,))
        row = cursor.fetchall()
        conn.commit()
        if(row):
            return row
        else:
            return False
    
    def applyJob(self,name,cvPath,jobId,title,company,userId,status):
        #increment apllications
        cursor = conn.cursor()
        sql = "INSERT INTO applications(name,cvPath,jobId,title,company,userId,status) VALUES(?,?,?,?,?,?,?)"
        cursor.execute(sql,(name,cvPath,jobId,title,company,userId,status))
        conn.commit()
        cvScore = self.getCvScore(userId)
        cvScore[2] += 1
        self.updateCvScore(cvScore)
        return True
    
    def fetchApplied(self,name,userId):
        cursor = conn.cursor()
        sql = "SELECT * FROM applications where name = ? AND userId = ?"
        cursor.execute(sql,(name,userId))
        row = cursor.fetchall()
        conn.commit()
        if(row):
            return row
        else:
            return False
    
    def insertScore(self,score):
        cursor = conn.cursor()
        sql = "INSERT INTO scores(userId,name,applicationID,jobID,score) VALUES(?,?,?,?,?)"
        cursor.execute(sql,score)
        conn.commit()
        return True
    
    def createUser(self,fn,ln,age,gender,contact,email,address,city,password,cvPath):
        cursor = conn.cursor()
        sql = "INSERT INTO users(fn,ln,age,gender,contact,address,city,email,password,cvPath) VALUES(?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,(fn,ln,age,gender,contact,address,city,email,password,cvPath))
        conn.commit()
        row = self.authenticate(fn,password)
        userId = row[0]
        sql2 = "INSERT INTO cvScore(userId,name,applications,shortlisted,selected,hired,rejected) VALUES(?,?,?,?,?,?,?)"
        cursor.execute(sql2,(userId,fn,0,0,0,0,0))
        
        conn.commit()
        return True
    
    def fetchAppliedToSort(self,jobId):
        cursor = conn.cursor()
        sql = "SELECT * FROM applications where jobId = ? AND status = ?"
        cursor.execute(sql,(jobId,"Applied"))
        row = cursor.fetchall()
        conn.commit()
        if(row):
            return row
        else:
            return False
    def getCvScore(self,userId):
        cursor = conn.cursor()
        sql = "SELECT * FROM cvScore where userId = ?"
        cursor.execute(sql,(userId,))
        row = cursor.fetchone()
        conn.commit()
        if(row):
            return list(row)
        else:
            return False
    
    def updateCvScore(self,cvScore):
        cursor = conn.cursor()
        sql = "UPDATE cvScore SET applications = ?,shortlisted = ?,selected = ? , hired = ? , rejected = ?  where userId = ?"
        cursor.execute(sql,(cvScore[2],cvScore[3],cvScore[4],cvScore[5],cvScore[6],cvScore[0]))
        conn.commit()
        return True
    
    def changeCvScore(self,userId,status):
        cvScore = self.getCvScore(userId)
        if(status == "Shortlisted"):
            cvScore[3] += 1
        if(status == "Selected"):
            cvScore[4] += 1
        if(status == "Hired"):
            cvScore[5] += 1
        if(status == "Rejected"):
            cvScore[6] += 1
    
        self.updateCvScore(cvScore)
            
        
        
        
    def updateStatus(self,userId,jobId,status):
        self.changeCvScore(userId,status)
        cursor = conn.cursor()
        sql = "UPDATE applications SET status= ? WHERE jobId = ?"
        cursor.execute(sql,(status,jobId))
        row = cursor.fetchall()
        conn.commit()
        if(row):
            return True
        else:
            return False
        
        
    
    def fetchPostedJobs_status_Sorted(self,userId):
        cursor = conn.cursor()
        sql = "SELECT a.name,a.cvPath,a.title,a.company,a.jobId,a.userId FROM jobs j,applications a WHERE j.postedBy = ? AND j.jobId = a.JobId and a.status =? "
        cursor.execute(sql,(userId,"Shortlisted"))
        row = cursor.fetchall()
        conn.commit()
        return row
    
    def getScores(self,userId):
        cursor = conn.cursor()
        sql = "SELECT score from scores where userId = ? "
        cursor.execute(sql,(userId,))
        row = cursor.fetchall()
        conn.commit()
        return row
    
    def getCVScore(self,userId):
        cursor = conn.cursor()
        sql = "SELECT * from cvScore where userId = ? "
        cursor.execute(sql,(userId,))
        row = cursor.fetchone()
        conn.commit()
        return list(row)
    
    
        
    
# CONVERT PDF TO TEXT SCRIPT
   
import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

def pdfToText(cvpath):
    pdf = wi(filename = cvpath , resolution = 300)
    pdfImage = pdf.convert('png')
    imageBlobs = []
    for img in pdfImage.sequence:
        imgPage = wi(image = img)
        imageBlobs.append(imgPage.make_blob('png'))
    recognized_text = []
    for imgBlob in imageBlobs:
        im = Image.open(io.BytesIO(imgBlob))
        text = pytesseract.image_to_string(im, lang = 'eng')
        recognized_text.append(text)    
        return recognized_text
        
