from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["name", "amount"] # 지금은 테스트로 모든 필드를 입력받는다.(테스트에서만 이렇게 해야지 모든 필드를 노출하면 위험함)