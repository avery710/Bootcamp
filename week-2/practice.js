// assignment-1
function calculate(min, max, step){
    let cur = min
    let result = 0

    while (cur <= max){
        result += cur
        cur += step
    }

    console.log(result)
}

calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18 
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0

// assignment-2
function avg(data){
    let totalSalary = 0
    let num = 0

    for (let i = 0; i < data.employees.length; i++){
        if (data.employees[i].manager === false){
            totalSalary += data.employees[i].salary
            num += 1
        }
    }

    console.log(totalSalary / num)
}

avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":false },
        {
            "name":"Bob",
            "salary":60000,
            "manager":true },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":false },
        {
            "name":"Tony",
            "salary":40000,
            "manager":false }
    ]
});

// assignment-3
function func(a){
    function multi(b, c){
        console.log(`${a + b * c}`)
    } 
    return multi
}

func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14 
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0 
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15 
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

// assignment-4
function maxProduct(nums){
    let maxNum = 0 - Number.MAX_VALUE
    let pivot = 0

    //console.log(nums.length)

    for (let i = 0; i < nums.length - 1; i++){
        for (let j = i + 1; j < nums.length; j++){
            if (nums[i] * nums[j] > maxNum){
                maxNum = nums[i] * nums[j]
            }
        }
        pivot++
    }

    if (maxNum === 0){
        console.log(0)
    }
    else {
        console.log(maxNum)
    }   
}

maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30 
maxProduct([10, -20, 0, -3]) // 得到 60 
maxProduct([-1, 2]) // 得到 -2 
maxProduct([-1, 0, 2]) // 得到 0 
maxProduct([5,-1, -2, 0]) // 得到 2 
maxProduct([-5, -2]) // 得到 10

// assignment-5
function twoSum(nums, target){
    for (let i = 0; i < nums.length - 1; i++){
        for (let j = i + 1; j < nums.length; j++){
            if (nums[i] + nums[j] === target){
                return `[${i}, ${j}]`
            }
        }
    }
}

let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

// assignment-6
function maxZeros(nums){
    let result = 0
    let temp = 0

    for (let i = 0; i < nums.length; i++){
        if (nums[i] === 0){
            temp++
        }

        if (i === nums.length - 1){
            if (temp > result){
                result = temp
                break
            }
        }

        if (nums[i + 1] != 0){
            if (temp > result){
                result = temp
                temp = 0
            }
        }
    }
    
    console.log(result)
}

maxZeros([0, 1, 0, 0]) // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) // 得到 4 
maxZeros([1, 1, 1, 1, 1]) // 得到 0 
maxZeros([0, 0, 0, 1, 1]) // 得到 3
