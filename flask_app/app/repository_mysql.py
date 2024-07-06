import mysql.connector

from itertools import product
from .models import *
from config import Config

brandID = 0

class BrandRepositoryMySQL:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
    
        
    def get_all_brands(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM brand")
        res = cursor.fetchall()
        cursor.close()
        return [Brand(brand_id=temp['brand_id'], brand_name=temp['brand_name']) for temp in res]
               
    def search_product(self, code):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT brand_name, product_code FROM brand B, permutation P WHERE B.brand_id = P.brand_id AND P.product_code LIKE %s", [code])
        res = cursor.fetchall()
        cursor.close()
        return[Product(brand_name=temp['brand_name'], product_code=temp['product_code']) for temp in res]    
    
    def get_brands_instruction(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT brand_name, coding_instruction FROM brand B, brand_codings BC WHERE B.brand_id = BC.brand_id ")
        res= cursor.fetchall()
        cursor.close()
        return [BrandInstruction(brand_name=temp['brand_name'], coding_instruction=temp['coding_instruction']) for temp in res]
        
    def create_brand(self, brand):
        cursor = self.conn.cursor(dictionary=True)
        print("=======")
        print(brand.brand_name)
        cursor.execute("INSERT INTO brand (brand_name) VALUES (%s)", [brand.brand_name])
        self.conn.commit()
        global brandID
        brandID= cursor.lastrowid
        print("INSERTED!")
        cursor.close()
        
    def update_brand(self, brand):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("UPDATE brand SET brand_name = %s WHERE brand_id = %s", (brand.brand_name, brand.brand_id))
        self.conn.commit()
        cursor.close()
        
    def delete_brand(self, brandId):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM brand WHERE brand_id = %s", [brandId])
        self.conn.commit()
        cursor.close()
        self.delete_brand_codings(brandId=brandId)
        
    def delete_brand_codings(self, brandId):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM brand_codings WHERE brand_id = %s", [brandId])
        self.conn.commit()
        cursor.close()
        self.delete_permutation(brandId=brandId)
        
        
    def delete_permutation(self, brandId):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM permutation WHERE brand_id = %s", [brandId])
        self.conn.commit()
        cursor.close()
        
    def create_brand_codings(self, coding_len, coding_istruction):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO brand_codings(brand_id, coding_len, coding_instruction) VALUES(%s, %s, %s)", [brandID, coding_len, coding_istruction])
        self.conn.commit()
        print("INSERTED!")
        cursor.close()
        
    def create_permutation(self, product_code):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO permutation(brand_id, product_code) VALUES(%s, %s)", [brandID, product_code])
        self.conn.commit()
        print("INSERTED")
        cursor.close()
        
    def set_ID(self, givenId):
        global brandID
        brandID = givenId

