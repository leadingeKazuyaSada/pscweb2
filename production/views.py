from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from rehearsal.views.view_func import *
from .models import Production, ProdUser


class ProdList(LoginRequiredMixin, ListView):
    '''Production のリストビュー
    
    ログインユーザの公演のみ表示するため、モデルは ProdUser
    '''
    model = ProdUser
    template_name = 'production/production_list.html'
    
    def get_queryset(self):
        '''リストに表示するレコードをフィルタする
        '''
        # 自分である ProdUser を取得する
        prod_users = ProdUser.objects.filter(user=self.request.user)
        return prod_users


class ProdCreate(LoginRequiredMixin, CreateView):
    '''Production の追加ビュー
    '''
    model = Production
    fields = ('name',)
    success_url = reverse_lazy('production:prod_list')
    
    def form_valid(self, form):
        '''バリデーションを通った時
        '''
        # 保存したレコードを取得する
        new_prod = form.save(commit=True)
        
        # 自分を owner として公演ユーザに追加する
        prod_user = ProdUser(production=new_prod, user=self.request.user,
            is_owner=True)
        prod_user.save()
        
        messages.success(self.request, str(new_prod) + " を作成しました。")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        '''追加に失敗した時
        '''
        messages.warning(self.request, "作成できませんでした。")
        return super().form_invalid(form)


class ProdUpdate(LoginRequiredMixin, UpdateView):
    '''Production の更新ビュー
    '''
    model = Production
    fields = ('name',)
    success_url = reverse_lazy('production:prod_list')
    
    def get(self, request, *args, **kwargs):
        '''表示時のリクエストを受けるハンドラ
        '''
        # アクセス情報から公演ユーザを取得しアクセス権を検査する
        prod_user = accessing_prod_user(self, kwargs['pk'])
        if not prod_user:
            raise PermissionDenied
        # 所有権を持っていなければアクセス拒否
        if not (prod_user.is_owner):
            raise PermissionDenied
        
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        '''保存時のリクエストを受けるハンドラ
        '''
        # アクセス情報から公演ユーザを取得しアクセス権を検査する
        prod_user = accessing_prod_user(self, kwargs['pk'])
        if not prod_user:
            raise PermissionDenied
        # 所有権を持っていなければアクセス拒否
        if not (prod_user.is_owner):
            raise PermissionDenied
        
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        '''バリデーションを通った時
        '''
        messages.success(self.request, str(form.instance) + " を更新しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        '''更新に失敗した時
        '''
        messages.warning(self.request, "更新できませんでした。")
        return super().form_invalid(form)


class ProdDelete(LoginRequiredMixin, DeleteView):
    '''Production の削除ビュー
    '''
    model = Production
    fields = ('name',)
    template_name_suffix = '_delete'
    success_url = reverse_lazy('production:prod_list')
    
    def get(self, request, *args, **kwargs):
        '''表示時のリクエストを受けるハンドラ
        '''
        # アクセス情報から公演ユーザを取得しアクセス権を検査する
        prod_user = accessing_prod_user(self, kwargs['pk'])
        if not prod_user:
            raise PermissionDenied
        # 所有権を持っていなければアクセス拒否
        if not (prod_user.is_owner):
            raise PermissionDenied
        
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        '''保存時のリクエストを受けるハンドラ
        '''
        # アクセス情報から公演ユーザを取得しアクセス権を検査する
        prod_user = accessing_prod_user(self, kwargs['pk'])
        if not prod_user:
            raise PermissionDenied
        # 所有権を持っていなければアクセス拒否
        if not (prod_user.is_owner):
            raise PermissionDenied
        
        return super().post(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        '''削除した時のメッセージ
        '''
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, str(self.object) + " を削除しました。")
        return result
