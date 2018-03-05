angular
  .module('app')
  .component('mainComponent', {
    templateUrl: '/src/components/main/mainView.html',
    bindings: { },
    controller: mainComponentController
  })
;

function mainComponentController() {

  var vm = this;
  vm.$onInit = onInit;

  function onInit() {
  }
}
