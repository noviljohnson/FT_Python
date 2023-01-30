# uses notations for encapsulation
# symbols

class Trainer:
    salary = 1000

t1 = Trainer()
print(t1.salary)


# protected
class TrainerPro:
    _salary = 1000

class Learner(TrainerPro):
    newPkg = 1700

t1 = TrainerPro()
print(t1._salary)

l1 = Learner()
print(l1._salary)


# private var
class TrainerPri:
    __salary = 1000

class Learner(TrainerPri):
    newPkg = 1700

t1 = TrainerPri()
print(t1._TrainerPri__salary)
# print(t1.__salary) # cause error

l1 = Learner()
print(l1._TrainerPri__salary)
# print(l1.__salary)


# name mangling
# process of changing the private var name with __ to _clss__var
