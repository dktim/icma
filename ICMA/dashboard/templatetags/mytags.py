# coding: utf-8


from django import template

register = template.Library()


@register.filter(name='int2str')
def int2str(value):
    """
    int 转换为 str
    """
    return str(value)

@register.filter(name='bool2')
def bool2(value):
    if value==0:
        return u'否'
    else:
        return u'是'

@register.filter(name='ellipses')
def ellipses(value):
    return value if len(value) < 20 else value[0:20]+"..."
      
@register.filter(name='res_splict')
def res_split(value):
    """
    将结果格式化换行
    """
    res = []
    if isinstance(value, tuple):
        for v in value:
            if v is not None:
                data = v.replace('\n', '<br>')
                res.append(data)
        return res
    else:
        return value

