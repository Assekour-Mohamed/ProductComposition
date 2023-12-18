from abc import ABCMeta , abstractmethod

  

class produit(metaclass = ABCMeta) :
    def _init_(self , nom , code) :
        self.__nom = nom
        self.__code = code

    @property
    def nom (self) :
        return self.__nom

    @property
    def code(self) :
        return self.__code

    @abstractmethod
    def getPrixAchat(self) :
        pass

class produitElementaire(produit) :
    def _init_(self, nom, code , prixAchat):
        super()._init_(nom, code) 
        self.__prixAchat = prixAchat
                                                         
    def _str_(self) :
        return (f" [{self.nom}] ( code : {self.code}, pix:{self.__prixAchat} dh )")

    def getPrixAchat(self):
        return self.__prixAchat
  





class composition :
    def _init_(self , produit  , quantite ) :
        self.__produit = produit
        self.__quantite = quantite
    
    @property
    def produit(self) :
        return self.__produit
    
    @produit.setter
    def produit(self , value) :
        self.__produit = value
    
    @property
    def quantite(self) :
        return self.__quantite
    
    @quantite.setter
    def quantite(self , value) :
        self.__quantite = value
    def _str_(self) :
        return f"Quntitie = { self.quantite }  de produit : { self.produit._str_() } "
    def compositionPrix(self):
        return self.produit.getPrixAchat() * self.__quantite




class produit_compose  :
    tauxTVA = 0.18 
    def _init_(self,  fraisFabrication , listeConstituants ):
        self.__fraisFabrication = fraisFabrication
        
        self.__listeConstituants =  listeConstituants

    @property
    def fraisFabrication(self) :
        return self.__fraisFabrication
    
    @fraisFabrication.setter
    def fraisFabrication(self , value) :
        self.__fraisFabrication = value

    
    @property
    def listeConstituants(self) :
        return self.__listeConstituants
    
    @listeConstituants.setter
    def listeConstituants(self , value) :
        self.__listeConstituants = value

    @property
    def TauxTVA(self):
        return self.tauxTVA

    def _str_(self):
        info = ""
        for i in self.__listeConstituants :
            info = info+ i._str_()+ "\n"
        
        return info

    def getPrixHT(self):
        produitsTotalPrix = 0
        for i in self.__listeConstituants:
            produitsTotalPrix += i.compositionPrix()
        return self.__fraisFabrication + produitsTotalPrix 

pe1 = produitElementaire("egg","001",30)
pe2 = produitElementaire("oil","002",30)
 
com1 = composition(pe1,4)
com2 = composition(pe2,5)

CompoditionList =[com1,com2]
produitCompose = produit_compose(10,CompoditionList)
print("[ cake info ] :")
print(produitCompose)
print ("cake Prix : " , produitCompose.getPrixHT()," dh")
