from PIL import Image, ImageFont, ImageDraw
import pandas as pd
def edit_image(text):
    my_image = Image.open("dinner invitation-01.png")
    title_font = ImageFont.truetype('Astro-Font\Futuristic Font\\2 Astro11 sinhala font by Aluth.com.TTF', 95)
    title_text = text
    text_len = len(title_text)
    print(text_len)
    x_alignment = (40-text_len)*13+250
    # title_text = title_text.encode("utf-8")
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((x_alignment,1810), title_text, (0, 0, 0), font=title_font)
    return my_image
def save_image(img,name,folder=''):
    img.save("%s\\%s.png"%(folder,name))

dataframe = pd.read_csv("Teachers' Dinner 2023 - name list 1 (2).csv")
for ind in dataframe.index:
    name_in_english = "_".join(dataframe["English"][ind].split())
    name_in_sinhalaA_encoded = dataframe["Encoded"][ind]
    x = edit_image(name_in_sinhalaA_encoded)
    save_image(x,name_in_english,"Invitations")
