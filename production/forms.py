from django import forms
from .models import ProdUser


class ProdUserAdminForm(forms.ModelForm):
    '''管理サイトで公演ユーザを編集する時のフォーム
    '''
    class Meta:
        model = ProdUser
        fields = ('prod_id', 'user_id', 'is_owner', 'is_editor')

    def clean_user_id(self):
        '''ユーザのバリデーション
        '''
        # user_id を検証しているという事は、追加フォームである
        user_id = self.cleaned_data['user_id']
        
        # prod_id が入力されていなければ、そっちの検証に任せる
        if 'prod_id' not in self.cleaned_data:
            return user_id
        
        # 同じ prod_id, user_id のレコードがあるか検索
        prod_id = self.cleaned_data['prod_id']
        dupe = ProdUser.objects.filter(prod_id=prod_id, user_id=user_id)
        
        # 追加なので、同じ prod_id, user_id のレコードが見つかったら重複
        if len(dupe) > 0:
            raise forms.ValidationError("{} はすでに {} のユーザです。"
                .format(user_id, prod_id))
        return user_id
