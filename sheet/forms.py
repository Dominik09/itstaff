from django.forms import ModelForm
from .models import Sheet, Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['com_text']

class AddNewsForm(ModelForm):
    class Meta():
        model = Sheet
        fields = ['title', 'text', 'image']

class EditNewsForm(ModelForm):
	class Meta():
		model = Sheet
		fields = ['title', 'text', 'image']