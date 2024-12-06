from django import template

from product.models import BucketProduct, Rating

register = template.Library()


@register.simple_tag(takes_context=True)
def get_buck_prod_count(context):
    request = context['request']
    user_id = request.user.id

    count = BucketProduct.objects.filter(bucket__user_id=user_id).count()
    return count if count else 0


@register.simple_tag(takes_context=True)
def get_prod_rating(context, product_id):
    request = context['request']
    user_id = request.user.id
    rating = Rating.objects.filter(user_id=user_id, product_id=product_id).first()

    return int(rating.stars) if rating else 0
