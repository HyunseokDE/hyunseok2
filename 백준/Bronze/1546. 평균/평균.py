n = int(input()) 
scores = list(map(int, input().split())) 

max = max(scores)
new_scores = [(s / max) * 100 for s in scores]  

average = sum(new_scores) / n  
print(average)
