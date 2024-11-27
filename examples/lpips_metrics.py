
import torch
from torchmetrics.image.lpip import LearnedPerceptualImagePatchSimilarity

# Instantiate the LPIPS metric
lpips_metric = LearnedPerceptualImagePatchSimilarity(net_type='vgg').to('cuda')  # Use 'vgg', 'alex', or 'squeeze'

# Example inputs
img1 = torch.rand(1, 3, 256, 256).to('cuda')  # Random tensor for example
img2 = torch.rand(1, 3, 256, 256).to('cuda')

# Calculate LPIPS distance
lpips_value = lpips_metric(img1, img2)
print(f"LPIPS value: {lpips_value.item()}")