"""В корзине лежат шары. Если разложить их в кучи по 2, останется один. Если разложить в кучи 
по 3, останется один. Если разложить в кучи по 4, останется один. Если разложить в кучи по 5, 
останется один. Если разложить в кучи по 6, останется один. Если разложить в кучи по 7, не будет 
остатка. Нужно найти минимальное количество шаров, удовлетворяющее условию."""

balls = 0
exit_if = 1 * 10**4
while True:
    balls += 1
    if balls%2==1 and balls%3==1 and balls%4==1 and balls%5==1 and balls%6==1 and balls%7==0:
        print('Найдено нужное число:', balls)
        break
    if balls > exit_if:
        print('Выполнение слишком долгое, выхожу')
        break

