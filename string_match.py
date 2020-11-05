import re
import Levenshtein

class leven():
  def __init__(self):
    self.special_char_rmv='[^a-zA-Z\s]+'
    self.last_word=["Limited","limited","Ltd.","ltd.","ltd","Ltd",
                    "corporation","Corporation","corp","Corp","corp.","Corp.",
                    "private","Private","pvt.","pvt","Pvt","Pvt.","Industries",
                    "agency","Agency","company","inc.","co","inc","plc","Plc"]

  def remove_spl_char_crtn_words(self,string):
    sentence=re.sub(self.special_char_rmv,"",string)
    exclusions="|".join(self.last_word)
    sentence1=re.sub(exclusions,"",sentence)
    return sentence1

  def lev_score(self,text1,text2):
    max_len=1.0*max(len(text1),len(text2))
    similarity_score=(max_len-Levenshtein.distance(text1,text2))/max_len
    return similarity_score