class Product:

    def __init__(self, name, manufacturer, category, description, cost_price, retail_price, stock_level, id = None):
        self.name = name
        self.manufacturer = manufacturer
        self.category = category
        self.description = description
        self.cost_price = cost_price
        self.retail_price = retail_price
        self.stock_level = stock_level
        self.id = id