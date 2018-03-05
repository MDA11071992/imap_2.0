angular
  .module('app')
  .factory('therapyEntity', therapyEntity);

function therapyEntity($cacheFactory, $q, $injector, ActiveRecord, API_ENDPOINT) {

  var prototype = {
    $urlRoot: API_ENDPOINT + 'info/therapylist/',
    $cache: $cacheFactory('therapylist'),
    $constructor: function therapyEntity(properties) {
      this.$initialize.apply(this, arguments)
    }
  };

  var methods = {
  };

  return ActiveRecord.extend(prototype, methods);
}