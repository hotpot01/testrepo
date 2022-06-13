def application(environ, start_respons):
    start_respons('206 OK', [('Content-Type', 'text/html')])
    body='<h1>Hello, %s !</h1>'%((environ['PATH_INFO'].encode('iso-8859-1').decode('utf-8'))[1:] or 'web')
    return [body.encode('iso-8859-1')]