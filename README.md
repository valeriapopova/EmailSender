# API EMAIL для оповещения о новых лидах


Метод, позвляющий получать оповещения о новых лидах (перенаправленные)


***/email*** доступ к api email

___POST___

_/email/post_ - Отправляет новые лиды(из вк) на указанную почту

*Parameters*


json - данные которые нужно перенаправить должны иметь такой вид

```
{
 "data": [{"name": name}, {"phone": phone}],
 "email" - почта на которую хотите получать уведомления о новых лидах
}
```


Responses 201 сообщение отправлено:

Новый лид!!! имя {name} , номер телефона {phone}

___рекомендуемый пример запроса___

```
def post_email(res, email, host):
    data = {'to': email}
    res.update(data)
    url = f'http://{host}:5001/email/post'
    response = requests.post(url, json=res)
    return response
```