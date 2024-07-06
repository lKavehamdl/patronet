class Brand:
    def __init__(self, brand_id, brand_name):
        self.brand_id = brand_id
        self.brand_name = brand_name
        
class BrandCodings:
    def __init__(self, brand_id, coding_len, coding_instruction):
        self.brand_id = brand_id
        self.coding_len = coding_len
        self.coding_instruction = coding_instruction
        
class Permutation:
    def __init__(self, brand_id, product_code):
        self.brand_id = brand_id
        self.product_code = product_code
        
class BrandInstruction:
    def __init__(self, brand_name, coding_instruction):
        self.brand_name = brand_name
        self.coding_instruction = coding_instruction
        
class Product:
    def __init__(self, brand_name, product_code):
        self.brand_name = brand_name
        self.product_code = product_code
        
