retail
    .factory('Product', function($resource) {
        return $resource('http://ng.helpservice.xyz:8010/products/:id/');
    })
    .factory('Invoice', function($resource) {
        return $resource('http://ng.helpservice.xyz:8010/invoice/:id/');
    });