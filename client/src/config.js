angular
    .module('app')
    .config(function ($httpProvider, $locationProvider, $authProvider, API_ENDPOINT) {
      $locationProvider.html5Mode(true);

      $authProvider.baseUrl = API_ENDPOINT;
      $authProvider.loginUrl = '/api-token-auth/';
    });
