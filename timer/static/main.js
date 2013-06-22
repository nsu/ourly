var myApp = angular.module('myApp', ['ngResource']);
myApp.factory('Data', function () {
  return {'user': 'foobar'};
});

myApp.directive('myCurrentTime', function($timeout, dateFilter) {
    // return the directive link function. (compile function not needed)
    return function(scope, element, attrs) {
      var format,  // date format
          timeoutId; // timeoutId, so that we can cancel the time updates

      // used to update the UI
      function updateTime() {
        d = new Date()
        utcD = new Date( d.getTime() + d.getTimezoneOffset() * 3600 * 1000).toUTCString().replace( / GMT$/, "" )
        scope.data.curTime = utcD.getTime();
      }

      // watch the expression, and update the UI on change.
      scope.$watch(attrs.myCurrentTime, function(value) {
        format = value;
        updateTime();
      });

      // schedule update in one second
      function updateLater() {
        // save the timeoutId for canceling
        timeoutId = $timeout(function() {
          updateTime(); // update DOM
          updateLater(); // schedule another update
        }, 1000);
      }

      // listen on DOM destroy (removal) event, and cancel the next UI update
      // to prevent updating time ofter the DOM element was removed.
      element.bind('$destroy', function() {
        $timeout.cancel(timeoutId);
      });

      updateLater(); // kick off the UI update process.
    };
});


myApp.filter('secstotime', function () {
    return function (difference) {
        difference = Math.floor(difference/1000);
        hours = Math.floor(difference/3600);
        difference = difference - hours*3600;
        minutes = Math.floor(difference/60);
        return hours+" hours "+minutes+" minutes";
    };
});

function defaultCtrl($scope, $resource, $http, Data){
  $scope.data = Data;
  var User = $resource('/api/v1/user/:id/');
  var WorkSession = $resource('/api/v1/worksession/:id/');


  var sessions = WorkSession.get(function(){
    $scope.data.sessions = sessions.objects;
    if ((!sessions.objects[0].stop)) {
        $scope.data.currentSession = sessions.objects[0];
        d = new Date(sessions.objects[0].start);
        $scope.data.currentStart = d.getTime();
    }
  });

  var user = User.get({id:1});
  $scope.data.user = user;

  $scope.timeDiff = function(date1, date2){
    date1 = new Date(date1);
    date2 = new Date(date2);
    difference = date1-date2;
    difference = Math.floor(difference/1000);
    hours = Math.floor(difference/3600);
    difference = difference - hours*3600;
    minutes = Math.floor(difference/60);
    return hours+" hours "+minutes+" minutes";
    // difference = difference/1000;
    // hours = Math.floor(difference/3600);
    // difference = difference - hours*3600;
    // minutes = Math.floor(difference/60);
    // return hours+" hours "+minutes+" minutes";
  };

  $scope.clockOut = function(){
    session = WorkSession.get({id:$scope.data.currentSession.id}, function() {
        session.stop = new Date();
        $http({
            url: "/api/v1/worksession/"+session.id+"/",
            dataType: "json",
            method: "PUT",
            data: session,
            headers: {
                "Content-Type": "application/json; charset=utf-8"
            }
        }).success(function(response){
            $scope.data.currentSession = false;
            var sessions = WorkSession.get(function(){
            $scope.data.sessions = sessions.objects;
            if ((!sessions.objects[0].stop)) {
                $scope.data.currentSession = sessions.objects[0];
                d = new Date(sessions.objects[0].start);
                $scope.data.currentStart = d.getTime();
            }
          });
        });
    });
  }

  $scope.clockIn = function(){
    if ($scope.currentSession) {
        return;
    }
    var newSession = {};
     $http({
            url: "/api/v1/worksession/",
            dataType: "json",
            method: "POST",
            data: newSession,
            headers: {
                "Content-Type": "application/json; charset=utf-8"
            }
    }).success(function(response){
        var sessions = WorkSession.get(function(){
        $scope.data.sessions = sessions.objects;
        if ((!sessions.objects[0].stop)) {
                $scope.data.currentSession = sessions.objects[0];
                d = new Date(sessions.objects[0].start);
                $scope.data.currentStart = d.getTime();
        }
        });
    });
  }

}
