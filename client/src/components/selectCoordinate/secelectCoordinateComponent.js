angular
  .module('app')
  .component('selectCoordinateComponent', {
    templateUrl: '/src/components/selectCoordinate/selectCoordinateView.html',
    bindings: {
      coordinate: '<',
      name: '@'
    },
    controller: selectCoordinateComponentController
  });

function selectCoordinateComponentController() {

  var vm = this;
  vm.$onInit = onInit;
  vm.activateAction = activateAction;
  vm.getCoordinate = getCoordinate;
  vm.draw = draw;
  vm.drawPoints = drawPoints;

  function onInit() {
    vm.rectSize = 6;
    vm.canvas = document.querySelector("#container").childNodes[0];
    vm.angCanvas = angular.element(document.querySelector("#container"));
    vm.ctx = vm.canvas.getContext("2d");

    vm.drawPoints();
  }

  function activateAction() {
    vm.angCanvas.unbind('click');
    vm.angCanvas.bind('click', getCoordinate);
  }

  function getCoordinate(event) {
    vm.ctx.clearRect(vm.coordinate.x - vm.rectSize/2, vm.coordinate.y - vm.rectSize/2, vm.rectSize, vm.rectSize);

    var rect = vm.canvas.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;

    vm.coordinate.x = Math.round(x);
    vm.coordinate.y = Math.round(y);

    vm.drawPoints();
  }

  function drawPoints() {
    switch (vm.name) {
      case 'terminal':
        vm.terminal = vm.coordinate;
        vm.draw("#336600");
        break;
      case 'entrance':
        vm.entrance = vm.coordinate;
        vm.draw("#606060");
        break;
      case 'room':
        vm.room = vm.coordinate;
        vm.draw("#FFFF00");
        break;
      case 'building':
        vm.building = vm.coordinate;
        vm.draw("#00FFFF");
        break;
      case 'passageway':
        vm.passageway = vm.coordinate;
        vm.draw("#791fd4");
        break;
    }
  }

  function draw(color) {
    vm.ctx.fillStyle = color;
    vm.ctx.fillRect(vm.coordinate.x - vm.rectSize/2, vm.coordinate.y- vm.rectSize/2, vm.rectSize, vm.rectSize);
  }

}
