from django import template

register = template.Library()


@register.filter(name='price')
def price(val):
    val = str(val)
    result = []
    while(len(val)):
        result.append(val[-3:])
        val = val[0:-3]
    result.reverse()
    return ",".join(result)
