var changeHeading = function(e, a) {
  var h = document.getElementById("h");
  if (a == 0){
    h.innerHTML = e;
  }else{
    h.innerHTML = "hello";
  }

}

var changeHeading2 = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = "hello";
}

var removeItem = function(e) {

}

var lis = document.getElementsByTagName("li");
console.log(lis);

for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover',changeHeading("<b>hello</b>"));
  lis[i].addEventListener('mouseout',changeHeading("<b>hello</b>"));
  lis[i].addEventListener('click',changeHeading("Hello World!", 0));
  lis[i].addEventListener('click',function (e) {console.log(e);});
}

var addItem = function(e){
  // var list =
  // var item = document.createElement("li");
  //  = "WORD";
  //list.???(item);
}

//var button = document.getElementByID("b");
//button.addEeventListener('click', addItem);

var addFib = function(e) {
  console.log(e);
}

var addFib2 = function(e) {
  console.log(e);
}

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);
