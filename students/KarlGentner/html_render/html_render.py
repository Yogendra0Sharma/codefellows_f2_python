#!/usr/bin/python


class Element(object):
    tag = u""
    indent = u""

    def __init__(self, content=None):
        if content is not None:
            self.content = [content]
        else:
            self.content = []

    def render(self, file_out, ind=u"    "):

        file_out.write(self.indent + u'<%s>\n' % self.tag)
        for item in self.content:
            try:
                # if its a Element obj, call its render method
                item.render(file_out, self.indent + ind)
            # if not, just write it
            except AttributeError:
                file_out.write(self.indent+ind+item + u'\n')
        file_out.write(self.indent + u'</%s>\n' % self.tag)

    def append(self, a_string):
            self.content.append(a_string)


class Html(Element):
        tag = u"html"


class Body(Element):
        tag = u"body"


class P(Element):
        tag = u"p"
        indent = u"    "


class Head(Element):
    tag = u"head"


class Title(Element):
    tag = u"title"
    indent = u"    "