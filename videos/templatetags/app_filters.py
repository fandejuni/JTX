from django import template

register = template.Library()

@register.filter(name='duration')
def duration(v):
    return '{:01}'.format(v.duree // 60) + ':' + '{:02}'.format(v.duree % 60)

@register.filter(name='auteurs')
def auteurs(v):
    s = v.relation_auteur_video_set.all()
    if len(s) > 0:
        return ", ".join([x.auteur.name for x in s])
    else:
        return "Inconnu"

@register.filter(name='short')
def short(s):
    n = 25
    if len(s) <= n:
        return s
    else:
        return s[:(n - 3)] + "..."

@register.filter(name='duration_proj')
def duration(p):
    s = 0
    for r in p.relation_proj_set.all():
        s += r.video.duree
    c = '{:02}'.format(s % 60)
    s //= 60
    b = '{:02}'.format(s % 60)
    a = str(s // 60)
    return a + ":" + b + ":" + c
