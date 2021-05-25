var twoSum = function(nums, target) {
    // 84ms; 39.9MB
    const num_dict = {}
    let result = []
    nums.forEach((k, i) => {
        if (target - k in num_dict) {
            result.push(num_dict[target - k], i)
        } else {
            num_dict[[k]] = i
        }
    })
    return result
};




console.log(twoSum(nums = [2,7,11,15], target = 9))