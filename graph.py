import util 
import matplotlib 
import matplotlib.pyplot as plt

'''
THIS Module plotGraph takes 1 argument which is userId of the user who wants to see his graph
call this method in main cv.py file with 
import graph as g 
g.plotGraph(userId)

'''

def plotGraph(userId):
    c = util.Utility()
    jobScore = c.getScores(userId)
    cvScore = c.getCVScore(userId)
    score = 0
    i = 0
    scorey = [0]
    for scorex in jobScore:
        scorey.append(scorex[0])

    application = cvScore[2]

    shortlisted = cvScore[3]
    selected = cvScore[4]
    hired = cvScore[5]
    rejected = cvScore[6]


    maxtest = application*3
    ch = []
    simplescore = [0]
    s=0
    while(maxtest > 0):
        if(shortlisted <= application):
            ch.append(shortlisted)
            s = s+shortlisted
            maxtest -=1
            shortlisted -=1
        if(selected <= shortlisted):
            ch.append(selected)
            s = s+selected
            maxtest -=1
            selected -=1
        if(hired <= selected):
            ch.append(hired)
            s = s+hired
            maxtest -=1
            hired -=1
        if(rejected <= shortlisted):
            ch.append(-rejected)
            s = s-rejected
            maxtest -=1
            rejected -=1
        maxtest -=1
        simplescore.append(s)
        s=0
    j = 1
    app = [0]
    for k in range(application):
        app.append(j)
        j +=1
    cy = ch[::-1]
    plt.plot(simplescore,label="personal scores")
    plt.plot(app,scorey,label = "Score given by companies")
    plt.axis([0,application,-2,10])
    plt.xlabel("Applications")
    plt.ylabel("Scores")
    plt.legend()
    path = str(userId)+".png"
    print(path)
    plt.savefig(path)
    return path
