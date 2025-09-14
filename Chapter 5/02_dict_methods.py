marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Renuka": 100})
print(marks)

print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error

#pop method
Rohan = marks.pop("Rohan")
print(Rohan)
print(marks)

#popitem
item = marks.popitem()
print(item)
print(marks)