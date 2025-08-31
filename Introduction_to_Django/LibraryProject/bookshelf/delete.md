# Delete Book Instance

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
```

# Expected Output
```text
<QuerySet []>
# or similar output indicating no books remain
```
