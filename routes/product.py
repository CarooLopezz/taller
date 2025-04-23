from flask import Blueprint
product=Blueprint("product", __name__)

@product.route("/api/products")#traigo todas las rutas
def getAllProducts():
    return ("Get all products!") 
#protocolo de comunicacion put get delete post http