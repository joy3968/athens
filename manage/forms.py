from django import forms
from admin.models import attendance_tbl
from datetime import datetime

class timeform(forms.ModelForm):

    class Meta:
        model = attendance_tbl
        fields = ['at_date']
        labels = {
            'at_date': '날짜 선택',
        }

