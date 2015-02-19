django_tinycms
==============
tinycms is a simple CMS application for Django.
Created for Django engineers with following concepts.
* Easy to use
* Easy to understand
* Easy to customize


## Requirement
* django
* django-mptt

## Install

###1.Install tinycms
```bash
  pip install tinycms
```
###2.Add mptt and tinycms to INSTALLED_APPS in settings.py
```python
INSTALLED_APPS = (
    ....
    'mptt',
    'tinycms',
)
```
###3. Add TEMPLATE_CONTEXT_PROCESSORS to settings.py
```python
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    "django.core.context_processors.tz",
)
```
###4. Add url(r'', include('tinycms.urls')) to urls.py
```python
urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('tinycms.urls')),
)
```

## Licence

GNU LGPL 3.0

## Author

[ccat](https://github.com/ccat)








## 概要
Django用のSimpleなCMSアプリケーションです。
Djangoを利用してシステムを構築するエンジニア向けに、以下の3つをコンセプトで作成しました。
* 簡単に使える
* 簡単に理解できる
* 簡単に拡張できる

DjangoでパーツとしてCMSを利用したい時や、CMSの勉強に利用できます。

## 機能一覧
* i18nに対応した多言語の表示


## 要件
以下のパッケージに依存します。

* django
* django-mptt


## インストール方法
###1. 以下のコマンドでtinycmsをインストールする
```bash
pip install tinycms
```
###2. settings.pyのINSTALLED_APPSにmpttとtinycmsを追加
```python
INSTALLED_APPS = (
    ....
    'mptt',
    'tinycms',
)
```
###3. settings.pyにTEMPLATE_CONTEXT_PROCESSORSを追加
```python
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    "django.core.context_processors.tz",
)
```
###4. urls.pyにurl(r'', include('tinycms.urls'))を追加
```python
urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('tinycms.urls')),
)
```

## ライセンス

GNU LGPL 3.0

## 作成者

[ccat](https://github.com/ccat)


