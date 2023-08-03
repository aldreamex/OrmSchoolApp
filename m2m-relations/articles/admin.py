from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                is_main = form.cleaned_data['is_main']
                if is_main and count < 1:
                    count += 1
                elif is_main and count >= 1:
                    raise ValidationError('Только один основной раздел!!!')
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
        if count == 0:
            raise ValidationError('Нужен хотя бы один обязательный раздел!!!')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]




