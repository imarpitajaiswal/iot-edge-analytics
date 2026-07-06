# app.py
import streamlit as st
import cv2
import tempfile
import os
from config import Config
from src.vision_engine import process_frame

# 1. UI Configuration
st.set_page_config(
    page_title="IoT Edge Analytics", 
    page_icon="🚦", 
    layout="wide"
)

st.title("🚦 Industrial IoT Edge Analytics")
st.markdown("### Real-Time Computer Vision for Logistics & Infrastructure")
st.divider()

# 2. Command Center Layout
col1, col2 = st.columns([1, 3])

with col1:
    st.header("Data Source")
    source_type = st.radio("Select Input Stream:", ["Use Default Asset", "Upload Custom Video"])
    
    uploaded_file = None
    if source_type == "Upload Custom Video":
        uploaded_file = st.file_uploader("Upload Edge Footage (MP4)", type=["mp4"])
        
    start_button = st.button("Initialize Edge Processing", type="primary", use_container_width=True)
    stop_button = st.button("Halt Execution", use_container_width=True)
    
    st.markdown("---")
    st.subheader("Live Telemetry")
    # Dynamic placeholder for real-time metrics
    metric_placeholder = st.empty()
    metric_placeholder.metric(label="Active Vehicles Detected", value=0)

with col2:
    # Dynamic placeholder for the video feed
    stframe = st.empty()
    if not start_button:
        stframe.info("Awaiting processing initialization. Please select a video source and click 'Initialize Edge Processing'.")

# 3. Execution Pipeline
if start_button:
    video_path = None
    
    # Resolve file paths
    if source_type == "Use Default Asset":
        if not os.path.exists(Config.DEFAULT_VIDEO_PATH):
            st.error(f"CRITICAL: Default asset missing at {Config.DEFAULT_VIDEO_PATH}.")
        else:
            video_path = Config.DEFAULT_VIDEO_PATH
    elif uploaded_file is not None:
        # Securely handle custom uploads via tempfiles
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(uploaded_file.read())
        video_path = tfile.name

    if video_path:
        cap = cv2.VideoCapture(video_path)
        
        with st.spinner("Compiling YOLOv8 Tensor and Processing Stream..."):
            while cap.isOpened() and not stop_button:
                ret, frame = cap.read()
                
                # End of video stream
                if not ret:
                    break
                
                # Execute inference
                annotated_frame, count = process_frame(frame)
                
                # Update UI elements dynamically
                # Patcher: Replaced use_container_width with use_column_width for v1.32.0 compatibility
                stframe.image(annotated_frame, channels="RGB", use_column_width=True)
                metric_placeholder.metric(label="Active Vehicles Detected", value=count)
                
        cap.release()
        
        # Cleanup temp file if custom upload was used
        if source_type == "Upload Custom Video" and os.path.exists(video_path):
            os.remove(video_path)
            
        st.success("Stream processing finalized.")