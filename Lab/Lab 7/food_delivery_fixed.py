
def parse_order(items_csv):
    if not isinstance(items_csv, str):
        return {}

    order = {}

    if not items_csv.strip():
        return order

    for item in items_csv.split(','):
        try:
            if ':' not in item:
                continue

            name, qty = item.split(':', 1)
            name = name.strip()

            if not name:
                continue

            quantity = int(qty.strip())

            if quantity <= 0:
                continue

            order[name] = quantity

        except (ValueError, TypeError):
            continue

    return order


def delivery_eta(distance_km):
    try:
        distance = float(distance_km)

        if distance < 0:
            return 0

        return int(15 + distance * 4)

    except (ValueError, TypeError):
        return 0


def coupon_discount(code):
    if not isinstance(code, str):
        return 0

    code = code.upper().strip()

    if not code.startswith("SAVE"):
        return 0

    try:
        discount = int(code[4:])

        if discount < 0 or discount > 100:
            return 0

        return discount

    except (ValueError, TypeError):
        return 0


def main():
    print("==== Running parse_order ====")
    user_input = input(
        "Enter items as name:qty CSV (e.g. pizza:2,burger:1): "
    )
    print("Order:", parse_order(user_input))

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    print("ETA in Minutes:", delivery_eta(user_input))

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    print("Discount:", coupon_discount(user_input))


if __name__ == "__main__":
    main()
