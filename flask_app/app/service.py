from .models import *
from itertools import product

class BrandService:
    def __init__(self, repository):
        self.repository = repository
        
    def get_all_brands(self):
        return self.repository.get_all_brands()
    
    def create_brand(self, brand_name):
        brand = Brand(brand_id=None, brand_name=brand_name)
        print("SERVICE : ")
        print(brand)
        return self.repository.create_brand(brand)
    
    def update_brand(self, givenId, name):
        brand = Brand(brand_id=givenId, brand_name=name)
        return self.repository.update_brand(brand)
    
    def delete_brand(self, givenId):
        return self.repository.delete_brand(givenId)
    
class BrandCodingsService:
    def __init__(self, repository):
        self.repository = repository
        
    def create_coding(self, coding_len, coding_instruction):
        return self.repository.create_brand_codings(coding_len, coding_instruction)  
        
    def get_brands_instruction(self):
        return self.repository.get_brands_instruction()
    
    def update_coding(self, givenId):
        self.repository.delete_brand_codings(givenId)
        self.repository.delete_permutation(givenId)
        self.repository.set_ID(givenId)
        
        
                      
    
class PermutationsService:
    def __init__(self, repository):
        self.repository = repository
        
    def create_permutation(self, my_list):
        permutations = list(product(*my_list))
        for perm in permutations:
            temp = "".join(str(e) for e in perm)
            self.repository.create_permutation(temp)
        
    def search_product(self, code):
        return self.repository.search_product(code)
