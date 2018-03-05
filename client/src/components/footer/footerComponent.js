angular
  .module('app')
  .component('footerComponent', {
    templateUrl: '/src/components/footer/footerView.html',
    bindings: {},
    controller: footerComponentController
  })
;

function footerComponentController() {

  var vm = this;
  vm.$onInit = onInit;

  function onInit() {

  }

}