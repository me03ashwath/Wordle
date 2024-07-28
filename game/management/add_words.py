from django.core.management.base import BaseCommand
from game.models import Words

class Command(BaseCommand):

    def handle(self):
        words = list(map('apple bread chair dance eagle faith giant heart idiot jelly kayak lemon money night opera place quiet royal smile teach uncle vivid witch zebra alone brave charm drink empty fancy ghost house image joint kites lucky metal never ocean paint queen river sweet treat under visit world xerox yield zesty angel blunt child diner evade fuzzy globe happy inner joker khaki lover music novel olive peach quick rules sound trust unity value waist water xenon young zebra acute burst climb dodge eager fiery glory harsh input joker kneel lower mount nurse other pouch quest royal stake twist unity voice whale yeast zesty'.split()))
        instances = []
        for word in words:
            instances.append(Words(word_length=len(word), word=word))

        Words.objects.bulk_create(instances)