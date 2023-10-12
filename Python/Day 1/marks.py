h_mark=[90,99,34,56,21,34,78,89,76,56,12,98,34,56,76,12]
# = max(highest_mark)
#print ("The highest mark is: " + str(c))
def h__(h_mark):
 gre=0
 for i in range(len(h_mark)):
    if h_mark[i]>gre:
        gre=h_mark[i]
        
 print("The highest score is: " +str(gre))        
def sum_s(h_mark):
    sum = 0
    for i in range(len(h_mark)):
        sum+=h_mark[i]
    
    return sum
def avg(h_mark):
    sum=sum_s(h_mark)
    avg =sum/len(h_mark)
    print("The avg is: " + str(avg))
    return avg
def per(h_mark):
    sum=sum_s(h_mark)
    per1 = (sum/(len(h_mark)*100))*100
    print("The percaentage is : "+ str(per1))
h__(h_mark)
sum = sum_s(h_mark)
print("The sum is: " + str(sum))
avg(h_mark)
per(h_mark)