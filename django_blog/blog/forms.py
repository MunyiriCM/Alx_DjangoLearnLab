from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment
from .models import Post, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # ✅ include tags

        
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        tag_names = self.cleaned_data.get('tag_names', '')
        tags = [Tag.objects.get_or_create(name=tag.strip())[0] for tag in tag_names.split(',') if tag.strip()]
        post.tags.set(tags)
        return post