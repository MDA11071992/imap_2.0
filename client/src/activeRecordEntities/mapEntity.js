angular
  .module('app')
  .factory('mapEntity', mapEntity);

function mapEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'map/',
    $cache: $cacheFactory('map'),
    $constructor: function mapEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}