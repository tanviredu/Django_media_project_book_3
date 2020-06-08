from django import forms
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    ## adding the Email portion
    ## its not n the user model
    ## you can add more
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    ## we are overriding the save method
    ## because there is new field
    ## if you add any new field
    ## you need to override the method and
    ## then add validation or logic for that field
    def save(self,commit=True):
        ## adding the super sonstructor
        user = super(UserCreationForm,self).save(commit=False) ## hold it dont save yet
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user



## adding user Registration Form













class ArticleForm(forms.ModelForm):
    def __init__(self,*args,**kargs):
        super(ArticleForm,self).__init__(*args,**kargs)
        self.fields['title'].widget.attrs = {'class': 'form-control',}
        self.fields['body'].widget.attrs = {'class': 'form-control',}
        self.fields['pub_date'].widget.attrs = {'class': 'form-control',}
        self.fields['likes'].widget.attrs = {'class': 'form-control',}
        self.fields['thumbnail'].widget.attrs = {'class': 'form-control',}


    class Meta:
        model = Article
        fields = ('title','body','pub_date','likes','thumbnail')
