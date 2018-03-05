angular
  .module('app')
  .factory('buildingEntity', buildingEntity);

function buildingEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'buildinglist/',
    $cache: $cacheFactory('buildinglist'),
    $constructor: function buildingEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}