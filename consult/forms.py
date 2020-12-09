from django import forms
from admin.models import consult_tbl

class reservationform(forms.ModelForm):
    class Meta:
        model = consult_tbl
        fields = ['cu_text']
        labels = {
            'cu_text': '상담 내용',
        }


class timeform(forms.ModelForm):
    pk = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = consult_tbl
        fields = ['cu_res_time','pk']
        labels = {
            'cu_res_time': '시간 선택',
        }

    def clean(self):
        cleaned_data = super().clean()
        res_time = cleaned_data.get('cu_res_time')
        pk_check = cleaned_data.get('pk')
        print(res_time)
        print(pk_check)
        try:
            a=consult_tbl.objects.get(cu_res_time=res_time,t_no_id=pk_check)
            print(a)
            self.add_error('cu_res_time','이미 예약된 시간입니다.')
        except:
            pass
