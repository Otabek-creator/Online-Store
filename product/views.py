from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import FormView, CreateView, UpdateView
from rest_framework.generics import ListCreateAPIView

from product.models import Product, BucketProduct, Bucket, Rating, Category, Contact
from product.forms import ContactForm, CreateProductForm
from .serializers import CategorySerializer, ProductSerializer, ContactSerializer, BucketSerializer, \
    BucketProductSerializer, RatingSerializer


# def product_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'product_list.html', context)
#
#
# def product_detail(request, product_id):
#     product = Product.objects.get(id=product_id)
#     related_products = Product.objects.filter(category=product.category).exclude(id=product_id)
#     context = {'product': product, 'related_products': related_products}
#
#     return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['related_products'] = Product.objects.filter(category=product.category).exclude(id=product.id)
        return context


class AboutView(FormView):
    template_name = 'about.html'
    form_class = ContactForm
    success_url = '/about/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ma'lumotlaringiz muvaffaqiyatli saqlandi!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Iltimos, barcha xatoliklarni tuzating!")
        return super().form_invalid(form)


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'product_create.html'
    success_url = '/create/'
    success_message = 'Tovar joylandi!'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    # def get_context_data(self, **kwargs):
    #     contex = super().get_context_data(**kwargs)
    #     return contex

    def get_queryset(self):
        return Product.objects.all().order_by('-id')


class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'discount_percent', 'is_active', 'count', 'image', 'category',
              'created_by']
    template_name = 'product_update.html'
    # success_url = '/update/'
    success_message = 'Tovar yangilandi!'

    def get_success_url(self):
        return reverse("product_update", kwargs={'pk': self.object.id})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = reverse_lazy('product_list')

    # def get(self, request, *args, **kwargs):
    #     return self.delete(self.get_object())


class BucketProductListView(LoginRequiredMixin, ListView):
    model = BucketProduct
    template_name = 'bucket.html'
    context_object_name = 'bucket_products'


class BucketProductCreateView(LoginRequiredMixin, View):
    pk_url_kwarg = 'product_id'

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get(self.pk_url_kwarg)
        bucket = Bucket.objects.filter(user=request.user).first()
        if not bucket:
            bucket = Bucket.objects.create(user=request.user)

        bucket_product = BucketProduct.objects.filter(bucket_id=bucket.id, product_id=product_id).first()
        if not bucket_product:
            BucketProduct.objects.create(bucket_id=bucket.id, product_id=product_id)

        return HttpResponseRedirect(reverse_lazy('product_list'))


class BucketProductDeleteView(LoginRequiredMixin, DeleteView):
    model = BucketProduct
    pk_url_kwarg = 'product_id'

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get(self.pk_url_kwarg)

        bucket_product = BucketProduct.objects.filter(bucket__user_id=request.user.id, product_id=product_id).first()
        if bucket_product:
            bucket_product.delete()

        return HttpResponseRedirect(reverse_lazy('bucket'))


class RatingCreateView(LoginRequiredMixin, View):
    model = Rating
    pk_url_kwarg = 'product_id'

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get(self.pk_url_kwarg)
        score = int(request.POST.get('score', 1))

        rating = Rating.objects.filter(
            user_id=request.user.id,
            product_id=product_id
        ).first()

        if not rating:
            rating = Rating.objects.create(
                user_id=request.user.id,
                product_id=product_id,
                stars=score
            )

        rating.stars = score
        rating.save()

        return HttpResponseRedirect(reverse_lazy('product_detail', kwargs={'pk': product_id}))


class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ContactListCreate(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class BucketListCreate(ListCreateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer


class BucketProductListCreate(ListCreateAPIView):
    queryset = BucketProduct.objects.all()
    serializer_class = BucketProductSerializer


class RatingListCreate(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
