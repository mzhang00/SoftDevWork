var changeHeading = function(e) {
  var h = document.getElementById("h");
  //console.log(h.innerHTML);
  h.innerHTML = e;
};

var removeItem = function(e) {
  e.remove();
};

var lis = document.getElementsByTagName("li");
//console.log(lis);

for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover',function (e) {changeHeading(this.innerHTML);});
  lis[i].addEventListener('mouseout',function (e) {changeHeading("Hello World!");});
  lis[i].addEventListener("click",function (e) {removeItem(this);});
}

var addItem = function(e){
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener('mouseover',function (e) {changeHeading(this.innerHTML);});
  item.addEventListener('mouseout',function (e) {changeHeading("Hello World!");});
  item.addEventListener("click",function (e) {removeItem(this);});
  list.appendChild(item);
};

var button = document.getElementById("b");
//console.log(button);
button.addEventListener('click', function(e) {addItem();});

firstfibnum = 1;
fibnum = 1;

var addFib = function(e) {
  //console.log(fibnum);
  var list = document.getElementById("fiblist");
  var item = document.createElement("li");
  if (firstfibnum == 1){
    item.innerHTML = fib(fibnum);
    list.appendChild(item);  
    firstfibnum++;
  }else{
    item.innerHTML = fib(fibnum);
    list.appendChild(item);
    fibnum++;
  }
};

var fib = function(e) {
  if (e < 2) {
    return 1;
  } else {
    return fib(e-1) + fib(e-2);
  }
};

var fb = document.getElementById("fb");
fb.addEventListener('click', function (e) {addFib();});

factnum = 1;

var addFact = function(e) {
  var list = document.getElementById("factlist");
  var item = document.createElement("li");
  item.innerHTML = fact(factnum);
  list.appendChild(item);
  factnum++;
};

var fact = function(e) {
  if (e < 2) {
    return 1;
  } else {
    return fact(e-1) * e;
  }
};

var fctb = document.getElementById("fctb");
fctb.addEventListener('click', function (e) {addFact();});