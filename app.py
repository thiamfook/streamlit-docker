import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.title("Grouped Bars")

df = pd.DataFrame(
    {
        "Period": ["Jan 2020", "Jan 2020", "Jan 2020", "Feb 2020", "Feb 2020", "Feb 2020", "Mar 2020", "Mar 2020", "Mar 2020", "Apr 2020", "Apr 2020", "Apr 2020"],
        "Group": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"],
        "Value": [425, 787, 784, 664, 642, 965, 525, 588, 632, 237, 367, 788],
    }
)

st.write(df)

tab1, tab2 = st.tabs(["Altair", "Plotly"])
with tab1:
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("yearmonth(Period):O", title=''),
        xOffset="Group:N",
        y=alt.Y("Value:Q"),
        color=alt.Color("Group:N").scale(scheme='pastel1'),
    )
    st.altair_chart(chart, use_container_width=True, theme=None)

with tab2:
    fig = px.histogram(df, x="Period", y="Value",
        color='Group', barmode='group',
    )
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")