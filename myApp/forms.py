from django import forms
from django.contrib.auth.models import User
from .models import RegistrationRequest

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegistrationRequest
        fields = ['full_name', 'prn_number', 'email', 'username', 'password', 'role']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)



from .models import StudentProfile
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'email', 'year', 'department', 'passout_year', 'graduation_type', 'profile_picture']  # Include profile_picture

    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['graduation_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['passout_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['full_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_picture'].widget.attrs.update({'class': 'form-control-file'})  # Add class for file input


from .models import AlumniProfile
class AlumniProfileForm(forms.ModelForm):
    class Meta:
        model = AlumniProfile
        fields = ['full_name', 'current_working', 'company_name', 'position', 'location',
                   'linkedin', 'bio', 'profile_picture']  # Added profile_picture field


from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_type', 'title', 'company_name', 'location', 'qualification',
            'role_responsibility', 'skills', 'description', 'closing_date'
        ]
        post_type = forms.ChoiceField(choices=Post.POST_TYPE_CHOICES)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'role_responsibility': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'closing_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }
        labels = {
            'post_type': 'Post Type (Job or Internship)',
            'title': 'Post Title',
            'company_name': 'Company Name',
            'location': 'Location',
            'qualification': 'Required Qualification',
            'role_responsibility': 'Role and Responsibilities',
            'skills': 'Skills Required',
            'description': 'Additional Description',
            'closing_date': 'Closing Date',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file.size > 10 * 1024 * 1024:  # 10 MB size limit
            raise forms.ValidationError("The file size exceeds the 10MB limit.")
        return file