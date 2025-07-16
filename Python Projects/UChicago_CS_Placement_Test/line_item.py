class LineItem:
  def __init__(self, name: str, price: float, qty: int):
      """Class for representing a LineItem
      
      Parameters:
          name: the name of the item
          price: unit price in dollars
          qty: quantity of the item
      
      """
      self.__name = name
      self.__unit_price = price
      self.__qty = qty

  def __str__(self) -> str:
      s = f"LineItem({self.__name}, ${self.__unit_price}/unit, {self.__qty} units)"
      return s

  def __repr__(self) -> str:
      return str(self)

  def line_cost(self) -> float:
      """Calculate the cost of the line item
      
      Returns:
          The cost of the line item in dollars
      """
      return self.__unit_price * self.__qty