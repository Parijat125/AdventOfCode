
    
def puzzle1(A_list):
    count = 0
    for i in range(len(A_list)-1):
        if(A_list[i] < A_list[i+1]):
            count += 1
    
    return count
    
"""follwing is brute force"""
def puzzle2(A_list):
    new_list = []
    temp = []
    for i in range (0, len(A_list)-2):
        addition = A_list[i] + A_list[i+1] + A_list[i+2]
        new_list.append(addition)
    
    temp = puzzle1(new_list)
    return(temp)


def main():
    new_list = [] 
    count = 0
    temp = []
    return_puzzle1 = 0
    return_puzzle2 = 0
    with open ("day1.txt", 'r') as file:
        temp = [int(i) for i in file.read().splitlines()] 
        

    print(f" sonar sweep : {puzzle1(temp)} " )
    print(f" three pointer sliding window : {puzzle2(temp)}" )

main()