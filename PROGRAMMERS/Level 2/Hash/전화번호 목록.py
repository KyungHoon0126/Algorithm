# Hash - 위장

# Hash 이용 X
def solution1(phone_book):
    phone_book = sorted(phone_book)

    for phone, target in zip(phone_book, phone_book[1:]):
        if target.startswith(phone):
            return False
    return True


# Hash 이용 O
def solution2(phone_book):
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True


solution1(["119", "97674223", "1195524421"])
solution2(["119", "97674223", "1195524421"])
