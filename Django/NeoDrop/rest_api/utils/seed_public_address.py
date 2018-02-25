from rest_api.models import Nano_Address


def seed(file):
	f = open(file)
	for i in f:
		addr = Nano_Address(address=i[:-1], used=False)
		addr.save()

def clean_db():
	addr = Nano_Address.objects.all()
	for i in addr:
		i.used = False
		i.save(0)



seed("./rest_api/utils/xrb_public.txt")