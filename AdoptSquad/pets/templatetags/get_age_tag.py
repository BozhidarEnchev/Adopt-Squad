from django import template

register = template.Library()


@register.simple_tag
def get_age(pet):
    parts = []

    if pet.years:
        parts.append(f"{pet.years} year{'s' if pet.years > 1 else ''}")
    if pet.years and pet.months:
        parts.append("and")
    if pet.months:
        parts.append(f"{pet.months} month{'s' if pet.months > 1 else ''}")
    parts.append('old')

    return ' '.join(parts)
