class Sieunhan:
     def __init__(self, para_ten, para_vu_khi, para_mau_sac):
          self.ten = para_ten
          self.vu_khi = para_vu_khi
          self.mau_sac = para_mau_sac
    
     @classmethod
     def from_string(cls, s) :
          lst = s.split('-')
          new_lst = [st.strip() for st in lst]
          ten, vu_khi, mau_sac = new_lst
          return cls(ten, vu_khi, mau_sac)
     

infor_str = "do - kiem - do"
sieunhanA = Sieunhan.from_string(infor_str)
print(sieunhanA.__dict__)
     



    
    
    

