source_str = "There is a string accessing example."

print(len(source_str))
print(source_str[34])

print(source_str.find('r'))  #there
print(source_str.rfind('r')) #string

print(source_str.find('ing'))  #string
print(source_str.rfind('ing')) #accessing

print(source_str.find('e',15))  #accessing
print(source_str.rfind('e',15)) #example

print(source_str.find('ing',5))  #string
print(source_str.rfind('ing',5)) #accessing

print(source_str.find('ing',18,28)) #string
print(source_str.rfind('ingg',5))