import os
import sys
import cloudinary.uploader

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import core.config  # 這行會自動初始化 Cloudinary

# 你要測試上傳的圖片路徑
IMAGE_PATH = os.path.join(
    os.path.dirname(__file__),
    "test.png"
)

if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"找不到測試圖片: {IMAGE_PATH}")

result = cloudinary.uploader.upload(IMAGE_PATH)

print("Upload success!")
print("secure_url:", result["secure_url"])
print("public_id:", result["public_id"])