# Get Better ~ W3 ~ Osama Yousuf - oy02945

#Q1 https://www.hackerrank.com/challenges/extra-long-factorials/problem
def extraLongFactorials(n):
    a=1
    for i in range(n,0,-1):
        a=a*i
    print(a)
    return a



#Q2 https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
def organizingContainers(container):
    conCap=[sum(x) for x in container]
    numBalls=[sum(x) for x in zip(*container)]
    print(conCap,numBalls)
    if (sorted(conCap) == sorted(numBalls)):
        return 'Possible'
    return 'Impossible'

#Q3 https://www.hackerrank.com/challenges/the-time-in-words/problem
def timeInWords(h, m):
    nums=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    kws=["o 'clock","minute","minutes","quarter","past","half","to"]
    if(m==0):
        return nums[h]+ " o' clock"
    elif (m>=1) and (m <=30):#past
        if m==15:#quarter
            return kws[3] + " " + kws[4] + " " + nums[h]
        elif m==30:#half
            return kws[5] + " " + kws[4] + " " + nums[h]
        elif m==1:
            return nums[m] + " " + kws[1] + " " + kws[4] + " " + nums[h]
        else:
             return nums[m] + " " + kws[2] + " " + kws[4] + " " + nums[h]
    else:#m>30
        if m==45:#quarter to
            return kws[3] + " " + kws[6] + " " + nums[h+1]
        else:
            return nums[60-m] + " " + kws[2] + " " + kws[6] + " " + nums[h+1]
    

