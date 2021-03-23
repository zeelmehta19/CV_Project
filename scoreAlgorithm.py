
def calculateScore(application,textCv,requirements):
    score = 0
    ssc = 'ssc'
    hsc = 'hsc'
    ten = '10th'
    twel = '12th'
    r = len(requirements)
    for i in range(r):
        
        if(requirements[i] == ssc): 
            requirements.append(ten)
            
        if(requirements[i] == hsc):
            requirements.append(twel)
            
        if(requirements[i] == ten):
            requirements.append(ssc)
            
        if(requirements[i] == twel):
            requirements.append(hsc)
        
    
                

    for req in requirements:
        if(textCv.find(req) != -1):
            score +=1
            
           
    
    # lateral conditions 
    
    if(textCv.find('github')):
        score +=1
    if(textCv.find('java')):
        score +=1
        
    print(application[6],application[1],application[0],application[3],score)
    return (application[6],application[1],application[0],application[3],score)