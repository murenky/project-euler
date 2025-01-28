// Euler project проблема 1
// Найти сумму натуральных чисел меньше 1000, делящихся на 3 или 5
@main
def main(): Unit =
  {
    var sum1: Int = 0
    var sum2: Int = 0
    var sum3: Int = 0

    for i <- 3 to 999 by 3 do sum1 = sum1 + i
    for j <- 5 to 999 by 5 do sum2 = sum2 + j
    for k <- 15 to 999 by 15 do sum3 = sum3 + k

    println(sum1 + sum2 - sum3)
  }
