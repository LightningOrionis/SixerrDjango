from django.forms import ModelForm
from .models import Gig


class GigForm(ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'category', 'description', 'photo', 'price', 'status']
        labels = {'title': 'Название',
                  'category': 'Категория',
                  'description': 'Описание',
                  'photo': 'Фото',
                  'price': 'Цена',
                  'status': 'Статус'
        }
