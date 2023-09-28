"""Include your own tests as functions here"""
import os
from ez_img_diff.api import compare_images


def test_compare_images():
    test_folder_path = os.path.dirname(os.path.join(os.path.abspath(__file__)))
    test_images_path = os.path.join(test_folder_path, "images")
    baseline_image_path = os.path.join(test_images_path, "baseline.png")
    current_image_path = os.path.join(test_images_path, "current.png")
    diff_image_path = os.path.join(test_images_path, "diff.png")
    thresh_image_path = os.path.join(test_images_path, "thresh.png")
    
    result = compare_images(baseline_image_path, current_image_path)
    assert 10 < result < 15
    result = compare_images(baseline_image_path, current_image_path, diff_image_path, thresh_image_path)
    assert 10 < result < 15
    assert os.path.exists(diff_image_path)
    assert os.path.exists(thresh_image_path)
    
    result = compare_images(baseline_image_path, baseline_image_path)
    assert result < 0.01
    
    result = compare_images(current_image_path, current_image_path)
    assert result < 0.01
    



