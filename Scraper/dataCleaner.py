import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Vinit\Naruto-Quotes-Api\narutoquotes.csv', names =['Speakers','Quotes'])

df = df.drop_duplicates()
Quotes = df.Quotes
Speakers = df.Speakers

del Quotes[0]
del Speakers[0]
del Quotes[49]
del Speakers[49]
del Quotes[80]
del Speakers[80]
del Quotes[81]
del Speakers[81]
del Quotes[129]
del Speakers[129]
del Quotes[130]
del Speakers[130]
del Quotes[132]
del Speakers[132]

Full=np.array([Speakers,Quotes])
df = pd.DataFrame(Full.T)
df.to_csv('finalQuotes.csv')