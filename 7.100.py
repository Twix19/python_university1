x = [1.2, 2.5, 3.7, 4.8, 6.1, 5.3, 7.2, 8.4, 9.9, 10.1, 11.3, 12.6, 13.2, 14.7, 15.9]

is_sorted = True
for i in range(len(x)-1):
  if x[i] > x[i+1]:
    is_sorted = False
    print("Рядковый номер первого числа, нарушающего упорядоченность: ", i+1)
    break
if is_sorted:
  print("Последовательность упорядоченная по возрастанию")