from django import forms

class ARIMAForm(forms.Form):
    file = forms.FileField(label='上传数据文件')
    steps = forms.IntegerField(label='预测步数', min_value=1)

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.csv'):
            raise forms.ValidationError('仅支持 CSV 格式的文件')
        return file
