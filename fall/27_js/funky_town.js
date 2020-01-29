// Ivan Galakhov and Michael Zhang (Team AlGoreithm)
// SoftDev1 pd1
// K#27 -- Sequential Progression
// 2019-12-10

fact = (n) => (n == 0 ? 1 : fact(n-1)*n);
fibonacci = (n) => (n == 0 || n == 1 ? 1 : fibonacci(n-1)+fibonacci(n-2));
gcd = (a, b) => (b == 0 ? a : gcd(b, a%b));
randomStudent = (l) => l[Math.floor(Math.random()*l.length)];
