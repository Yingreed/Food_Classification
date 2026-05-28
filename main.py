import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
import time

# Nhập Data và Giao diện từ file bên ngoài (MVC Architecture)
from food_data import FOOD_INFO
import ui_components as ui

# ── 1. CẤU HÌNH MÔI TRƯỜNG ──────────────────────────────────────────────────
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
 
st.set_page_config(
    page_title="Ẩm Thực Việt | AI",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render CSS và Hero Section
st.markdown(ui.get_custom_css(), unsafe_allow_html=True)
st.markdown(ui.get_hero_section(), unsafe_allow_html=True)
 
# ── 2. LOGIC XỬ LÝ PYTHON ──────────────────────────────────────────────────
def lay_thong_tin(class_name):
    if class_name in FOOD_INFO:
        return FOOD_INFO[class_name]
    ten = class_name.replace("_", " ").title()
    return {
        "ten": ten,
        "mo_ta": f"{ten} là món ăn truyền thống đặc sắc của Việt Nam.",
        "nguon_goc": "Việt Nam",
        "dac_diem": ["Truyền thống", "Đặc sản"],
        "fun_fact": f"{ten} mang đậm bản sắc văn hóa ẩm thực Việt Nam."
    }
 
@st.cache_resource
def load_model(model_path):
    return YOLO(model_path)
 
# ── 3. KHUNG LAYOUT CHÍNH ──────────────────────────────────────────────────
col_left, col_right = st.columns([1, 2], gap="large")
 
with col_left:
    st.markdown('<div class="upload-label">TẢI ẢNH LÊN (JPG, PNG, WEBP)</div>', unsafe_allow_html=True)
    uploaded = st.file_uploader("", type=["jpg","jpeg","png","webp"], label_visibility="collapsed")
 
    if uploaded:
        img = Image.open(uploaded).convert("RGB")
        st.markdown('<div class="img-preview">', unsafe_allow_html=True)
        st.image(img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
 
    st.markdown('<div class="setting-label">ĐƯỜNG DẪN MODEL (.PT)</div>', unsafe_allow_html=True)
    model_path = st.text_input("", value=r"F:\Project\Food_Classification\runs\food_vn_v4\weights\best.pt", label_visibility="collapsed")
 
    st.markdown('<div class="setting-label">HIỂN THỊ TOP (K) KẾT QUẢ</div>', unsafe_allow_html=True)
    top_k = st.slider("", 3, 10, 5, label_visibility="collapsed")
 
    st.markdown('<div class="setting-label">NGƯỠNG TIN CẬY TỐI THIỂU (%)</div>', unsafe_allow_html=True)
    conf_threshold = st.slider("", 0, 100, 10, label_visibility="collapsed", format="%d%%")
 
    run = st.button("🔍  PHÂN TÍCH HÌNH ẢNH", disabled=not uploaded)
 
with col_right:
    if not uploaded:
        st.markdown(ui.get_empty_state_no_image(), unsafe_allow_html=True)
 
    elif run:
        if not os.path.exists(model_path):
            st.error(f"❌ Không tìm thấy model tại `{model_path}`. Kiểm tra lại đường dẫn.")
        else:
            with st.spinner("Đang phân tích hình ảnh..."):
                time.sleep(0.5) 
                model = load_model(model_path)
                results = model(img, imgsz=320, verbose=False)
                probs   = results[0].probs
                names   = results[0].names
                top1_class = names[probs.top1]
                top1_conf  = float(probs.top1conf) * 100
                info = lay_thong_tin(top1_class)
 
            # Bắt lỗi ảnh rác
            NGUONG_ANH_RAC = 40.0 
            if top1_conf < NGUONG_ANH_RAC:
                st.markdown(ui.get_error_not_food(top1_conf), unsafe_allow_html=True)
                
            # Cảnh báo mờ
            elif top1_conf < conf_threshold:
                st.warning(f"⚠️ Độ tin cậy của AI chỉ đạt ({top1_conf:.1f}%). Vui lòng thử lại với ảnh rõ hơn.")  
            
            # In kết quả
            else:
                tags_html = "".join(f'<span class="tag">{t}</span>' for t in info["dac_diem"])
                bar_w = min(int(top1_conf), 100)
 
                # Khối kết quả chính
                st.markdown(ui.get_result_main_html(info, top1_conf, bar_w, tags_html), unsafe_allow_html=True)
 
                # Khối danh sách Top K
                st.markdown(f'<div class="topk-sec"><div class="topk-head">Các dự đoán khác (Top {top_k})</div>', unsafe_allow_html=True)
                
                medals = ["🥇", "🥈", "🥉"]
                top5_indices = probs.top5.tolist() if hasattr(probs.top5, 'tolist') else probs.top5
                
                for i in range(min(top_k, len(top5_indices))):
                    idx  = top5_indices[i]
                    conf = float(probs.top5conf[i]) * 100 if hasattr(probs.top5conf, '__getitem__') else float(probs.top5conf.tolist()[i]) * 100
                        
                    name = names[idx]
                    info_i = lay_thong_tin(name)
                    rank = medals[i] if i < 3 else f"#{i+1}"
                    bw = min(int(conf), 100)
                    bg_color = "#f97316" if i == 0 else "#71717a"
                    
                    st.markdown(ui.get_topk_row_html(rank, info_i["ten"], bw, bg_color, conf), unsafe_allow_html=True)
                    
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown(ui.get_empty_state_uploaded(), unsafe_allow_html=True)