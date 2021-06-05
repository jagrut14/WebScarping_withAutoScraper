from autoscraper import AutoScraper
import streamlit as st
import pandas as pd
from PIL import Image
url = 'https://www.primeabgb.com/page/1/?post_type=product&taxonomy=product_cat&product_cat=graphic-cards-gpu&s=RTX&orderby=relevance'
#Set title of our Front web app
image = Image.open('logo.png')
st.image(image,use_column_width=True)
st.title('PrimeAbgb Nvidia-RTXcard Availability-checker')
st.write("Visit the following link and enter required details below:      "
         + str(url))
def main():


    url='https://www.primeabgb.com/page/1/?post_type=product&taxonomy=product_cat&product_cat=graphic-cards-gpu&s=RTX&orderby=relevance'



    specs=st.text_input("Enter exact name of any card from PrimeAbgb website")
    discounts=st.text_input("Enter exact discount with % of that particular card")

    search_list=[specs,discounts]
    scraper=AutoScraper()
    scraper.build(url,search_list)
    main=scraper.get_result_similar(
        'https://www.primeabgb.com/page/1/?post_type=product&taxonomy=product_cat&product_cat=graphic-cards-gpu&s=RTX&orderby=relevance',
        grouped=True)
    scraper.set_rule_aliases({list(main.keys())[0]: 'Specs of RTX card', list(main.keys())[1]: 'Discount'})
    scraper.keep_rules([list(main.keys())[0],list(main.keys())[1]])
    scraper.save('PrimeRGB-Nvidia-RTXGPU-scraper')


    for i in range(1,10):



        op=scraper.get_result_similar('https://www.primeabgb.com/page/'+str(i)+'/?post_type=product&taxonomy=product_cat&product_cat=graphic-cards-gpu&s=RTX&orderby=relevance',group_by_alias=True)
        if len(op[list(op.keys())[1]])>0:
            df=pd.DataFrame()
            df['Specs of Nvidia RTX card'] = op[list(op.keys())[0]]
                #df['Total overall cards shown available'] = len(op[list(op.keys())[1]])
            st.success(str(len(op[list(op.keys())[1]]))+' graphic cards are available at page '+str(i))
            st.dataframe(df)





    if st.checkbox('Do you want specs of all the RTX card over PrimeAbgb?'):

        for j in range(1,7):
            try:
                op_all = scraper.get_result_similar(
                    'https://www.primeabgb.com/page/' + str(
                        j) + '/?post_type=product&taxonomy=product_cat&product_cat=graphic-cards-gpu&s=RTX&orderby=relevance',
                    group_by_alias=True)
                df_all = pd.DataFrame()
                df_all['Specs of Nvidia RTX card at page '+str(j)] = op_all[list(op_all.keys())[0]]
                st.dataframe(df_all)
            except Exception:
                pass


if __name__ == '__main__':
    main()

