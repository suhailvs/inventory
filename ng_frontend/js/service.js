retail
    .factory('Product', function($resource) {
        return $resource('http://localhost:8000/products/:id/');
    });