# src/vision_engine.py
import cv2
from ultralytics import YOLO
from config import Config

# 1. Enterprise Pattern: Load model into memory once at microservice boot
model = YOLO(Config.MODEL_NAME)

def process_frame(frame):
    """
    Executes edge-level inference on a single video frame.
    Identifies logistics and transit vehicles, returning the annotated frame and metrics.
    """
    # 2. Execute YOLOv8 inference strictly on target classes (vehicles)
    results = model(
        frame, 
        classes=Config.TARGET_CLASSES, 
        conf=Config.CONFIDENCE_THRESHOLD, 
        verbose=False # Suppress console spam in production
    )
    
    # 3. Extract business intelligence (metrics)
    detections = results[0].boxes
    vehicle_count = len(detections)
    
    # 4. Generate the visual artifact for the UI
    annotated_frame = results[0].plot()
    
    # 5. Convert OpenCV BGR format to standard RGB for Streamlit rendering
    annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    
    return annotated_frame_rgb, vehicle_count