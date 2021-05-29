function lengthOfLongestSubstring( s --[[string]] )
    local charmap = {}

    local res = 0
    local i = 0

    for j = 1, #s do
        local char = s:sub(j, j)
        if charmap[char] ~= nil then
            i = math.max( charmap[char], i)
        end
        res = math.max(res, j - i)
        charmap[char] = j
    end
    return res
end

print(lengthOfLongestSubstring(
    "abcabc"
))