from django.core.management import BaseCommand

from education.models import Payments


class Command(BaseCommand):
    def handle(self, *args, **options):
        paymants_list = [
            {'lesson': 1, 'payment_sum': 3000, 'payment_method': 'cash'},
            {'course': 2, 'payment_sum': 3000, 'payment_method': 'card'},
            {'course': 2, 'payment_sum': 3000, 'payment_method': 'card'},
            {'lesson': 1, 'payment_sum': 3000, 'payment_method': 'card'},
            {'lesson': 1, 'payment_sum': 3000, 'payment_method': 'cash'}
        ]

        payments_for_create = []
        for payments_item in paymants_list:
            payments_for_create.append(
                Payments(**payments_item)
            )
        print(payments_for_create)
