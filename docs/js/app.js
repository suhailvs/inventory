'use strict';

var retail = angular.module("retail", []);

angular
    .module('SampleApplication', [
        'ui.router',
        'retail',
        'ngResource'
    ]).config(['$resourceProvider','$stateProvider', '$urlRouterProvider', function($resourceProvider,$stateProvider, $urlRouterProvider) {

    $resourceProvider.defaults.stripTrailingSlashes = false;

    $stateProvider
        .state({
            name: 'product',
            url: '/',
            templateUrl: '../templates/product.html',
            controller: 'ProductController'
        })
        .state({
            name: 'invoices',
            url: '/invoices',
            templateUrl: '../templates/invoices.html',
            controller: 'InvoicesController'
        })
	.state({
            name: 'invoice',
            url: '/invoice/:id',
            templateUrl: '../templates/invoice.html',
            controller: 'InvoiceController'
        })
        .state({
            name: 'addinvoice',
            url: '/addinvoice',
            templateUrl: '../templates/addinvoice.html',
            controller: 'addInvoiceController'
        });
    $urlRouterProvider.otherwise('/');
}]);
