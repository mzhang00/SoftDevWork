// Emily Zhang and Michael Zhang
// SoftDev pd1
// K04 -- I see a red door
// 2020-02-05

var c = document.getElementById("slate");
var ctx = c.getContext("2d");

var state = "dot";
const SIDE = 50;

c.addEventListener("click", function (e) {
    console.log("clicked");
    var rect = c.getBoundingClientRect();
    if (state == "rect") {
        ctx.fillRect(event.clientX - rect.x, e.clientY - rect.y, SIDE, SIDE);
    } else {
        ctx.fillRect(event.clientX - rect.x, e.clientY - rect.y, 1, 1);
    }
});

document.getElementById("toggle").addEventListener("click", function () {
    console.log("toggling");
    if (state == "rect") {
        state = "dot"
    } else {
        state = "rect"
    }
});


document.getElementById("clear").addEventListener("click", function () {
    console.log("clear");
    ctx.clearRect(0, 0, c.height, c.width);
});


var draw = function() {
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");

    ctx.fillRect(event.clientX, event.clientY, 150, 100);
    console.log("draw");
}