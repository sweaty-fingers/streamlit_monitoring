__all__ = ['ImageComparator']
import os, sys
from pathlib import Path
sys.path.append(str((Path(os.path.abspath(__file__)).parents[3])))

import time
import pandas as pd
import streamlit as st
from PIL import Image
from dashboard.utils import list_files_with_extension

ROOT_DIR = str((Path(os.path.abspath(__file__)).parents[3]))
LOG_PATH = os.path.join(ROOT_DIR, "logs", "realtime_monitoring", "old_model_log.csv")

class ImageComparator:
    def __init__(self, df_path: pd.DataFrame = None, max_points=20):
        # if df_path is None:
        if df_path is None:
            self.df_path = LOG_PATH

        # self.df = None
            
        self.max_points = max_points
        # self.current_index = 0

    def display_images(self, placeholders):
        
        try:
            df = pd.read_csv(self.df_path)
        except FileNotFoundError:
            df = None
        
        if (df is not None) and (not df.empty):
            # recent_df = self.df.tail(1)
            
            # # Initialize session state for slider
            # if 'step' not in st.session_state:
            #     st.session_state.step = int(recent_df['step'].min())

            # # Trackbar to select image pair
            # st.session_state.step = st.slider("Select step", min_value=int(recent_df['step'].min()), max_value=int(recent_df['step'].max()), value=st.session_state.step)
            # selected_row = recent_df[recent_df['step'] == st.session_state.step]
            selected_row = df.iloc[-1]

            # Placeholder for the images

            if not selected_row.empty:
                image_path1 = selected_row['original_image_path']#.values[0]
                image_path2 = selected_row['pred_combined_image_path']#.values[0]
                image_path3 = selected_row['true_combined_image_path']#.values[0]
            
                # 이미지 파일이 존재하는지 확인
                if os.path.exists(image_path1) and os.path.exists(image_path2) and os.path.exists(image_path3):
                    # original_image
                    image1 = Image.open(image_path1)
                    # masked_image
                    image2 = Image.open(image_path2)
                    image3 = Image.open(image_path3)

                    # 이미지를 나란히 표시
                    with placeholders[0].container():
                        col1, col2, col3 = st.columns([1, 1, 1]) 
                        width = 230
                        with col1:
                            # st.image(image1, caption=f"Sample {self.df.id[self.current_index]} - 변환 전", width=300)
                            st.image(image1, caption="Original Image", width=width)
                        with col2:
                            # st.image(image1, caption=f"Sample {self.df.id[self.current_index]} - 변환 전", width=300)
                            st.image(image2, caption="Device Seg Image", width=width)
                        with col3:
                            st.image(image3, caption="True seg Image", width=width)
                            # st.image(image2, caption=f"Sample {self.df.id[self.current_index]} - 변환 후", width=300)

                        
                        st.write(f"Accuracy: {selected_row['accuracy']}")
                        if selected_row['success'] == 1: #".values[0] == 1:
                            st.markdown(
                                            """
                                            <div style="text-align: center;">
                                                <strong>Success.</strong>
                                            </div>
                                            """,
                                            unsafe_allow_html=True
                                        )
                        else:
                            st.markdown(
                                            """
                                            <div style="text-align: center;">
                                                <strong>FAil.</strong>
                                            </div>
                                            """,
                                            unsafe_allow_html=True
                                    )
                            
                else:
                    placeholders[0].error("One or more of the selected images do not exist. Please check the paths.")
            else:
                placeholders[0].error("Selected row is empty. Please check the step value.")                        
        else:
            placeholders[0].error("Log file does not exist. Please check the path.")

    def app(self):
        st.write(f"{st.session_state.active_page}")
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Select a page", ["Result Comparison"])
        if page == "Result Comparison":
            if st.sidebar.button("Update"):
                placeholder1 = st.empty()
                placeholder2 = st.empty()

                placeholders = [placeholder1, placeholder2]
                # self.display_images(placeholders)
                while True:
                    self.display_images(placeholders)
                    time.sleep(1)




def main():
    # 이미지 파일 경로 리스트
    
    df_path = LOG_PATH
    df = pd.read_csv(df_path, index_col=0)
    comparator = ImageComparator(df)
    comparator.display_images()

if __name__ == "__main__":
    main()
