"""Please write code to memoize the following recursive function
 then upload your Python file to this question:
"""
memo = {}
def doSomething(n):
    if n in memo:
        return memo[n]
    if n<= 1:
        result = n
    else:
        return doSomething(n - 1) + doSomething(n-2)
    memo[n] = result
    return result


if __name__ == '__main__':
    print(doSomething(5))