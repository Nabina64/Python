# Args : arguments
# arguments name is followed by *
# * is used to define args


# def intro(*args):
#     print(args)
    # print(args[0])
    # print(args[1])
    # print(args[2])
    # for i in args:
    #     print(i)
#     print(f"Hello, my name is {args[0]}. I am {args[1]} years old and I live in {args[2]}.")

# a = "Nabina"
# b = 18
# intro(a,b,"Kathmandu")

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum(10,20))
print(sum(10,20,30))
print(sum(10,20,30,40))

