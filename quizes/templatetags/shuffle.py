# Imports for answering quizes
import random
from django import template

# Change the options orders randomly
register = template.Library()
@register.filter
def shuffle(arg):
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp

@register.filter
def index(sequence, position):
    return sequence[position]