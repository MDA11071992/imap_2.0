angular
  .module('app')
  .factory('serviceEntity', serviceEntity);

function serviceEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'info/servicelist/',
    $cache: $cacheFactory('servicelist'),
    $constructor: function serviceEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}