class Product:

    def __init__(self, name, manufacturer, category, description, retail_price, stock_level, id = None):
        self.name = name
        self.manufacturer = manufacturer
        self.category = category
        self.description = description
        self.retail_price = retail_price
        self.stock_level = stock_level
        self.id = id