class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount':amount, 'description':description})

  def withdraw(self, amount, description=''):
    if self.check_funds(amount) == True:
      self.ledger.append({'amount':amount*-1, 'description':description})
      return True
    else:
      return False

  def transfer(self, amount, category):
    if self.check_funds(amount) == True:
      #transfer out of category
      withdrawDescription = "Transfer to " + category.category
      self.ledger.append({'amount':amount*-1, 'description':withdrawDescription})
      #transfer into category
      depositDescription = "Transfer from " + self.category
      category.deposit(amount, depositDescription)
      return True
    else:
      return False  

  def get_balance(self):
    result = ''
    title = self.category.center(30, '*')
    result += title + '\n'
    total = 0
    for row in self.ledger:
      #for key in row:
      description = row['description'][:23]
      result += description
      amount = row['amount']
      total += row['amount']
      amount = format(amount, '.2f')
      offset = 30 - len(description)
      offsetStr = '{:>' + str(offset) + '}'
      amount = offsetStr.format(amount)
      result += amount + '\n'
    result += 'total: ' + format(total)
    return result

  def check_funds(self, amount):
    balance = 0
    for row in self.ledger:
      for key in row:
        balance += row['amount'] 
    if amount < balance:
      return True
    else:
      return False

def create_spend_chart(categories):
  pass