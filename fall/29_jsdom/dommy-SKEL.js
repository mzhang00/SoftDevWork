var changeHeading = function(e) {
  var h = document.getElementByID("h");
  h.innerHTML = e;
}

var removeItem = function(e) {

}

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++){
  list[i].addEventListener('mouseover',changeHeading(i));
  list[i].addEventListener('mouseout',changeHeading("Hello World!"));
  list[i].addEventListener('click',changeHeading(removeItem(i)));
}

var addItem = function(e){
  // var list =
  // var item = document.createElement("li");
  //  = "WORD";
}
