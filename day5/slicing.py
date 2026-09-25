# Slicing: sequential data(list,tuple,string),
# subset/multiple character or data fetch/get/access
# syntax: variable[start_index: end_index + 1 : step]
# start_index: inclusive ->when accessing a subset the character/data of the start index is included in the result
# end_index: exclusive ->when accessing a subset the character/data of the end index is not included in the result

a = "mind risers"
print(a[0:4])  #mind
print(a[5:11])  #risers
print(a[5:9])  #rise
print(a[:4])  #mind
print(a[5:])  #risers
print(a[:])  #mind risers
print(a[::2])  #mn ies         # kati ota step skip garera data nikalne vannako lagi
print(a[::3])  #mdir

