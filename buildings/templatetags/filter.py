from django import template

register = template.Library()

@register.filter(name='price')
def price(val):
    val = str(val)
    result = [];
    while(len(val)):
        result.append(val[0:3])
        val = val[:3]

    print (result)
    return result

