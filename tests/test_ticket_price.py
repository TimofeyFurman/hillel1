from revision.hw_functions_utils import get_ticket_price

def test_free_ticket():
    assert get_ticket_price(5) == 0.0

def test_half_price():
    assert get_ticket_price(10) == 50.0

def test_full_price():
    assert get_ticket_price(30) == 100.0

def test_senior_discount():
    assert get_ticket_price(60) == 70.0
