angular
  .module('app')
  .factory('advertisementEntity', advertisementEntity);

function advertisementEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'info/adver/',
    $cache: $cacheFactory('advertisement'),
    $constructor: function advertisementEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}