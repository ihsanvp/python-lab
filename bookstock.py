book = {
	"DBMS": 10,
	"OS": 20,
	"COA": 30,
	"MATHS": 10,
	"PE": 10
}

print(book)
print("")
print("1.Recieve Book")
print("2.Sell Book")

choice = int(input("Select choice [1/2] : "))
name = input("Enter book name : ")
stock = int(input("Enter no of books : "))


if choice in [1, 2] :
	if name in book :
		if choice == 1 :
			book[name] += stock
		else :
			book[name] -= stock
	elif choice == 1 :
		book[name] = stock
	
	if name not in book :
		print("Book not found")
	else :
		print("")
		print(book)
else :
	print("Invalid choice")
