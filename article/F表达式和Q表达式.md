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

