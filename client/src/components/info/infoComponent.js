angular
  .module('app')
  .component('infoComponent', {
    templateUrl: '/src/components/info/infoView.html',
    bindings: {},
    controller: infoComponentController
  })
;

function infoComponentController(ngDialog) {

  var vm = this;
  vm.$onInit = onInit;
  vm.close = close;

  function onInit() {

  }

  function close() {
    ngDialog.closeAll();
  }

}