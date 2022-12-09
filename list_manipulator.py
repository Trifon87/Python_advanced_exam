from collections import deque


def list_manipulator(list, start, finish, *args):

    if start == "add" and finish == "end":
        if len(args) == 1:
            number = args[0]
            list.append(number)
        if len(args) > 1:
            number = (args[0:])
            for x in number:
                list.append(int(x))
        return list
    if start == "add" and finish == "beginning":
        if len(args) == 1:
            number = args[0]
            list.insert(0,number)
        if len(args) > 1:
            number = (args[0:][::-1])
            for x in number:
                list.insert(0, int(x))
        return list
    if start == "remove" and finish == "end":
        if not args:
            list.pop()
            return list
        else:
            for i in range(args[0]):
                list.pop()
            return list

    if start == "remove" and finish == "beginning":
        new = deque(list)
        if not args:
            new.popleft()
            return [x for x in new]
        else:
            for i in range(args[0]):

                new.popleft()
            return [x for x in new]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
