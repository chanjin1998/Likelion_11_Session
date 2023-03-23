# django 초기 세팅 순서
<br>

## pythion3 -m venv venv
## source venv/bin/activate < = > deactivate
## pip install django
## django-admin startproject [이름]
## cd [이름]
## python3 manage.py startapp [이름(1)]

## settings에 app 추가
## models 데이터베이스 추가
<p>
  admin => 
  [ from .models import *
  admin.site.register(Blog) ]
</p>


## python3 manage.py createsuperuser
<p>
  id : root
  pwd : root
  email : r@r.com
</p>