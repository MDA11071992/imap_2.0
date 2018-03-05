angular
  .module('app')
  .component('serviceContentComponent', {
    templateUrl: '/src/components/serviceContent/serviceContentView.html',
    bindings: {
      content: '<'
    },
    controller: serviceContentComponentController
  })
;

function serviceContentComponentController() {

  var vm = this;
  vm.$onInit = onInit;

  function onInit() {

  }
}