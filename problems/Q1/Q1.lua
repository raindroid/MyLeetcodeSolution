function twoSum(nums, target)
    local numMap = {}
    for i = 1, #nums do
        local k = nums[i]
        if (numMap[target - k] ~= nil) then
            return {numMap[target - k], i}
        else
            numMap[k] = i
        end
    end
end

print(table.concat(twoSum({2, 7, 11, 15}, 9), ' '))