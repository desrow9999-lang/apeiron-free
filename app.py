import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai
import datetime
import urllib.parse

# ページ設定
st.set_page_config(
    page_title="Apeiron Free - 究極ソクラテス",
    page_icon="🔮",
    layout="centered"
)

# 【極上のUI：オーロラダークCSS】
st.markdown("""
<style>
/* 全体の背景とベースカラー */
.stApp {
    background: radial-gradient(circle at top center, #0f172a 0%, #050508 100%);
    color: #f1f5f9;
}

/* ヘッダーデザイン */
.app-header {
    background: linear-gradient(135deg, rgba(30, 27, 75, 0.7), rgba(15, 23, 42, 0.9));
    border: 1px solid rgba(129, 140, 248, 0.3);
    padding: 20px 24px;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}

.app-title {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-weight: 800;
    font-size: 1.6rem !important;
    background: linear-gradient(135deg, #c7d2fe, #a855f7, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 4px 0;
}

.app-subtitle {
    color: #94a3b8;
    font-size: 13px;
    margin: 0;
    letter-spacing: 0.5px;
}

/* 有料版プロモーションカード */
.pro-banner {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(56, 189, 248, 0.2));
    border: 1px solid rgba(168, 85, 247, 0.4);
    padding: 16px 20px;
    border-radius: 16px;
    margin-bottom: 20px;
    text-align: center;
}

.pro-title {
    color: #f43f5e;
    font-weight: 700;
    font-size: 15px;
    margin-bottom: 6px;
}

.pro-link-btn {
    display: inline-block;
    background: linear-gradient(135deg, #a855f7, #6366f1);
    color: white !important;
    font-weight: bold;
    padding: 8px 20px;
    border-radius: 12px;
    text-decoration: none;
    margin-top: 8px;
    box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
}

/* インフォメーション・分析カード */
.insight-card {
    background: linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(30, 27, 75, 0.5));
    border: 1px solid rgba(129, 140, 248, 0.25);
    padding: 16px;
    border-radius: 16px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# 【ヘッダー表示】
st.markdown("""
<div class="app-header">
    <div class="app-title">🔮 Apeiron Free <span style="font-size: 1.1rem; font-weight: 400; color: #ec4899;">(アペイロン 無料版)</span></div>
    <p class="app-subtitle">終わりなき問いを通じて、思考の深淵へとダイブするソクラテス的対話システム</p>
</div>
""", unsafe_allow_html=True)

# 【有料版への誘導バナー】
# ※「https://xxx.streamlit.app」部分を実際の有料版URLに書き換えてください
st.markdown("""
<div class="pro-banner">
    <div class="pro-title">✨ 制限なし＆広告なしで快適に使いたい方へ</div>
    <div style="font-size: 12px; color: #cbd5e1;">無制限対話・高速レスポンスの「有料版 Apeiron」はこちら</div>
    <a href="https://buy.stripe.com/7sY7sK0z4fDbfRxbn8eZ209" target="_blank" class="pro-link-btn">有料版 Apeiron を開く 🚀</a>
</div>
""", unsafe_allow_html=True)

# --- ここから下にAPIキー入力やチャット処理を記述 ---

# 【APIキー管理】
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.markdown("""
<div class="insight-card">
    <div style="color: #f59e0b; font-weight: bold; margin-bottom: 8px;">🔑 APIキーの入力が必要です</div>
    <div style="font-size: 13px; color: #94a3b8;">思考の深淵を開くため、有効なGemini APIキーを入力してください。</div>
</div>
""", unsafe_allow_html=True)

api_key_input = st.text_input("ここにAPIキーを入力", type="password", value=st.session_state.api_key)
if api_key_input:
    st.session_state.api_key = api_key_input.strip()


# --- 画面最下部に広告を設置 ---
st.write("---")
st.caption("スポンサーリンク")

a8_code = """
<div style="display: flex; justify-content: center;">
<a href="https://px.a8.net/svt/ejp?a8mat=4BE68R+1SAU42+4GSM+C33KX" rel="nofollow">
<img border="0" width="300" height="250" alt="" src="https://www26.a8.net/svt/bgt?aid=261001755108&wid=001&eno=01&mid=s00000020839002030000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www3.a8.net/0.gif?a8mat=4BE68R+1SAU42+4GSM+C33KX" alt="">
</div>
"""

components.html(a8_code, height=270)
