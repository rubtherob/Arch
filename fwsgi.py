def application(environ, start_response):
   """
   :paramenviron: словарь данных от сервера
   :paramstart_response: функция для ответа серверу
   """
   # сначала в функцию start_responseпередаем код ответа и заголовки
   start_response('200 OK', [('Content-Type', 'text/html')])
   # возвращаем тело ответа в виде списка из bite
   return[b'HelloworldfromasimpleWSGIapplication!']
