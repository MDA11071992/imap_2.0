angular.module('app')
  .filter('isEmpty', isEmpty);

  function isEmpty() {
    var prop;
    return function (obj, bool) {
      for (prop in obj) {
          if (obj.hasOwnProperty(prop)) {
            return !bool;
          }
      }
      return bool;
    };
  }