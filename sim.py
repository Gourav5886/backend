from typing import Callable , Any

routes : dict[str,Callable[[],Any]] = {}

def route (path : str):
    def register_route(func):
        routes[path] = func
        return func
    return register_route

@route('/shipment')
def get_shipment():
    return 'Shipment<1122, on the way'

request : str = ''

while True:
    request = input(">")

    if request == 'quit':
        break

    if request in routes:
        response = routes[request]()
        print(response)

    else:
        print('404 page not found')
