retail
    .controller('InvoiceController', function($scope, Product) {
	$scope.date = new Date();
	$scope.selectedProducts = [];
        Product.query().$promise.then(function(data) {
            $scope.products = data;
        });
        $scope.addProduct = function() {
	 var newitem = new Object();
	 newitem.id = $scope.Filtered[0].id;
	 newitem.name= $scope.Filtered[0].name;
	 newitem.price = $scope.Filtered[0].price;
	 if ($scope.invoice.qty) {
		 newitem.qty= $scope.invoice.qty;
	 }else{ newitem.qty = 1;}
	 newitem.total = newitem.qty * newitem.price;
	 $scope.selectedProducts.unshift(newitem);
	 
 	 $scope.invoice.qty = "";
	 $scope.invoice.product = "";
	
	 // to find Net value of Purchased products	
	 $scope.sum = function(items, prop){
    	  return items.reduce( function(a, b){
           return a + b[prop];
    	  }, 0);
	 };	 
	 $scope.invoice.net = $scope.sum($scope.selectedProducts, 'total');
	}

	 	 
        $scope.createInvoice = function() {
	 var newinvoice = new Object();
	 newinvoice.customer = "customer";
	 newinvoice.total = "net amount";
	 newinvoice.items = {'1':3,'2':1}; // key = product_id, value = qty
	 // var invoice = new Invoice({
	 //  customer: inv.cust, items: [{p.id,p.qty},..],total,inv.total});
	 // product.$save(function(){
	 //  refresh page
	 // });
	 alert (newinvoice.items['1']);
	}
	 	 
});
