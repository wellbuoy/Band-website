from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):

    # password input field
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # password confirmation input field
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:

        # bind to User model
        model = User

        # specify fields to include in form
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):

        # get password from form data
        password1 = self.cleaned_data.get('password')

        # get password confirmation from form data
        password2 = self.cleaned_data.get('password2')

        # validate passwords match
        if password1 and password2 and password1 != password2:

            # raise error if they don't match
            raise forms.ValidationError('Passwords do not match')
        
        # return cleaned password2 data
        return password2

    def save(self, commit=True):

        # create user object from form data
        user = super().save(commit=False)

        # set password using encrypted hash
        user.set_password(self.cleaned_data['password'])
        if commit:

            # save user object to database
            user.save()

        # return saved user object
        return user