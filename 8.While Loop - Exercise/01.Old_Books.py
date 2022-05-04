find_book = input()
count = 0

while True:
    enter_book = input()
    if find_book == enter_book:
        print(f"You checked {count} books and found it.")
        break
    elif enter_book == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {count} books.")
        break
    count +=1