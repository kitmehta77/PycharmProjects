import calculation


def lessThan14000(gross_income):
    taxrate = 10.5
    tax = calculation.multiply(gross_income, taxrate/100)
    return tax

def lessThan48000(gross_income):
    taxrate = 17.5
    tax_range = calculation.subtract(gross_income, 14000)
    tax = calculation.multiply(tax_range, taxrate/100)
    tax = tax + lessThan14000(14000)
    return tax

def lessThan70000(gross_income):
    taxrate = 30
    tax_range = calculation.subtract(gross_income, 48000)
    tax = calculation.multiply(tax_range, taxrate / 100)
    tax = tax + lessThan48000(48000)
    """tax = tax + lessThan14000(14000)"""
    return tax

def lessThan180000(gross_income):
    taxrate = 33
    tax_range = calculation.subtract(gross_income, 70000)
    tax = calculation.multiply(tax_range, taxrate / 100)
    tax = tax + lessThan70000(70000)
    """tax = tax + lessThan48000(48000)
    tax = tax + lessThan14000(14000)"""
    return tax

def overThan180000(gross_income):
    taxrate = 39
    tax_range = calculation.subtract(gross_income, 180000)
    tax = calculation.multiply(tax_range, taxrate / 100)
    tax = tax + lessThan180000(180000)
    """tax = tax + lessThan70000(70000)
    tax = tax + lessThan48000(48000)
    tax = tax + lessThan14000(14000)"""
    return tax

def totalTax(gross_income):
    if gross_income >= 180000:
        return overThan180000(gross_income)
    elif gross_income >= 70000: # 70000 - 180000
        return lessThan180000(gross_income)
    elif gross_income >= 48000: # 48000 - 70000
        return lessThan70000(gross_income)
    elif gross_income >= 14000: # 14000 - 48000
        return lessThan48000(gross_income)
    else: # up to 14000
        return lessThan14000(gross_income)

