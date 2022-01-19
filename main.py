import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

passcards = Passcard.objects.all()

active_passcards = []
for passcard in passcards:
    # print(passcard.owner_name, passcard.passcode, passcard.created_at, passcard.is_active, sep='\n')
    if passcard.is_active:
        active_passcards.append(passcard)

print(f'Всего пропусков: {Passcard.objects.count()}', f'Активных пропусков: {len(active_passcards)}')