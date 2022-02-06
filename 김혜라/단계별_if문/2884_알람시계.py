a, b = map(int, input().split())
time = 60 * a + b - 45
new_hour = time // 60 
if new_hour < 0:
    new_hour = 24 + new_hour
    
new_minute = time % 60 
print(new_hour, new_minute)