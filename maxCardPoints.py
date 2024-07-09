def score_cal(cardPoint, k):
    length = len(cardPoint)
    
    total_Point = sum(cardPoint[:k])
    max_points = total_Point
    
    for i in range(1, k+1):
        total_Point += cardPoint[-i] - cardPoint[k - i]
        max_points = max(total_Point, max_points)
        
    return max_points
    
x = list(map(int, input("Enter the card points by giving spaces ").split()))

y = int(input("Enter the total no of cards to be selected "))

print("The max points earned is ", score_cal(x, y))

"""
Enter the card points by giving spaces 1 2 3 4 5 6 1
Enter the total no of cards to be selected 3
The max points earned is  12

=== Code Execution Successful ===
"""
