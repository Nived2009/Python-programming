Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary{}
#dict{}
a={"name": "thanmai","year":2011,"month":5}
print(a)
{'name': 'thanmai', 'year': 2011, 'month': 5}
type(a)
<class 'dict'>

#dictionary methods
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['thanmai', 2011, 5])
a.items()
dict_items([('name', 'thanmai'), ('year', 2011), ('month', 5)])

#acessing
a[name]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[name]
NameError: name 'name' is not defined
a["name"]
'thanmai'
a["year"]
2011
a.get("name")
'thanmai'
a.get("month")
5

#update()
a
{'name': 'thanmai', 'year': 2011, 'month': 5}
a.update({"date":17})
a
{'name': 'thanmai', 'year': 2011, 'month': 5, 'date': 17}
b={"colour1":"red"}

b.update({"colour2":"yellow","colour":"green"})
          
b        
{'colour1': 'red', 'colour2': 'yellow', 'colour': 'green'}

#Setdefault()
          
a={"hour":3,"min":45}
          
a.setdefault("sec",59)      
59
a       
{'hour': 3, 'min': 45, 'sec': 59}

#pop()         
a.pop("min")        
45
a       
{'hour': 3, 'sec': 59}
a.popitem()       
('sec', 59)

a         
{'hour': 3}

#copy()
          
a={"a":1,"b":2,"c":3}
          
c=a.copy()
          
a          
{'a': 1, 'b': 2, 'c': 3}

c          
{'a': 1, 'b': 2, 'c': 3}

#clear()         
c.clear()
          
c        
{}
 
#len()
          
len(a)           
3

#note: in dictionary duplicates are not allowed      
a={"name": "thanmai","year":2011,"month":5,"name":"nived"}
           
a           
{'name': 'nived', 'year': 2011, 'month': 5}

a={"name": "thanmai","year":2011,"month":5,"name1":"thanmai"}
          
a           
{'name': 'thanmai', 'year': 2011, 'month': 5, 'name1': 'thanmai'}
 
#list in dictionay
           
a={"id":[10,20,30],"names":["raju","ravi","roja"]}
          
print(a)           
{'id': [10, 20, 30], 'names': ['raju', 'ravi', 'roja']}

type(a)           
<class 'dict'>
a.keys()           
dict_keys(['id', 'names'])
a.items()           
dict_items([('id', [10, 20, 30]), ('names', ['raju', 'ravi', 'roja'])])
a.values()           
dict_values([[10, 20, 30], ['raju', 'ravi', 'roja']])
