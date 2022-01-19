import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

    # passcards = Passcard.objects.all()

    active_passcards = Passcard.objects.filter(is_active=True)

    print(f'Активных пропусков: {len(active_passcards)}')