# Merge sort - example from Miller and Ranum 2011, p219
# I have added comments and print statements to assist understanding of this algorithm

def mergeSort(alist):
    print("Splitting", alist)
    if len(alist)>1:
#This part of the algorithm splits the list into LH and RH halves. It is called recursively with smaller and smaller portions. 
#set the midpoint of the list with the floor operator ie rounds down to nearest int.
#Where the list length is an even number the two halves will be the same length
#Where the list length is an odd number the second half will be one item longer than first. 
        mid = len(alist)//2
        print("Length of list is", len(alist),"Midpoint of list is", mid)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        (print("Left half is", lefthalf, "Right half is", righthalf ))
        
#call the function recursively for the two halves
        mergeSort(lefthalf)
        print("Function called for lefthalf", lefthalf)
        mergeSort(righthalf)
        print("Function called for righthalf" ,righthalf)
#set up position indices for left half list (i), right half list (j) and the main list (k) which is going to have items moved into it.         
        i=0
        j=0
        k=0
#start iterating through the two halves to merge the portions back together
#this while loop is for when both halves still have items to be checked
        while i<len(lefthalf) and j<len(righthalf):
#compare the current item (starting from 0) in both lists and move the smaller one into the main list at current position (starting from 0)
#move up the current position index in the list which item was moved from. It doesn't need to be compared again.
#if the compared items are equal then move the one from right hand list. 
            if lefthalf[i]<righthalf[j]:
                alist[k] = lefthalf[i]
                print("At position", k, "item", alist[k], "has been added from left half list.")
                i=i+1
            else:
                alist[k]=righthalf[j]
                print("At position", k, "item", alist[k], "has been added from right half list.")
                j=j+1
            k=k+1
#this while loop should be used if all the items in the right hand list have been compared but not all in the left.        
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            print("At position", k, "item", alist[k], "has been added from left half list. Right half list is finished" )
            i=i+1
            k=k+1

#this while loop should be used if all the items in the left hand list have been compared but not all in the right.        
        while j<len(righthalf):
            alist[k]=righthalf[j]
            print("At position", k, "item", alist[k], "has been added from right half list. Left half list is finished." )
            j=j+1
            k=k+1
      
        print("Merging", alist)

myList = [6,2,65,78,32,54,6,1,90,65,35,8,69,32,44,12,8,36,99,7,13]
print(mergeSort(myList))
        