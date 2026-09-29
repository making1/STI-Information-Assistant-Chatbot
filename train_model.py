from pathlib import Path
import json, joblib, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,f1_score
B=Path(__file__).resolve().parent
D=pd.read_csv(B/'data/intent_training.csv').dropna().drop_duplicates()
Xtr,Xte,ytr,yte=train_test_split(D.text,D.intent,test_size=.25,random_state=42,stratify=D.intent)
p=Pipeline([('tfidf',TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True)),('clf',LogisticRegression(max_iter=2000,class_weight='balanced'))])
p.fit(Xtr,ytr); pred=p.predict(Xte)
classes=sorted(D.intent.unique())
metrics={'accuracy':accuracy_score(yte,pred),'macro_f1':f1_score(yte,pred,average='macro'),'weighted_f1':f1_score(yte,pred,average='weighted'),'n_test':len(yte)}
(B/'models').mkdir(exist_ok=True); (B/'evaluation').mkdir(exist_ok=True)
joblib.dump({'pipeline':p,'metrics':metrics},B/'models/intent_model.joblib')
(B/'evaluation/metrics.json').write_text(json.dumps(metrics|{'classification_report':classification_report(yte,pred,output_dict=True)},indent=2))
pd.DataFrame(confusion_matrix(yte,pred,labels=classes),index=classes,columns=classes).to_csv(B/'evaluation/confusion_matrix.csv')
print(metrics)
