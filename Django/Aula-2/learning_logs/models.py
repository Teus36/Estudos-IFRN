from django.db import models

class tb_topic(models.Model): 
    top_text = models.CharField(max_length=255)
    top_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        
    #Devolve representação em string do modelo
        return self.top_text