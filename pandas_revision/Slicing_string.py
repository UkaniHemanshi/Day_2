s = input("Enter the string:")
def slice_string(s):
   print(f"First 5 character: {s[:5]}")
   print(f"Last 5 character: {s[-6:]}")
   print(f"First 5 character: {s[:5]}")
   partition = int(len(s) / 2)
   print("Length of the string: ",len(s))
   if len(s)%2==0:
       print(f"Middle 2 character: {s[partition-1:partition+1]}")
   else:
       print(f"Middle 3 character: {s[partition-1:partition+2]}")

   print(f"Every second charcter: {s[::2]}")

slice_string(s)