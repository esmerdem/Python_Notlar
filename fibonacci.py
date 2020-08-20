print("*******************"
      "Fibonacci Serisi"
      "*******************")

a = 1
b = 1

fibonacci = [a,b]
girdi = int(input("Bir sayı giriniz"))
for i in range(girdi - 2):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)





























