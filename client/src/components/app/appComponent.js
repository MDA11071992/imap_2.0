angular
    .module('app')
    .component('appComponent', {
      templateUrl: '/src/components/app/appView.html',
      bindings: {
        video: '<'
      },
      controller: appComponentController
    })
;

function appComponentController(ngDialog, $interval, $scope, TIMER) {

  var vm = this;
  vm.$onInit = onInit;
  vm.onFocus = onFocus;
  vm.showAdevertisement = showAdevertisement;
  vm.startTimer = startTimer;
  vm.$onDestroy = onDestroy;

  function onInit() {
    vm.advertisementVideo = vm.video.length > 0 ? vm.video[0].video: {};
    vm.startTimer();

    vm.bodyContainer = angular.element(document.querySelector("body"));
    vm.bodyContainer.addClass('body-overflow');
  }

  function startTimer() {
    var counter = 0;
    vm.stopTimer = $interval(function () {
      if(counter > TIMER) {
        vm.showAdevertisement();
        $interval.cancel(vm.stopTimer);
      }
      counter ++;
    }, 1000);
  }

  function onFocus() {
    ngDialog.close();
    $interval.cancel(vm.stopTimer);
    vm.startTimer();
  }

  function showAdevertisement() {
    ngDialog.open({
      template: '<advertisement-popup-component' +
      ' video="ngDialogData.video">' +
      '</advertisement-popup-component>',
      plain: true,
      showClose: false,
      overlay: false,
      className: 'ngdialog-theme-default__advertisement',
      data: {
        video: vm.advertisementVideo
      }
    });
  }

  var closeAdvertisementListener = $scope.$on('closeAdvertisementListener', onFocus);

  function onDestroy() {
    $scope.$on('$destroy', closeAdvertisementListener);
  }
}
