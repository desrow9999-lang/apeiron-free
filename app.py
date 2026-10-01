import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai

# ページ設定
st.set_page_config(
    page_title="Apeiron Free - 対話型ソクラテス",
    page_icon="🤖",
    layout="centered"
)

# --- 無料版の利用制限設定 ---
MAX_TURNS = 5  # 1セッションあたりの最大対話回数

# セッション状態の初期化
if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

# --- ヘッダー表示 ---
st.title("Apeiron Free (アペイロン 無料版)")
st.caption("終わりのない問いを通じて、思考の深淵へダイブするソクラテス的対話システム")

# APIキー設定や対話メイン処理（既存のコードを配置）
# ...

# --- 対話カウントのロジック例 ---
# ユーザーが送信したタイミングで st.session_state.chat_count += 1 を実行

if st.session_state.chat_count >= MAX_TURNS:
    st.warning("⚠️ 無料版の本日（1セッション）の対話上限に達しました。")
    st.info("制限なしでじっくり対話したい場合は、有料版（広告なし）をご利用ください。")

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
