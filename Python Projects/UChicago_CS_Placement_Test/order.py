from line_item import LineItem

class Order:
  def __init__(self, tax_rate):
      """Class for representing an Order
      
      Parameters:
          tax_rate: the sales tax rate
      """
      self.__tax_rate = tax_rate
      self.__items = []

  def add_line_item(self, item: LineItem) -> None:
      """Add a LineItem to the Order
      
      Parameters:
          item: the item to add
      """
      self.__items.append(item)
      return None

  def total_cost(self) -> float:
      """Calculate the total cost of the order
      
      Returns:
          The total cost of the order in dollars
      """
      sum = 0
      for x in self.__items:
          sum = sum + (x.line_cost()*(1+(self.__tax_rate/100)))
      return sum