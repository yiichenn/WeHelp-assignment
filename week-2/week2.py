def calculate(min,max,step):
    sum=0
    for x in range(min,max+1,step):
        sum=sum+x
    print(sum)
calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)

def avg(data):
    total_salary=0
    total_employees=0
    employees_data=data["employees"]
    numbers=len(employees_data) # 4個人
    for i in employees_data:
        if i["manager"]==False:
            total_salary+=i["salary"]
    #print(total_salary)
    for x in employees_data:
        if x["manager"]==False:
            total_employees+=1
    #print(total_employees)
    average=total_salary/total_employees
    print(average)
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
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式



def func(a):
    #return a+(b*c)
    def func2(b,c):
        result= a+(b*c)
        print(result)
        return(result)
    return func2
# result = func(2)(3, 4) #func(a)(b,c)
# print(result)
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

def maxProduct(nums):
    n=len(nums)
    if (n < 2):
        return
    a=nums[0]
    b=nums[1]
    for i in range(0,n):

        for j in range(i+1,n):
            if(nums[i]*nums[j] > a*b):
                a=nums[i]
                b=nums[j]
    ans=a*b
    print(ans)
                #return(ans)
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

def twoSum(nums, target):
    for i in range(len(nums)):
        left = nums[i+1:]
        for j in range(len(left)):
            if (nums[i] + left[j]) == target:
                return [i, j+i+1]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

def maxZeros(nums):
    result=0
    count=0
    for i in range(0,len(nums)):
        if (nums[i]==1):
            count=0
        else:
            count+=1
            result=max(result,count)
    print(result)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
