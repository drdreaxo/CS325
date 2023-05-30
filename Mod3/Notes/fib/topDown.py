FibMemo = {0:1, 1:1}
def Fib_top_down(n):    
    if n in FibMemo: #If n is already a key in the FibMemo dictionary, the function simply returns the corresponding value. 
        return FibMemo[n] #& stores the result in the FibMemo dictionary so that it can be reused later if necessary. 
    FibMemo[n] = Fib_top_down(n-1) + Fib_top_down(n-2) #If not, it calculates the n-th Fibonacci number by recursively calling the Fib_top_down function w/ n-1 & n-2 as inputs, 
    return FibMemo[n]
print(Fib_top_down(5))


"""In the Fibonacci implementation you provided, 
each term is calculated only once bc it is stored in the FibMemo dictionary, 
which avoids recalculating the same term multiple times.

So for the Fib_top_down function, 
the recurrence relation is T(n) = T(n-1) + Theta(1), 
bc the function recursively calls itself only once for each term & the lookup in the dictionary is a constant-time operation (Theta(1))."""


def fib_top_down2(n, fibmemo=None):
    if fibmemo is None:
        fibmemo = {0:1, 1:1} #local dictionary 
    if n not in fibmemo:
        fibmemo[n] = fib_top_down2(n-1, fibmemo) + fib_top_down2(n-2, fibmemo)
    return fibmemo[n]



"""This is an implementation of the Fibonacci sequence using a dynamic programming technique called memoization, 
which is a form of the top-down approach.

The code initializes a dictionary called FibMemo w/ two keys, 0 and 1, each with a value of 1. 
Then, it defines a function called Fib_top_down which takes an integer n as input.

If n is already a key in the FibMemo dictionary, the function simply returns the corresponding value. 
If not, it calculates the n-th Fibonacci number by recursively calling the Fib_top_down function w/ n-1 & n-2 as inputs, 
& stores the result in the FibMemo dictionary so that it can be reused later if necessary. 
Finally, the function returns the value of the n-th Fibonacci number.

The last line calls the Fib_top_down function with n=5 as input and prints the result, which should be 8."""