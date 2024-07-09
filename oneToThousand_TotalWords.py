def no_to_word(n):
    if n == 0:
        return ""
        
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n < 20:
        return units[n]
    elif n < 100:
        return tens[n // 10] + units[n % 10]
    elif n < 1000:
        return units[n //100] + "hundred" + ('and' + no_to_word(n % 100) if n % 100 != 0 else "")
    elif n == 1000:
        return "onethousand"
    else:
        return ""
        
def count_l(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        total_letters += len(no_to_word(i))
    return total_letters
    
    
upper_limit = int(input("Enter the upper limit: "))
print("The total no of letters form 1 to ", upper_limit, "is ", count_l(upper_limit))

"""
Enter the upper limit: 1000
The total no of letters form 1 to  1000 is  21124

=== Code Execution Successful ===
"""
