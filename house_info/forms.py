from django import forms


class ARIMAForm(forms.Form):
    file = forms.FileField(label='上传文件')
    steps = forms.IntegerField(label='预测步数', min_value=1)

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.csv'):
            raise forms.ValidationError('仅支持 CSV 格式的文件')
        # 如果文件大于5MB
        if file.size > 5 * 1024 * 1024:
            raise forms.ValidationError('文件大小不能超过5MB')
        return file
