angular.module('app')
  .filter('fixedPrice', fixedPrice);

  function fixedPrice() {
    return function (obj, number) {
      return Math.floor(obj * number.toFixed(2));
    };
  }