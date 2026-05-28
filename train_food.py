import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from ultralytics import YOLO
import torch

if __name__ == '__main__':
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")

    model = YOLO("yolov8m-cls.pt")   # ← đổi x sang m
    model.train(
        data=r"F:\Project\Food_Classification\data_split",
        epochs=100,
        patience=15,
        imgsz=320,
        batch=64,          # m nhẹ hơn → tăng batch lên 64
        workers=0,
        
        degrees=25.0,
        fliplr=0.5,
        flipud=0.0,
        hsv_h=0.01,
        hsv_s=0.6,
        hsv_v=0.5,
        mosaic=0.0,
        mixup=0.3,
        erasing=0.4,
        scale=0.7,
        translate=0.2,
        shear=5.0,
        perspective=0.0005,
        bgr=0.1,
        dropout=0.4,
        device=0,
        amp=True,
        project=r"F:\Project\Food_Classification\runs",
        name="food_vn_v4",
        exist_ok=True,
    )