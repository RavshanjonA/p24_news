from django.contrib import admin

from apps.article.models import Article, Category, Comment, Advertise, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug', 'is_active', 'owner', 'likes')
    list_filter = ('category', 'is_active', 'owner')
    date_hierarchy = 'published_at'
    prepopulated_fields = {'slug': ('title', 'published_at')}
    search_fields = ('title', 'body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'owner', 'article')
    list_filter = ('owner', 'article')
    date_hierarchy = 'created_at'


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_filter = ('is_active',)
    date_hierarchy = 'expire_date'
    list_display = ('url', 'expire_date', 'phone')
    list_display_links = ('expire_date',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass