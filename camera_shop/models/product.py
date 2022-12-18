class Product:

    def __init__(self, name, category, description, manufacturer, retail_price, stock_level, id = None):
        self.name = name
        self.category = category
        self.description = description
        self.manufacturer = manufacturer
        self.retail_price = retail_price
        self.stock_level = stock_level
        self.id = id