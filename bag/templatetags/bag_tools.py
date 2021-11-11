from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subttl(price, quantity):
    return price * quantity
