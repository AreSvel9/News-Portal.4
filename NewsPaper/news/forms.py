from django.forms import ModelForm, Select
from .models import Post


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['rating']


from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user