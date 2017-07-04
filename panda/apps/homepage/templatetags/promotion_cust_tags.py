from django.template import Library, Node, RequestContext, Variable
from django.template.loader import select_template

register = Library()


class PromotionNode(Node):
    def __init__(self, promotion):
        self.promotion_var = Variable(promotion)

    def render(self, context):
        promotions = self.promotion_var.resolve(context)
        template = select_template(['homepage/gallery.html'])
        args = {'promotions': promotions, 'products': []}
        for promotion in promotions:
            if hasattr(promotion, 'product'):
                args['products'].append(promotion.product)
            # args.update(**promotion.template_context(request=context['request']))
        # ctx = RequestContext(context['request'], args)
        # return template.render(ctx)
        return template.render(args, context['request'])


def get_promotion_html(parser, token):
    _, promotion = token.split_contents()
    return PromotionNode(promotion)


register.tag('render_promotion', get_promotion_html)
