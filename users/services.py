import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name):
    '''Создала продукт в stripe.'''

    return stripe.Product.create(name="Pay")


def create_stripe_price(amount):
    '''Создала цену в stripe.'''

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        recurring={"interval": "month"},
        product_data={"name": "Pay"},
    )


def create_stripe_session(price):
    '''Создала сессию на оплату в stripe.'''

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
