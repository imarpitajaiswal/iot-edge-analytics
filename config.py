import os

class Config:
    # Utilizing YOLOv8 Nano for maximum FPS on edge devices without GPUs
    MODEL_NAME = "yolov8n.pt" 
    
    # COCO dataset class IDs for logistics monitoring
    # 2: car, 3: motorcycle, 5: bus, 7: truck
    TARGET_CLASSES = [2, 3, 5, 7] 
    
    # Minimum confidence to register a positive detection
    CONFIDENCE_THRESHOLD = 0.5
    
    # Directory mapping
    ASSETS_DIR = "assets"
    DEFAULT_VIDEO_PATH = os.path.join(ASSETS_DIR, "sample_traffic.mp4")