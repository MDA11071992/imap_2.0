angular.module('app')
  .filter('toTrusted', toTrusted);

  function toTrusted($sce) {
     return function(text) {
            return $sce.trustAsHtml(text);
        };
  }