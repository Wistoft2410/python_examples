# 10.1: Implementing bubble sort 
L = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] 
print(L,"\n")

def bubble_sort():
    print("exercise 10.1")

    def algorithm(L, order='ascending'):
        for i in range(len(L)):
            for j in range(len(L)-1-i):
                if order == 'ascending':
                    if L[j] > L[j+1]:
                        L[j], L[j + 1] = L[j + 1], L[j]
                elif order == 'decending':
                    if L[j] < L[j+1]:
                        L[j], L[j + 1] = L[j + 1], L[j]
        return L

    test_list = L#list(range(len(L)))
    
    print(algorithm(test_list, order='decending'),"\n")

# 10.2: Strings and encoding 
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb." 

def decode():
    return text


# 10.3: Rading files and RegEx 
def eliminate():

    prev = None 
    result = []
    for item in L:
        
        if item != prev: 
            result.append(item)
            prev = item

    return  result 

#print eliminate(my_list)
#my_list = [a,a,a,a,b,c,c,a,a,d,e,e,e,e]

    

# 10.4: Lists and slicing - NO ITERATING! 

# 10.5: Lists and loops 


def main():
	# Here you will need to call some or all of the above functions to test that your code is working. Some functions will generate an output that is used as input in another function.
    bubble_sort()
    

if __name__ == "__main__":
	# Executes only if run as a script
	main()