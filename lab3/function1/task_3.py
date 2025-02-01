def solve(numheads, numlegs):
    chickens = (4 * numheads - numlegs) // 2
    rabbits = numheads - chickens
    print("rabbits:", rabbits)
    print("chickens:", chickens)

solve(35, 94)
