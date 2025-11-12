def get_ticket_price(age: int) -> float:
    BASE_PRICE = 100.0
    if age < 6:
        price = 0.0
    elif 6 <= age <= 17:
        price = BASE_PRICE * 0.5
    elif 18 <= age <= 59:
        price = BASE_PRICE
    else:  # age >= 60
        price = BASE_PRICE * 0.7
    return price
