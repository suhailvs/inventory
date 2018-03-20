retail
    .factory('Product', function($resource) {
        return $resource('http://localhost:8000/products/:id/');
    })
    .factory('Invoice', function($resource) {
        return $resource('http://localhost:8000/invoice/:id/');
    });