
# review it again 

# score=int(input(""))
# store=[]
# for i in range(score):
#     store.append(score)

# largest=max(store)
# store.remove(largest)
# runnerUP=max(store)
# print(runnerUP)



n = int(input("enter"))  # Number of scores
scores = list(map(int, input().split()))  # All scores in one line

unique = list(set(scores))  # Remove duplicates
unique.remove(max(unique))  # Remove the highest
print("value is ",max(unique))  #