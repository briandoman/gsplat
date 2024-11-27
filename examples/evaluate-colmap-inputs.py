import os
from pycolmap import SceneManager
import struct


def summarize_colmap_directory(data_dir: str):
    # Set up COLMAP directory paths
    colmap_dir = os.path.join(data_dir, "sparse", "0")
    if not os.path.exists(colmap_dir):
        colmap_dir = os.path.join(data_dir, "sparse")
    if not os.path.exists(colmap_dir):
        print(f"COLMAP directory {colmap_dir} does not exist.")
        return

    print(f"Scanning COLMAP files in: {colmap_dir}")

    # Initialize SceneManager to manage the COLMAP scene
    manager = SceneManager(colmap_dir)
    print(f"...post manager...")
    try:
        manager.load_cameras()
        print("Cameras loaded successfully.")
    except struct.error as e:
        print("Error reading camera data:", e)
        return

    try:
        manager.load_images()
        print(f"{len(manager.images)} images loaded successfully.")
    except struct.error as e:
        print("Error reading image data:", e)
        return

    try:
        manager.load_points3D()
        print(f"{len(manager.points3D)} 3D points loaded successfully.")
    except struct.error as e:
        print("Error reading 3D points data:", e)
        return

    # Summarize camera information
    camera_ids = set(im.camera_id for im in manager.images.values())
    print(f"Found {len(camera_ids)} unique cameras.")

    # Display details about cameras and images
    for camera_id in camera_ids:
        cam = manager.cameras[camera_id]
        print(f"Camera ID {camera_id}: Type = {cam.camera_type}, "
              f"Resolution = {cam.width}x{cam.height}, "
              f"Focal Length = ({cam.fx}, {cam.fy})")

    print("[Summary] COLMAP data structure checked. No critical issues found in loading.")


if __name__ == "__main__":
    #data_dir = "data/360_v2/garden"  # Adjust path as needed
    data_dir = r"D:/Fuse-TG/Projects/Active/iris/gaussian-splatting/gsplat/examples/data/360_v2/garden"

    summarize_colmap_directory(data_dir)
