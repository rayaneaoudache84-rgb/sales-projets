# Question 04: Create Products from File
import sys
import os

# Ajouter le chemin du dossier parent pour importer le module utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(file), '..')))

from utils.helpers import clean_lines, parse_products
from utils.product import Product

def main():
    file_path = '../data/raw/data.txt'
    if not os.path.exists(file_path):
        file_path = 'data/raw/data.txt'

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Nettoyer les lignes et analyser les produits
    cleaned = clean_lines(lines)
    parsed_data = parse_products(cleaned)

    total_sales = 0.0
    for name, price, qty in parsed_data:
        p = Product(name, price, qty)
        val = p.total_value()
        total_sales += val
        print(f"{p.name}: {val}")

    print(f"Total Sales: {total_sales}")

if name == 'main':
    main()