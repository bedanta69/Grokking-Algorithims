voted = {}
def check_voter(name):
    if (voted.get(name)!= None):
        print("kick them out")
    else:
        voted[name]= True
        print("Let them vote")
    
