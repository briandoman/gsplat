import torch

def check_image_normalization(img, name="image"):
    """
    Checks if the input image tensor is normalized for LPIPS.
    LPIPS requires:
    - Shape: [N, 3, H, W]
    - Range: [0, 1]
    - Data type: float32
    
    Parameters:
        img (torch.Tensor): Input image tensor.
        name (str): Name of the image for logging purposes.
    
    Returns:
        bool: True if the image is normalized, False otherwise.
    """
    is_valid = True

    # Check shape
    if len(img.shape) != 4 or img.shape[1] != 3:
        print(f"{name} has invalid shape: {img.shape}. Expected [N, 3, H, W].")
        is_valid = False

    # Check range
    if img.min() < 0 or img.max() > 1:
        print(f"{name} has invalid range: [{img.min().item()}, {img.max().item()}]. Expected [0, 1].")
        is_valid = False

    # Check data type
    if img.dtype != torch.float32:
        print(f"{name} has invalid data type: {img.dtype}. Expected torch.float32.")
        is_valid = False

    if is_valid:
        print(f"{name} is properly normalized.")
    return is_valid
