

N = 700000000 #total number that the bank will pay for interest within one year
Interest = 1 #bank interest
Base = 1 #customer base money


TotalSum = Base * (1 + Interest / N) ** N

print("Total sum:")
print(TotalSum)
