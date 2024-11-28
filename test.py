import torch

# 假设 tensor_a 是一个张量
tensor_a = torch.tensor([1, 2, 3, 4, 5])

# 创建一个 mask，其中大于 2 的元素被标记为 True
mask = tensor_a > 2

# 方法1: 使用 mask 直接索引
sum_with_mask_indexing = tensor_a[mask].sum()

# 方法2: 使用乘法和 mask
sum_with_multiplication = (tensor_a * mask).sum()

print("Sum with mask indexing:", sum_with_mask_indexing)
print("Sum with multiplication:", sum_with_multiplication)