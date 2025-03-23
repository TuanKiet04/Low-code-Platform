import streamlit as st

st.title("Chatbot Workflow Builder")
st.write("Drag and drop nodes to design your workflow.")

# Add simple node selection
node_type = st.selectbox("Select node type", ["Trigger", "NLP", "Response"])
st.write(f"You selected: {node_type}")

if st.button("Save Workflow"):
    st.write("Workflow saved!")