import streamlit as st
import torch
from torchvision.models import googlenet, GoogLeNet_Weights
import torch.nn as nn
from torchvision import transforms
from PIL import Image
from streamlit_option_menu import option_menu
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO
import base64
# Function to initialize the model
def initialize_model():
    model = googlenet(weights=GoogLeNet_Weights.IMAGENET1K_V1)
    model.fc = nn.Sequential(
        nn.Linear(in_features=1024, out_features=512),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(in_features=512, out_features=128),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(in_features=128, out_features=64),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(in_features=64, out_features=4)
    )
    model.load_state_dict(torch.load(r'blood_cancer_model.pth'))
    model.eval()
    return model

# Transformation function
def preprocess_image(img_path):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])
    img = Image.open(img_path)
    img = transform(img)
    img = img.unsqueeze(0)  # Add batch dimension
    return img

# Resource usage functions
# def get_cpu_memory_usage():
#     process = psutil.Process()
#     cpu_usage = process.cpu_percent(interval=1)
#     memory_info = process.memory_info()
#     memory_usage = memory_info.rss / (1024 ** 2)  # Convert bytes to MB
#     return cpu_usage, memory_usage

#def get_gpu_memory_usage():
#     if torch.cuda.is_available():
#         gpu_memory_allocated = torch.cuda.memory_allocated() / (1024 ** 2)  # Convert bytes to MB
#         gpu_memory_reserved = torch.cuda.memory_reserved() / (1024 ** 2)  # Convert bytes to MB
#         return gpu_memory_allocated, gpu_memory_reserved
#     return None, None

# Streamlit app
# Main function
st.title("LeukoApp - Blood Cancer Prediction")
if __name__ == '__main__':
    with st.sidebar:
        selected = option_menu('Blood Cancer Predictor',
                          ['LeukoApp - Blood Cancer Prediction',
                           #'Our Prediction Records',
                           'About Us'],
                          icons=['heart','book','info'],
                          default_index=0)
if selected =="LeukoApp - Blood Cancer Prediction":
    st.write("Upload an image to predict the type of blood cancer.")
    # File uploader
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load model
        model = initialize_model()

        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Preprocess image
        img_tensor = preprocess_image(uploaded_file)

        # Select device
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        model = model.to(device)
        img_tensor = img_tensor.to(device)

        # Get resource usage before prediction
        # cpu_usage_before, memory_usage_before = get_cpu_memory_usage()
        # gpu_memory_allocated_before, gpu_memory_reserved_before = get_gpu_memory_usage()

        # Make prediction
        with torch.no_grad():
            output = model(img_tensor)
            probabilities = torch.nn.functional.softmax(output, dim=1)
            confidence, predicted_class = torch.max(probabilities, 1)

        # Labels map
        labels_map = {0: 'Normal Study', 1: 'Early_Pre_B-Abnormal Leukocyte Forms', 2: 'Pre_B-Abnormal Leukocyte Form', 3: 'Abnormal Leukocyte Form'}
        predicted_class_name = labels_map[predicted_class.item()]
        confidence_score = confidence.item()
        
        if predicted_class_name in ['Early Pre-B-Abnormal Leukocyte Form', 'Pre_B-Abnormal Leukocyte Form', 'Abnormal Leukocyte Form']:
            formatted_class_name = f"Malignant - {predicted_class_name}"
        else:
            formatted_class_name = "Normal Study"

        # Display results
        st.subheader("Prediction Results")
        st.write(f"**Predicted Class:** {formatted_class_name}")
        st.write(f"**Confidence Score:** {confidence_score:.4f}")
        # Get resource usage after prediction
        # cpu_usage_after, memory_usage_after = get_cpu_memory_usage()
        # gpu_memory_allocated_after, gpu_memory_reserved_after = get_gpu_memory_usage()
        
        # st.subheader("Resource Usage")
        # st.write(f"**CPU Usage Before:** {cpu_usage_before:.2f}%")
        # st.write(f"**Memory Usage Before:** {memory_usage_before:.2f} MB")
        # st.write(f"**CPU Usage After:** {cpu_usage_after:.2f}%")
        # st.write(f"**Memory Usage After:** {memory_usage_after:.2f} MB")
        # st.write(f"**CPU Used:** {cpu_usage_after - cpu_usage_before:.2f}%")
        # st.write(f"**Memory Used:** {memory_usage_after - memory_usage_before:.2f} MB")

        # if gpu_memory_allocated_before is not None and gpu_memory_reserved_before is not None:
        #     st.write(f"**GPU Memory Allocated Before:** {gpu_memory_allocated_before:.2f} MB")
        #     st.write(f"**GPU Memory Reserved Before:** {gpu_memory_reserved_before:.2f} MB")
        #     st.write(f"**GPU Memory Allocated After:** {gpu_memory_allocated_after:.2f} MB")
        #     st.write(f"**GPU Memory Reserved After:** {gpu_memory_reserved_after:.2f} MB")
        #     st.write(f"**GPU Memory Allocated:** {gpu_memory_allocated_after - gpu_memory_allocated_before:.2f} MB")
        #     st.write(f"**GPU Memory Reserved:** {gpu_memory_reserved_after - gpu_memory_reserved_before:.2f} MB")

# if selected == "Our Prediction Records":
if selected == "About Us":
        st.markdown("<h2 style='text-align: center;'>ABOUT</h2>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<p style='text-align: center;'>Ideation Partner : Shawred Analytics Pvt Ltd</p>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<h4 style='text-align: center;'>Developed and maintained by</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Pavan Kumar Didde</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Shaik Zuber</p>", unsafe_allow_html=True)
        st.markdown("____")



