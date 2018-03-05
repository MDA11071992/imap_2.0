angular
  .module('app')
  .factory('findPathEntity', findPathEntity);

function findPathEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'findpath/',
    $cache: $cacheFactory('findpath'),
    $constructor: function findPathEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}