res = []
seq = sorted(nums)
for num in nums:
    pos = bisect_left(seq, num)
    res.append(pos)
    seq.pop(pos)
return res
