# 1 array che ama [1,2,4,6,7,1,3,2,5,6,7,2] ane ama aapde 1st time number aave to double karvano ane number repeate thai to double nai krvano

# arr = [1,2,4,6,7,1,3,2,5,6,7,2]
# check = []
# i=0

# while(i<len(arr)):
#     if arr[i] in check:
#         i=i+1
#         continue
#     else:
#         check.append(arr[i])
#         arr[i] = arr[i]*2
#         i=i+1

# print(arr)
    
    
# Date Genrator 

# from datetime import datetime, timedelta

# # Get the current date
# current_date = datetime.now().date()

# # Generate a list of dates for the next 30 days
# date_list = [current_date + timedelta(days=i) for i in range(30)]

# # Print the list of dates
# for date in date_list:
#     print(date)


a = [1,2,3]
b = [5,6,3]

for i ,j in zip(a,b):
    print(i,j)