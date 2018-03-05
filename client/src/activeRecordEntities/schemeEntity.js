angular
  .module('app')
  .factory('schemeEntity', schemeEntity);

function schemeEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'schemelist/',
    $cache: $cacheFactory('schemelist'),
    $constructor: function schemeEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}