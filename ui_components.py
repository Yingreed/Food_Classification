# --- FILE: ui_components.py ---

def get_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    * { box-sizing: border-box; }
    html, body, [class*="css"], .stApp { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #09090b; color: #e4e4e7; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 1300px !important; margin: 0 auto; }
    .hero-wrapper { text-align: center; padding: 60px 20px 40px 20px; background: radial-gradient(circle at 50% 0%, rgba(234, 88, 12, 0.15) 0%, transparent 60%); border-bottom: 1px solid rgba(255,255,255,0.05); margin-bottom: 40px; }
    .badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(234, 88, 12, 0.1); border: 1px solid rgba(234, 88, 12, 0.2); padding: 6px 16px; border-radius: 50px; font-size: 0.75rem; font-weight: 600; letter-spacing: 1px; color: #fdba74; text-transform: uppercase; margin-bottom: 20px; }
    .hero-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(3rem, 5vw, 5rem); font-weight: 700; line-height: 1.1; color: #fafafa; margin-bottom: 16px; }
    .hero-title em { font-style: italic; color: #ea580c; }
    .hero-subtitle { font-size: 1rem; color: #a1a1aa; font-weight: 400; max-width: 600px; margin: 0 auto 30px; line-height: 1.6; }
    .hero-features { display: flex; justify-content: center; gap: 24px; flex-wrap: wrap; }
    .hero-feature { font-size: 0.85rem; color: #d4d4d8; display: flex; align-items: center; gap: 6px; }
    .hero-feature span { color: #fdba74; font-weight: 600; }
    [data-testid="column"]:nth-of-type(1) { background-color: #18181b; border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 30px !important; box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5); }
    [data-testid="column"]:nth-of-type(2) { padding: 20px 0 20px 40px !important; }
    [data-testid="stFileUploadDropzone"] { background-color: rgba(234, 88, 12, 0.05) !important; border: 2px dashed rgba(234, 88, 12, 0.3) !important; border-radius: 16px !important; padding: 30px !important; transition: all 0.3s ease !important; }
    [data-testid="stFileUploadDropzone"]:hover { background-color: rgba(234, 88, 12, 0.1) !important; border-color: #ea580c !important; }
    .st-emotion-cache-1gkelhq, [data-testid="stFileUploadDropzone"] div { color: #a1a1aa !important; }
    .st-emotion-cache-1gkelhq:hover { color: #ea580c !important; }
    .st-emotion-cache-10trncj p, label[data-baseweb="label"] { font-size: 0.8rem !important; font-weight: 600 !important; color: #d4d4d8 !important; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px !important; }
    [data-baseweb="input"] { background-color: transparent !important; }
    .stTextInput > div > div > div { background-color: #27272a !important; border: 1px solid #3f3f46 !important; border-radius: 10px !important; color: white !important; }
    .stTextInput > div > div > div:focus-within { border-color: #ea580c !important; box-shadow: 0 0 0 1px #ea580c !important; }
    .stSlider [data-testid="stTickBar"] { display: none; }
    .stSlider > div > div { background-color: #27272a !important; }
    .stSlider > div > div > div > div { background-color: #ea580c !important; }
    [data-testid="baseButton-secondary"] { background: linear-gradient(135deg, #f97316, #ea580c) !important; color: white !important; border: none !important; border-radius: 12px !important; font-weight: 600 !important; font-size: 1rem !important; padding: 24px 0 !important; margin-top: 10px !important; box-shadow: 0 4px 15px rgba(234, 88, 12, 0.3) !important; transition: all 0.2s !important; }
    [data-testid="baseButton-secondary"]:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 20px rgba(234, 88, 12, 0.4) !important; }
    [data-testid="baseButton-secondary"]:disabled { background: #3f3f46 !important; color: #71717a !important; box-shadow: none !important; transform: none !important; }
    .empty-box { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; min-height: 500px; text-align: center; padding: 40px; border: 1px dashed rgba(255,255,255,0.1); border-radius: 24px; background: rgba(255,255,255,0.02); animation: fadeIn 0.5s ease; }
    .empty-box-icon { font-size: 3.5rem; margin-bottom: 20px; animation: float 3s ease-in-out infinite; }
    .empty-box-title { font-family: 'Cormorant Garamond', serif; font-size: 2rem; color: #fafafa; margin-bottom: 10px; }
    .empty-box-desc { font-size: 0.9rem; color: #a1a1aa; line-height: 1.6; }
    .img-preview { border-radius: 16px; overflow: hidden; border: 2px solid #27272a; margin-bottom: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.4); }
    .res-header { display: flex; align-items: center; gap: 20px; margin-bottom: 30px; animation: fadeIn 0.5s ease; }
    .res-icon { background: linear-gradient(135deg, #f97316, #ea580c); width: 64px; height: 64px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 2rem; box-shadow: 0 8px 20px rgba(234, 88, 12, 0.25); }
    .res-title { font-family: 'Cormorant Garamond', serif; font-size: 3rem; font-weight: 700; color: #fff; line-height: 1; margin-bottom: 8px; }
    .res-origin { font-size: 0.9rem; color: #fdba74; display: flex; align-items: center; gap: 6px; }
    .conf-box { background: #18181b; border: 1px solid #27272a; border-radius: 16px; padding: 20px; margin-bottom: 30px; animation: fadeIn 0.6s ease; }
    .conf-top { display: flex; justify-content: space-between; margin-bottom: 12px; }
    .conf-label { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; color: #a1a1aa; font-weight: 600; }
    .conf-num { font-size: 1.2rem; font-weight: 700; color: #f97316; }
    .conf-bar-bg { height: 6px; background: #27272a; border-radius: 10px; overflow: hidden; }
    .conf-bar-fill { height: 100%; background: linear-gradient(90deg, #f97316, #fcd34d); border-radius: 10px; transition: width 1s ease; }
    .desc-box { font-size: 1rem; line-height: 1.8; color: #d4d4d8; padding-left: 20px; border-left: 3px solid #ea580c; margin-bottom: 30px; animation: fadeIn 0.7s ease; }
    .fact-box { background: rgba(234, 88, 12, 0.05); border: 1px solid rgba(234, 88, 12, 0.2); border-radius: 16px; padding: 20px; display: flex; gap: 16px; margin-bottom: 30px; animation: fadeIn 0.8s ease; }
    .fact-icon { font-size: 1.5rem; }
    .fact-content p { margin: 0; font-size: 0.95rem; color: #e4e4e7; line-height: 1.6; }
    .fact-content strong { color: #f97316; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 4px; }
    .tags-row { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; animation: fadeIn 0.9s ease; }
    .tag { background: #27272a; border: 1px solid #3f3f46; color: #d4d4d8; font-size: 0.8rem; padding: 6px 16px; border-radius: 50px; }
    .topk-sec { margin-top: 40px; padding-top: 30px; border-top: 1px dashed rgba(255,255,255,0.1); animation: fadeIn 1s ease; }
    .topk-head { font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; color: #a1a1aa; font-weight: 600; margin-bottom: 20px; }
    .topk-row { display: flex; align-items: center; gap: 16px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .topk-medal { width: 30px; text-align: center; font-size: 1.1rem; color: #71717a; font-weight: bold; }
    .topk-name { flex: 1; font-size: 1rem; color: #e4e4e7; }
    .topk-track { width: 120px; height: 4px; background: #27272a; border-radius: 10px; overflow: hidden; }
    .topk-fill { height: 100%; border-radius: 10px; }
    .topk-val { width: 50px; text-align: right; font-size: 0.85rem; color: #a1a1aa; font-variant-numeric: tabular-nums; }
    .stAlert { border-radius: 16px !important; background: rgba(220, 38, 38, 0.1) !important; border: 1px solid rgba(220, 38, 38, 0.3) !important; color: #fca5a5 !important; }
    @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
    </style>
    """

def get_hero_section():
    return """
    <div class="hero-wrapper">
        <div class="badge">🤖 YOLOv8 AI Model</div>
        <div class="hero-title">Khám phá<br><em>ẩm thực</em> Việt</div>
        <div class="hero-subtitle">Ứng dụng trí tuệ nhân tạo để nhận diện món ăn. Hãy tải lên một bức ảnh và lắng nghe câu chuyện đằng sau những hương vị truyền thống.</div>
        <div class="hero-features">
            <div class="hero-feature">✨ <span>100+</span> món ăn Việt</div>
            <div class="hero-feature">🎯 <span>Độ chính xác cao</span></div>
            <div class="hero-feature">📚 <span>Thông tin văn hóa</span></div>
        </div>
    </div>
    """

def get_empty_state_no_image():
    return """
    <div class="empty-box">
        <div class="empty-box-icon">🍜</div>
        <div class="empty-box-title">Chưa có dữ liệu</div>
        <div class="empty-box-desc">Hãy tải lên một bức ảnh ở bảng điều khiển bên trái<br>để AI bắt đầu nhận diện món ăn.</div>
    </div>
    """

def get_empty_state_uploaded():
    return """
    <div class="empty-box">
        <div class="empty-box-icon">✨</div>
        <div class="empty-box-title">Đã tải ảnh lên</div>
        <div class="empty-box-desc">Hãy nhấn nút <strong>Phân tích hình ảnh</strong><br>để xem kết quả nhận diện.</div>
    </div>
    """

def get_error_not_food(conf):
    return f"""
    <div style="background: rgba(220, 38, 38, 0.08); border: 1px solid rgba(220, 38, 38, 0.3); padding: 30px; border-radius: 20px; margin-bottom: 30px; animation: fadeIn 0.5s ease;">
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px;">
            <span style="font-size: 2.8rem; animation: float 3s infinite;">🛑</span>
            <h3 style="color: #fca5a5; margin: 0; font-size: 1.5rem; font-family: 'Plus Jakarta Sans', sans-serif;">Hình ảnh không hợp lệ! ({conf:.1f}%)</h3>
        </div>
        <div style="color: #d4d4d8; line-height: 1.7; padding-left: 65px; font-size: 1rem;">
            Trí tuệ nhân tạo phân tích và <b>không tìm thấy đặc điểm của món ăn</b> trong bức ảnh này.<br>
            Có vẻ bạn đã tải lên hình ảnh của <b>người, phong cảnh, xe cộ</b> hoặc một vật thể khác lạ.<br>
            <span style="color: #f97316; font-weight: 600; display: inline-block; margin-top: 8px;">
                💡 Vui lòng bỏ hình ảnh món ăn vào hệ thống để AI nhận diện chính xác nhé!
            </span>
        </div>
    </div>
    """

def get_result_main_html(info, top1_conf, bar_w, tags_html):
    return f"""
    <div class="res-header">
        <div class="res-icon">🥢</div>
        <div>
            <div class="res-title">{info["ten"]}</div>
            <div class="res-origin">📍 Nguồn gốc: {info["nguon_goc"]}</div>
        </div>
    </div>
    <div class="conf-box">
        <div class="conf-top">
            <span class="conf-label">Mức độ tự tin (Confidence)</span>
            <span class="conf-num">{top1_conf:.1f}%</span>
        </div>
        <div class="conf-bar-bg"><div class="conf-bar-fill" style="width: {bar_w}%;"></div></div>
    </div>
    <div class="desc-box">{info["mo_ta"]}</div>
    <div class="fact-box">
        <div class="fact-icon">💡</div>
        <div class="fact-content">
            <strong>Bạn có biết?</strong>
            <p>{info["fun_fact"]}</p>
        </div>
    </div>
    <div class="tags-row">{tags_html}</div>
    """

def get_topk_row_html(rank, name, bw, bg_color, conf):
    return f"""
    <div class="topk-row">
        <div class="topk-medal">{rank}</div>
        <div class="topk-name">{name}</div>
        <div class="topk-track"><div class="topk-fill" style="width: {bw}%; background: {bg_color};"></div></div>
        <div class="topk-val">{conf:.1f}%</div>
    </div>
    """