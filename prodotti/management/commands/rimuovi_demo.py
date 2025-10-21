from django.core.management.base import BaseCommand
from prodotti.models import Categoria, Prodotto, ImmagineProdotto
from clienti.models import Cliente, Appuntamento
from preventivi.models import Preventivo, VocePreventivo


class Command(BaseCommand):
    help = 'Rimuove i dati di esempio dal database per il negozio cucine'

    def handle(self, *args, **kwargs):
        self.stdout.write('🗑️ Stai per rimuovere i dati dai seguenti modelli: Categoria, Prodotto, ImmagineProdotto, Cliente, Appuntamento, Preventivo, VocePreventivo')
        conferma = input('Confermi? (s/N): ').lower()
        if conferma != 's':
            self.stdout.write('Operazione annullata')
            return

        self.stdout.write('Eliminazione Voci Preventivo...')
        count_voci = VocePreventivo.objects.count()
        VocePreventivo.objects.all().delete()
        self.stdout.write(f'✓ Eliminati {count_voci} record VocePreventivo')

        self.stdout.write('Eliminazione Preventivi...')
        count_preventivi = Preventivo.objects.count()
        Preventivo.objects.all().delete()
        self.stdout.write(f'✓ Eliminati {count_preventivi} record Preventivo')

        self.stdout.write('Eliminazione Appuntamenti...')
        count_appuntamenti = Appuntamento.objects.count()
        Appuntamento.objects.all().delete()
        self.stdout.write(f'✓ Eliminati {count_appuntamenti} record Appuntamento')

        self.stdout.write('Eliminazione Prodotti...')
        count_prodotti = Prodotto.objects.count()
        Prodotto.objects.all().delete()
        self.stdout.write(f'✓ Eliminati {count_prodotti} record Prodotto')

        self.stdout.write('Eliminazione Clienti...')
        count_clienti = Cliente.objects.count()
        Cliente.objects.all().delete()
        self.stdout.write(f'✓ Eliminati {count_clienti} record Cliente')

        self.stdout.write('Eliminazione Immagini Prodotti...')
        count_immagini = ImmagineProdotto.objects.count()
        ImmagineProdotto.objects.all().delete()
        self.stdout.write(f'✓ Eliminati {count_immagini} record ImmagineProdotto')

        self.stdout.write('Eliminazione Categorie...')
        count_categorie = Categoria.objects.count()
        Categoria.objects.all().delete()
        self.stdout.write(f'✓ Eliminati {count_categorie} record Categoria')

        self.stdout.write(self.style.SUCCESS('✅ Rimozione completata!'))
