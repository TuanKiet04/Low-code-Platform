import streamlit as st

st.title("Chatbot Workflow Builder")
st.write("Drag and drop nodes to design your workflow.")

# Danh sách node và kết nối
if 'nodes' not in st.session_state:
    st.session_state.nodes = []
if 'edges' not in st.session_state:
    st.session_state.edges = []

# Thêm node mới
node_type = st.selectbox("Select node type", ["Trigger", "NLP", "Response"])
if st.button("Add Node"):
    new_node = {"id": f"node-{len(st.session_state.nodes)}", "type": node_type}
    st.session_state.nodes.append(new_node)

# Hiển thị danh sách node và kết nối
st.write("Nodes:")
st.write(st.session_state.nodes)
st.write("Edges:")
st.write(st.session_state.edges)

if len(st.session_state.nodes) >= 2:
    source_node = st.selectbox("Select source node", [node["id"] for node in st.session_state.nodes])
    target_node = st.selectbox("Select target node", [node["id"] for node in st.session_state.nodes])
    if st.button("Add Edge"):
        new_edge = {"source": source_node, "target": target_node}
        st.session_state.edges.append(new_edge)