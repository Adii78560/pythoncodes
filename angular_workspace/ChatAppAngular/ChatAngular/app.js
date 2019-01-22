var app = angular.module("ChatAngular", ['ui.router'], function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  });

//declare an app.config() function to configure different routes as per user request
app.config(['$stateProvider', '$urlRouterProvider', function($stateProvider,$urlRouterProvider){

    //stateProvider defines different states as per user request
    $stateProvider.state('login',{
        url: '/login',
        templateUrl: 'Templates/login.html',
         controller: 'login'
    })
    .state('register',{
        url: '/register',
        templateUrl: 'Templates/registration.html',
        controller: 'register'
    })
    $urlRouterProvider.otherwise('login');
}]);