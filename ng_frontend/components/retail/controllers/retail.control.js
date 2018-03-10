retail
    .controller('RetailController', function($scope, Product) {
        Product.query().$promise.then(function(data) {
            $scope.products = data;
        });
});
