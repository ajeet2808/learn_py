# closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore

def outer(par):
    loc = par

    def inner():
        return loc
    return inner

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


if __name__ == "__main__":
    var = 1
    fun = outer(var)
    print(fun())

#############################

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))