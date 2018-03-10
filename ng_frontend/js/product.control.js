retail
    .controller('ProductController', function($scope, Product) {
        Product.query().$promise.then(function(data) {
            $scope.products = data;
        });
        $scope.submitProduct = function(p) {
        	alert(p.name);
		    var product = new Product({
		    	name: p.name,description:p.description,price:p.price});
		    product.$save(function(){
		      $scope.products.unshift(product);
		    })
		}
});
