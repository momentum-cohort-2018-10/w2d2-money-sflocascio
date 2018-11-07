class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """
    def __init__(self, name, code, symbol=None, digits=2):
       self.name = name 
       self.code = code
       self.symbol = symbol
       self.digits = digits
       
    # """
    #     Parameters:
    #     - name -- the English name of the currency
    #     - code -- the ISO 4217 three-letter code for the currency
    #     - symbol - optional symbol used to designate currency
    #     - digits -- number of significant digits used
    #     """
      

    def __str__(self):
        return f"{self.code}"

        """
        Should return the currency code, or code with symbol in parentheses.
        """  

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name
                and self.code == other.code and self.symbol == other.symbol
                and self.digits == other.digits)

class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
      
    def __str__(self):
        
        if self.currency.symbol:
            return f"{self.currency.symbol}{self.amount:.2f}"
        else:
            return f"{self.currency.code} {self.amount:.3f}"
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """  
    

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.amount == other.amount
                and self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency != other.currency:
            raise DifferentCurrencyError("Different Currencies")
        else:

            return Money(self.amount + other.amount, self.currency)
            


    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency != other.currency:
            raise DifferentCurrencyError("Different Currencies")
        else:
            return Money(self.amount - other.amount, self.currency)


    def mul(self, multiplier):
        self.multiplier = int(multiplier)
            # """
            # Multiply a money object by a number to get a new money object.
            # """
        return Money(self.amount * self.multiplier, self.currency)

    def div(self, divisor):
        self.divisor = int(divisor)
        """
        Divide a money object by a number to get a new money object.
        """

        return Money(self.amount / self.divisor, self.currency)


    
# #Inside f string {var:.2f}  this will add decimel points
# if slese lcurrenct .digits == 2 
#     {var:.2f}
# else:
#      {var:.3f}  (replace digits with the number 2 to get it working glbally)
#if self.currency.code 