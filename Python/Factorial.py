
import time 

def Factorial (n):

    if (n < 2):
        return n
    return Factorial(n - 2) + Factorial (n-1)

if __name__ == "__main__":
    start_time = time.time()
    result = Factorial(50)
    sub = time.time() - start_time
    print (result)
    print (time.time() - start_time)