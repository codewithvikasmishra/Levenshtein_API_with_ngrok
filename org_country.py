import pandas as pd
import sys

from google.colab import files
src = list(files.upload().values())[0]
open('string_match.ipynb','wb').write(src)
from string_match import leven

data1=pd.read_excel("/content/India_org.xlsx",sheet_name='India_org')
data2=pd.read_excel("/content/UK_org.xlsx",sheet_name='UK_org')

excel1=[]
excel2=[]
excel1=data1['Organisation_india'].tolist()
excel2=data2['Organisation_UK'].tolist()

class type_identification():
  def __init__(self):
    self.string_match=leven()

  def get_org_india(self,search_name,threshold):
    search_name=search_name.lower()
    search_name=self.string_match.remove_spl_char_crtn_words(search_name)
    match_score=[]
    for item in excel1:
      item=item.lower()
      item=self.string_match.remove_spl_char_crtn_words(item)
      match_score.append(self.string_match.lev_score(search_name,item))
    return max(match_score)

  def get_org_UK(self,search_name,threshold):
    search_name=search_name.lower()
    search_name=self.string_match.remove_spl_char_crtn_words(search_name)
    match_score=[]
    for item in excel2:
      item=item.lower()
      item=self.string_match.remove_spl_char_crtn_words(item)
      match_score.append(self.string_match.lev_score(search_name,item))
    return max(match_score)