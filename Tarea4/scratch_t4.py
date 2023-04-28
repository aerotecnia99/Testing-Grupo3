
# value = 5  
# limit = 7
# value = (value + limit + 1) % limit
# print(value)


# value = 5  
# value2 = (value + limit + 1) 
# print(value2)


bytes_0 = b"\xe9\x18"
print(int.from_bytes(bytes_0, "big"))


print(int.from_bytes(b"\xe9\xdf~\x18", "big"))