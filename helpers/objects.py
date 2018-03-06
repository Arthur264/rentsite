def get_or_None(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

def filter_or_None(classmodel, **kwargs):

    try:
        return classmodel.objects.filter(**kwargs)
    except classmodel.DoesNotExist:
        return None