
heading = """
=========================================
         Created by: Aayush Singh
               From:Nepal
-----------------------------------------
   🔢 Enter a Number to Check Whether
     It's Positive, Negative, or Zero
=========================================
"""

print(heading)

num = int(input("Enter number : "))

if num >= 1:
    print("Positive number is :", num)
elif num < 0:
    print("Negative number is :", num)
elif num == 0:
    print("Number is zero")

print("✅ Number you entered:", num)
