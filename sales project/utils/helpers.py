# Question 01: Clean Lines Function
def clean_lines(lines):
    # 1. Solution sans list comprehension 
    cleaned_normal = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            cleaned_normal.append(stripped)
    return cleaned_normal


# Question 02: Parse Products Function
def parse_products(lines):
    parsed = []
    for line in lines:
        parts = line.split(',')
        if len(parts) == 3:
            name = parts[0].strip()
            price = float(parts[1].strip())
            quantity = int(parts[2].strip())
            parsed.append((name, price, quantity))
    return parsed