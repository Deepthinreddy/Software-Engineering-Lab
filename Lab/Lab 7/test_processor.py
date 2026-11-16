import pytest
from hypothesis import given, strategies as st

from food_delivery_fixed import (
    parse_order,
    delivery_eta,
    coupon_discount
)

# Test 1: Fuzz testing parse_order
@given(st.text())
def test_parse_order_fuzz(items_csv):
    try:
        parse_order(items_csv)
    except Exception as e:
        pytest.fail(f"parse_order crashed: {e}")


# Test 2: Fuzz testing delivery_eta
@given(st.text())
def test_delivery_eta_fuzz(distance_km):
    try:
        delivery_eta(distance_km)
    except Exception as e:
        pytest.fail(f"delivery_eta crashed: {e}")


# Test 3: Fuzz testing coupon_discount
@given(st.text())
def test_coupon_discount_fuzz(code):
    try:
        coupon_discount(code)
    except Exception as e:
        pytest.fail(f"coupon_discount crashed: {e}")
