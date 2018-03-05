angular
  .module('app')
  .factory('subTherapyEntity', subTherapyEntity);

function subTherapyEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'info/subtherapylist/',
    $cache: $cacheFactory('subtherapylist'),
    $constructor: function subTherapyEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}