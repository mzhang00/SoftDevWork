console.log("Yeet");

var fibarray = [0,1,1];

var factorial = function(n) {
  if(n == 0) return 1;
  return n * factorial(n - 1);
};

var fibonacci = function(n) {
  if (n < 3) return 1;
  if (fibarray[n]) return fibarray[n];
  fibarray[n] = fibonacci(n - 1) + fibonacci(n - 2);
  return fibarray[n]
};

var gcd = function(a, b) {
  if(b > a) return gcd(b, a);
  if((a % b) == 0) return b;
  return gcd(b, a % b);
};

var students = ["John", "Bill", "Mandy", "David", "Jennifer", "Alexandria", "Arthur", "Tim", "Justin", "Anthony", "Mark"];
var randomStudent = function() {
  return students[Math.floor(Math.random() * students.length)];
};

var factorialOnClick = function() {
  document.getElementById("factorialAnswer").innerHTML = factorial(document.getElementById("factorialInput").value);
}

var fibonacciOnClick = function() {
  document.getElementById("fibonacciAnswer").innerHTML = fibonacci(document.getElementById("fibonacciInput").value);
}

var gcdOnClick = function() {
  document.getElementById("gcdAnswer").innerHTML = gcd(document.getElementById("gcdInput1").value, document.getElementById("gcdInput2").value);
}

var randomStudentOnClick = function() {
  document.getElementById("randomStudentAnswer").innerHTML = randomStudent();
}

document.getElementById("factorialButton").addEventListener("click", factorialOnClick);
document.getElementById("fibonacciButton").addEventListener("click", fibonacciOnClick);
document.getElementById("gcdButton").addEventListener("click", gcdOnClick);
document.getElementById("randomStudentButton").addEventListener("click", randomStudentOnClick);

console.log("Testing Factorial:");
console.log(factorial(1));
console.log(factorial(23));
console.log(factorial(100));
console.log("Testing Fibonacci:");
console.log(fibonacci(1));
console.log(fibonacci(23));
console.log(fibonacci(100));
console.log("Testing GCD:");
console.log(gcd(20, 5));
console.log(gcd(1263, 343));
console.log(gcd(24, 16));
console.log("Testing Random Students:");
console.log(randomStudent());
console.log(randomStudent());
console.log(randomStudent());
console.log(randomStudent());
console.log(randomStudent());
