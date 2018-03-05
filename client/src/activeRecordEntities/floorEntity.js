angular
  .module('app')
  .factory('floorEntity', floorEntity);

function floorEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'floorlist/',
    $cache: $cacheFactory('floorlist'),
    $constructor: function floorEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}