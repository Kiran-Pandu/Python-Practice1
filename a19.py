# Get the number of days book usgage, and calculate the fee
# accordingly. The fees details is listed below:
# • Till five days : Rs.2/day
# • Six to ten days : Rs. 3/day
# • 11 to 15 days : Rs. 4/day
# • After 15 days: Rs 5/day
# Hint:
# Use conditional statements and logical operator
books = int (input("Enter the Number of Days books taken from library : "))
if books<=5:
    books=books*2
    print(books)
elif 6<=books and books<=10:
    books=books*3
    print(books)
elif 11 <= books <= 15:
        books = books * 4
        print(books)
else:
        books = books * 5
        print(books)
        # return books
# elif 11<=books and books <=15:
#     books*4
#     print(books)
# elif books>15:
#     books*5
#     print(books)
# else:
#     print("Please Enter a Positive Number of Days!!")


