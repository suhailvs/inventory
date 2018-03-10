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
            name: 'invoice',
            url: '/invoice',
            templateUrl: '../templates/invoice.html',
        });

    $urlRouterProvider.otherwise('/');
}]);