retail
    .factory('Product', function($resource) {
        return $resource('http://ng.helpservice.xyz/products/:id/');
    })
    .factory('Invoice', function($resource) {
        return $resource('http://ng.helpservice.xyz/invoice/:id/');
    });