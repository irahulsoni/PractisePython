import calc

# __name__ is the special variable that gives the name of the file if it's main or secondary
# if you print in the main file it will print main but if we print it in imported module,it will print name of the module
print(__name__)
c = calc.add(2, 4)

print(c)


def main():
    print("Hello")
    print("Welcome here")


if __name__ == '__main__':
    main()
