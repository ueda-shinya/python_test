import streamlit as st

check = st.checkbox("チェックボックス") #引数に入れることでboolを返す
if check:
  st.button("ボタン") #引数に入れるとboolで返す
  st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名、第二引数：選択肢
  st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名、第二引数：選択肢、複数選択可
  st.radio("ラジオボタン", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名（選択肢群の上に表示）、第二引数：選択肢
# 以下をサイドバーに表示
st.sidebar.text_input("文字入力欄") #引数に入力内容を渡せる
st.sidebar.text_area("テキストエリア")