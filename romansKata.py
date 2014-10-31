def toRoman(num):
    numenrom = [('M',  1000),('CM', 900),
                     ('D',  500), ('CD', 400),
                     ('C',  100), ('XC', 90),   
                     ('L',  50),  ('XL', 40),
                     ('X',  10),  ('IX', 9),
                     ('V',  5),   ('IV', 4),
                     ('I',  1)]
    lista = ""
    for x, y in numenrom:
        while num >= y:
            lista += x
            num-= y                 
    return str(lista)
    raise NotImplementedError
