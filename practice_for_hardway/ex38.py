ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song",
              "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))
print("There we go: ", stuff)
print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())  # list.pop()会将元素添加到list最后
print(' '.join(stuff))  # what? cool! 使用一个字符串将list连接起来“ ”
print('#'.join(stuff[3:5]))  # super stellar! 指 3 ≤ x < 5 的元素
