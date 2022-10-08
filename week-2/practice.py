import sys

def main():
    # call func-1
    calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6 
    calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18 
    calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

    # call func-2
    avg({
        "employees":[ 
            {
                "name":"John", 
                "salary":30000, 
                "manager":False
            }, 
            {
                "name":"Bob", 
                "salary":60000, 
                "manager":True
            }, {
                "name":"Jenny", 
                "salary":50000, 
                "manager":False
            }, {
                "name":"Tony", 
                "salary":40000, 
                "manager":False
            }
        ]
    })

    # call func-3
    func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14 
    func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0 
    func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15 

    # call func-4
    maxProduct([5, 20, 2, 6]) # 得到 120
    maxProduct([10, -20, 0, 3]) # 得到 30 
    maxProduct([10, -20, 0, -3]) # 得到 60 
    maxProduct([-1, 2]) # 得到 -2 
    maxProduct([-1, 0, 2]) # 得到 0 
    maxProduct([5,-1, -2, 0]) # 得到 2 
    maxProduct([-5, -2]) # 得到 10

    # call func-5
    result = twoSum([2, 11, 7, 15], 9)
    print(result) # show [0, 2] because nums[0]+nums[2] is 9

    # call func-6
    maxZeros([0, 1, 0, 0]) # 得到 2
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
    maxZeros([1, 1, 1, 1, 1]) # 得到 0 
    maxZeros([0, 0, 0, 1, 1]) # 得到 3

# assignment-1
def calculate(min, max, step):
    cur = min
    result = 0
    while cur <= max:
        result += cur
        cur += step
    print(result)

# assignment-2
def avg(data):
    totalSalary = 0
    num = 0

    for employee in data["employees"]:
        if (employee["manager"] == False):
            totalSalary += employee["salary"]
            num += 1
    
    print(totalSalary / num)

# assignment-3
def func(a):
    def multi(b, c):
        print(f"{a + b * c}")
    return multi

# assignment-4
def maxProduct(nums):
    maxNum = -sys.maxsize - 1
    pivot = 0

    for num1 in nums[:len(nums) - 1]:
        for num2 in nums[pivot + 1:]:
            if (num1 * num2) > maxNum:
                maxNum = num1 * num2
            
        pivot += 1
    
    print(maxNum)

# assignment-5
def twoSum(nums, target):
    R = range(len(nums))

    for pivot1 in R[: len(nums) - 1]:
        for pivot2 in R[pivot1 + 1:]:
            if nums[pivot1] + nums[pivot2] == target:
                return f"[{pivot1}, {pivot2}]"

# assignment-6
def maxZeros(nums):
    result = 0
    temp = 0

    for cur_idx in range(len(nums)):
        if nums[cur_idx] == 0:
            temp += 1

            # if last element
            if cur_idx == len(nums) - 1:
                if temp > result:
                    result = temp
                break

            # check next element
            if nums[cur_idx + 1] != 0:
                if temp > result:
                    result = temp
                temp = 0

    print(result)

main()