angular
  .module('app')
  .factory('roomEntity', roomEntity);

function roomEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'info/roomlist/',
    $cache: $cacheFactory('roomlist'),
    $constructor: function roomEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}