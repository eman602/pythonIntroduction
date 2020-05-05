import pdb

pdb.set_trace
def factorial(input):
    answer=1
    for i in range(1,input+1):
        answer*=i
    print(answer)

factorial(1000000)
