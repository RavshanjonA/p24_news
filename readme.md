## 1.feed yuborish uchun ckeditor qollash
## 2.query.txt yozish 6ta m2m, m20, o2m
## 3.search ni ishlatish:             
```
search = form.cleaned_data["search"]
articles = Article.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
```