def extract_route(req):
    route = req.split('\n')[0]
    route = route.split(' ')[1][1:]
    return route

def read_file(path):
    file = open(path, mode = 'rb')
    return file.read()