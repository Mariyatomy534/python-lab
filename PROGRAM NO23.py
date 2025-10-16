def even_PerfectSq(start, end):
    if start > end:
        start, end = end, start  # Swap to fix range

    evenSq = []
    for num in range(start, end + 1):
        if all(int(digit) % 2 == 0 for digit in str(num)):
            sqrt = int(num ** 0.5)
            if sqrt * sqrt == num:
                evenSq.append(num)
    return evenSq

start = 1000
end = 9999
result = even_PerfectSq(start, end)
print(result)

                  
         
