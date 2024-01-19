import pandas as pd
import streamlit as st

from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from spire.presentation import Presentation as Presentation2, FileFormat

donations_state_url = "https://raw.githubusercontent.com/MoH-Malaysia/data-darah-public/main/donations_state.csv"

df = pd.read_csv(donations_state_url)
df.to_csv('test.csv')
st.write(df)

