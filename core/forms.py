from django import forms
from core.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'text']
    
    def save(self, commit=True):
        self.instance.author = self.initial['author']
        self.instance.save()
        return super().save()