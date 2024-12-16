from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            raise ValidationError('Тут всегда ошибка')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]