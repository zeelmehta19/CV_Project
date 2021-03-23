import util
import scoreAlgorithm

def startToShortlist(postedBy):
    candidate = 0
    c = util.Utility()
    result = c.fetchJobWhereId(postedBy)
    if(result):
        jobId = result[0][0]
        requirements = result[0][8].lower().split(',')
        applications = c.fetchAppliedToSort(jobId)
        passing = len(requirements)
        print("Passing Criteria",passing)
        if(applications != False):
            for application in applications:
                textCv = util.pdfToText(application[2])
                scores = scoreAlgorithm.calculateScore(application,textCv[0].lower(),requirements)
                print("score=",scores[4])
                if(scores[4] >= passing):
                    if(c.insertScore(scores)):
                        c.updateStatus(application[6],application[3],"Shortlisted")
                        candidate +=1
                else:
                    if(c.insertScore(scores)):
                        c.updateStatus(application[6],application[3],"Rejected")
                        candidate +=1

    return True



