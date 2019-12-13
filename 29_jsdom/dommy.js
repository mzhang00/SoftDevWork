var changeHeading = function(e) {
  var h = document.getElementById("h");
  //console.log(h.innerHTML);
  h.innerHTML = e;
};

var removeItem = function(e) {

};

var lis = document.getElementsByTagName("li");
//console.log(lis);

for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover',function (e) {changeHeading(this.innerHTML);});
  lis[i].addEventListener('mouseout',function (e) {changeHeading("Hello World!");});
  //lis[i].addEventListener("click",changeHeading("asd", count));
  lis[i].addEventListener("click",function (e) {console.log(e); console.log("hello")});
}

var addItem = function(e){
  var list = document.getElementsByTagName("li");
  var item = document.createElement("li");
  item.appendChild(document.createTextNode("WORD"));
  //NEED TO FIX THIS BELOW
  //list[list.length - 1].appendChild(item);
  //list.appendChild(item);
};

var button = document.getElementById("b");
//console.log(button);
button.addEventListener('click', function(e) {addItem("WORD"); console.log(lis);});

var addFib = function(e) {
  console.log(e);
};

var addFib2 = function(e) {
  console.log(e);
};

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);
