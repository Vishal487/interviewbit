# https://www.pepcoding.com/resources/online-java-foundation/recursion-on-the-way-up/print-stair-paths-official/ojquestion
    

def printPathUtil(n, psf):
    if n < 0:
        return
    if n == 0:
        print(psf)
        return

    printPathUtil(n-1, psf+'-'+str(1))
    printPathUtil(n-2, psf+'-'+str(2))
    printPathUtil(n-3, psf+'-'+str(3))

def printPath(n):
    printPathUtil(n, str(n))


# driver
n = 3
printPath(n)
