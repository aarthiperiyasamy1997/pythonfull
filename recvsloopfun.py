#time complexity

mobprice=[78000,6000,70000,54000,6700]
def iterate(index=0):
    if index==len(mobprice):return
    else:
        print("hello",mobprice[index])
        index+=1
        iterate(index)
iterate()


#using loop
'''for temp in range(2,len(mobprice)-1):
    print("hai",mobprice[temp])'''                     