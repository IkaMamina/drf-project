from django.core.management import BaseCommand

from users.models import Pay, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        params = dict(username='test', email='test@example.com', password='qwerty')
        user, user_status = User.objects.get_or_create(**params)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print('User created successfully.')

        pay_list = [
            {
                'user': user,
                "date_pay": "2022-09-01",
                "payment_course": "2",
                "payment_lesson": "",
                "payment_amount": "5000",
                "payment_method": "cash",
            },
            {
                'user': user,
                "date_pay": "2022-09-03",
                "payment_course": "1",
                "payment_lesson": "",
                "payment_amount": "6000",
                "payment_method": "transfer",
            },
            {
                'user': user,
                "date_pay": "2022-09-05",
                "payment_course": "3",
                "payment_lesson": "",
                "payment_amount": "3000",
                "payment_method": "cash",
            }
        ]

        payment_for_create = []
        for pay_item in pay_list:
            payment_for_create.append(Pay(**pay_item))

        Pay.objects.bulk_create(payment_for_create)
