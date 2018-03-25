retail
    .controller('InvoicesController', function($scope,Invoice) {
	$scope.date = new Date();
    Invoice.query().$promise.then(function(data) {
      $scope.invoices = data;
    });
	 	 
})
    .controller('InvoiceController', function($scope,$state,Invoice) {
	id = $state.params['id'];
	Invoice.get({id:id}, function(data) {
    		$scope.invoice = data;
      	});
	$scope.invoiceitems=[{'invoice':1,'product':{'name':'sugar','price':10},'quantity':10}];
    });
