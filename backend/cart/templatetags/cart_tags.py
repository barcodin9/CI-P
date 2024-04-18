from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(str(key))