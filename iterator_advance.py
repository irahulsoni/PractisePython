class TopTen:
    def __init__(self):
        self.num =1

    # iter and next method are must use when working with iterator, always mention them in the class
    def __iter__(self):
        return self

    # printing first 10 numbers only
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val

        # need to stop the iteration else it will go in infinite loop. To stop iteration:
        else:
            raise StopIteration


vals = TopTen()

# print(next(vals))

for i in vals:
    print(i)
