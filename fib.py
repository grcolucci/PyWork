



def fibcalc(x):
        
        if x <= 0:
                return 0
        
        x += fibcalc(x-1)
        return x


fibTot = fibcalc(15)

print("Total ", fibTot)
        
        