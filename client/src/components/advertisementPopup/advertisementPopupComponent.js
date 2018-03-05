angular
  .module('app')
  .component('advertisementPopupComponent', {
    templateUrl: '/src/components/advertisementPopup/advertisementPopupView.html',
    bindings: {
      video: '<'
    },
    controller: advertisementPopupController
  })
;

function advertisementPopupController($rootScope) {

  var vm = this;
  vm.$onInit = onInit;
  vm.close = close;


  function onInit() {
  }

  function close() {
    $rootScope.$broadcast('closeAdvertisementListener');
  }



}
