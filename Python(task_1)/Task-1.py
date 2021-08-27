import random
def whoWon():
    ovr=int(input("Enter the number of overs you want to play: "))
    tar=(random.randint(0,(ovr*36))+1)  #+1 because if user scores 5 the target is 6
    print("The target to win is ",tar)  #tar is target for user
    runs=0
    for i in range (ovr*6):             #loop for required balls
        num=int(input())
        c_no=random.randint(0,6)
        print(c_no)                     #c_no is computer number
        runs+=num                       #Total 4 cases
        if c_no==num :                  #when computer number is same as user number     
            print("Computer won by",tar+num-runs-1)
            break
        elif (runs+1)==tar and i==((ovr*6)-1) or  ((runs+1)==tar and c_no==num):     #Match is draw when the scores are level and at last ball user is out 
            print("Match tied.")                                                     #or when scores are level and the user gets out but not at last ball
            break
        elif runs>=tar:
            print("The User won.")
            break
        elif runs<tar and i==((ovr*6)-1):                                            #the total balls are bowled but user is not able to reach target
            print("Computer won by",tar-runs-1)
            break 
if __name__=="__main__":                                                             #function call
    whoWon()              
