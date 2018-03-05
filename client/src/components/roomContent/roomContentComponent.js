angular
  .module('app')
  .component('roomContentComponent', {
    templateUrl: '/src/components/roomContent/roomContentView.html',
    bindings: {
      content: '<'
    },
    controller: roomContentComponentController
  })
;

function roomContentComponentController() {

  var vm = this;
  vm.$onInit = onInit;

  function onInit() {

  }

}