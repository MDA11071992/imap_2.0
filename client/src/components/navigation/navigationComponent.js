angular
  .module('app')
  .component('navigationComponent', {
    templateUrl: '/src/components/navigation/navigationView.html',
    bindings: {
    },
    controller: navigationComponentController
  })
;

function navigationComponentController() {

  var vm = this;
  vm.$onInit = onInit;

  function onInit() {

  }

}