AIM = 100000
startSize = AIM # стартовый размер массива натуральных чисел
addSize = AIM # размер дополнительного массива натуральных чисел<br/>
nums = [None] * startSize
primeNums = [None] * AIM
foundPrimes = 0
for i in range(startSize):
    nums[i] = True
addition = False
adder = 0
while True:
    if (addition):
        nums.resize(nums.size() + addSize, true)
# исключим составные числа простыми из предыдущих итераций
        for i in range(foundPrimes):
            cur_num = primeNums[i]
            if ((addSize + ((nums.size() - addSize) % cur_num)) < cur_num):
                continue
            for i in range(((nums.size() - addSize) / cur_num) * cur_num, len(nums), cur_num):
                nums[j] = False
    else:
        addition = True
    iter = 0
    if (foundPrimes == 0):
        iter = 2
    else:
        iter = primeNums[foundPrimes - 1] + 2
    for i in range(iter, len(nums)):
    # выбираем очередное простое число
        if (nums[iter]):
            primeNums[foundPrimes] = iter
            foundPrimes += 1
            if (foundPrimes == AIM):
                break
            # просеиваем
            for i in range(iter+iter, len(nums), iter):
                nums[i] = False
        else:
            continue

    if (foundPrimes == AIM):
        break