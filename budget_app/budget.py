class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = []
        self.balance = 0
        self.withdrawals = 0

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def deposit(self, amount, description = ""):
        self.ledger.append(dict(amount = amount, description = description))
        self.balance += amount

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        else:           
            self.ledger.append(dict(amount = - amount, description = description))
            self.balance -= amount
            self.withdrawals += amount
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        self.balance -= amount
        self.withdrawals += amount
        return True

    def spent(self):
        if (self.withdrawals + self.balance) == 0:
            spent = 0
        else:
            spent = (self.withdrawals  / (self.withdrawals + self.balance)) * 100
        return  spent - (spent % 10)

    def __str__(self):
        output = f"{self.name.center(30, '*')}" + '\n'
        for elem in self.ledger:
            output += f'{elem["description"][0:23]:<23}' + f'{elem["amount"]:>7.2f}\n'
        output += f'Total: {self.balance}'
        return output



def create_spend_chart(categories):
  
    chart = []
    title = 'Percentage spent by category '
    chart.append(title)
    i = 100
    while i >= 0:
        x = 0
        new_line = f"{str(i).rjust(3)}|"
        while x < len(categories):
            if categories[x ].spent() >= i and x == 0:
                new_line += ' ' + 'o'
            elif categories[x ].spent() >= i and x > 0:
                new_line += ' ' * 2 + 'o'
            elif categories[x].spent() != i and x == 0:
                new_line += ' '* 2
            elif categories[x].spent() != i and x > 0:
                new_line += ' '* 3
            x += 1
        chart.append(new_line)
        i -= 10

    dotted = f"{'-' * (len(categories) * 3 + 1)}"
    dotted_line = dotted.rjust(4 + len(dotted))
    chart.append(dotted_line)

    categories_copy = []
    for i in categories:
      categories_copy.append(i.name)

    max_len = len(max(categories_copy, key=len))
    i = 0
    while i < max_len:
        x = 0
        new_line = ' ' * 4
        while x < len(categories_copy):
          try:
            if x == 0:
                new_line += ' ' + str(categories_copy[x][i])
            elif x > 0 :
                new_line += ' ' * 2 + str(categories_copy[x][i])
          except:# index error
            if x == 0:
                new_line += ' ' * 2
            elif x > 0 :
                new_line += ' ' * 3
          x += 1
        chart.append(new_line)
        i += 1
    return '\n'.join(chart)