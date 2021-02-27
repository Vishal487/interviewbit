def mice(mouse, holes):
    mouse.sort()
    holes.sort()

    ans = 0
    for i in range(len(mouse)):
        ans = max(ans, abs(mouse[i]-holes[i]))

    return ans

mouse = [4,-4,2]
holes = [4,0,5]
print(mice(mouse, holes))







"""
-4 0 => 4
2  4 => 2
4  5 => 1
"""