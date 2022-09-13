# API EMAIL для оповещения о новых лидах


Метод, позвляющий получать оповещения о новых лидах (перенаправленные)


***/email*** доступ к api email

___POST___

_/email/post_ - Отправляет новые лиды(из вк) на указанную почту

*Parameters*

email - почта на которую хотите получать уведомления о новых лидах

json - данные которые нужно перенаправить должны иметь такой вид

```
{
 "data": [{"name": name}, {"phone": phone}]
}
```


Responses 201 сообщение отправлено:

Новый лид!!! имя {name} , номер телефона {phone}
