# Multiderivação direta

class Base1:
    pass

class Base2:
    pass


class Multiderivado(Base1, Base2):
    pass

# Multiderivação indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Multiderivado(Base2):
    pass