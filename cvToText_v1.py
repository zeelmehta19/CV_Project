# 1.menu to post for job position             --- complete 12.00
# 2.the details will go to sqlite3 database   --- complete 12.30
# 3.menu to show jobs                         --- complete 12.43
# 4.Apply for job                             --- complete 1.16
# 5.post your CV                              --- complete 1.33
# 6.CV To text                                --- complete 2.18
# 7.text Cleaning                             --- complete 3.02
# 8. Getting qualified candidates(database)   --- complete 3.23
# 9. Implementing GUI                         --- incomplete


# imports
import util
import os



def newJob(msg):
    print(msg)
    title = input("1. Enter Job Title:") # Job title wala box
    description = input("2. Enter Job Description:") # description wala box
    requirements = []
    req = '0'
    # yaha se while loop hatake tujhe jitna requirements chaiye woh lele 
    # FOR eg
    # 10th 12th SCIENCE etc etc and save it in requirements ka list
    while(req != 'q'):
        req = input("Enter Requirements and press enter press q to exit : ")
        requirements.append(req)
    requirements.pop() # ignore this
    
    # INSERT THIS STUFF INTO DATABASE 
    c = util.Utility()
    if(c.insertJob(title,description,requirements)):
        print("Successfull!!")
    else:
        print("Beta tumse na ho payega!") 

def applyJob():
    c = util.Utility()
    # 5 lines prints all JOB from database
    result = c.fetchJobs()
    for row in result:
        print("========================")
        print(row[0],".",row[1])
        print("Description: ",row[2])
        print("Requirements: ", row[3])
        print("========================")
    
    # takes application and stores them in database 
    apply = int(input("Bol kidar apply karega? : "))
    name = input("Naam kya hai bhai?: ")
    cvpath = os.getcwd()+'/'+input("cv name? (enter extension too):")
    if(c.applyJobs(name,cvpath,apply)):
        print("Applied Successfully!! ")
    

def authentication():
    u = input("USERNAME DAAL:")
    p = input("password DAAL:")
    c = util.Utility()
    return c.authenticate(u,p)
    
    

if __name__ == '__main__':
    if(authentication()):
        choice = int(input("Select Kar fatfat mere paas time nai \n1.Upload a new Job \n2.Apply For a Job:"))
        if(choice == 1):
            k = newJob("Chal Job daal")
        elif(choice == 2):
            k = applyJob()
        else:
            print("Andha hai kya kuch bhi datla hai?")
        