#### F表达式
`F`表达式是用来优化`ORM`操作数据库的。

* 如果给每个员工增加工资1000元

原始方法是先将所有员工工资数据取出，计算完再保存到数据库。

```python
employees = Employee.objects.all()
    for i in employees:
        i.salary += 1000
        i.save()
```

`F`表达式可以直接执行`SQL`语句，就能完成这个需求。

```python
from django.db.models import F
    Employee.objects.update(salary=F('salary')+1000)
```

* 求出用户名和`email`相同的用户

```python
from django.db.models import F
    authors = Author.objects.filter(name=F('email'))
    for i in authors:
        print('{}/{}'.format(i.name, i.email))
```

#### Q表达式
* 如果想找出图书价格高于30元，评分高于4分的图书，可以在`filter`直接操作

```python
    books = Book.objects.filter(price__gte=30,rating__gte=4)
```
* 注意，以上方法是**并集**操作，可以用传递参数的方法实现，如果是**或**操作，就要用`Q`表达式

```python
from django.db.models import Q
    books = Book.objects.filter(Q(price__gte=30) | Q(rating__gte=4))
```

* 如果要找出价格大于30元，图书名不包含**梦**字的图书

```python
from django.db.models import Q
books = Book.objects.filter(Q(price__gte=30) & ~Q(name__icontains='梦'))
```

