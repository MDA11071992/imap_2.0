angular
  .module('app')
  .component('roomFormComponent', {
    templateUrl: '/src/components/roomForm/roomFormView.html',
    bindings: {
        room: '<'
    },
    controller: roomFormComponentController
  });

function roomFormComponentController($scope) {

  var vm = this;
  vm.$onInit = onInit;
  vm.removeRoom = removeRoom;
  vm.clearErrors = clearErrors;

  function onInit() {
    vm.room.coordinate = vm.room.coordinate || {};
    vm.room.noValid = false;

  }

  function removeRoom() {
    $scope.$emit('removeRoomListener', vm.room);
  }

  function clearErrors() {
     vm.room.noValid = false;
  }

}