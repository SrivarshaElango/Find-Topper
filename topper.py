import pandas as pd
url = 'https://raw.githubusercontent.com/SrivarshaElango/Find-Topper/main/Student_marks_list.csv'
df = pd.read_csv(url)
print()
#Finding Maths Topper(s)
mmax=df['Maths'].max()
mindex=df.index[df['Maths']==mmax].tolist()
print('Topper(s) in Maths :',end=" ")
for i in mindex :
	print(df['Name'][i],end=" ")
	if(i!=mindex[len(mindex)-1]):
		print('&',end=" ")
print()
#Finding Biology Topper(s)
bmax=df['Biology'].max()
bindex=df.index[df['Biology']==bmax].tolist()
print('Topper(s) in Biology :',end=" ")
for i in bindex :
	print(df['Name'][i],end=" ")
	if(i!=bindex[len(bindex)-1]):
		print('&',end=" ")
print()
#Finding English Topper(s)
emax=df['English'].max()
eindex=df.index[df['English']==emax].tolist()
print('Topper(s) in English :',end=" ")
for i in eindex :
	print(df['Name'][i],end=" ")
	if(i!=eindex[len(eindex)-1]):
		print('&',end=" ")
print()
#Finding Physics Topper(s)
pmax=df['Physics'].max()
pindex=df.index[df['Physics']==pmax].tolist()
print('Topper(s) in Physics :',end=" ")
for i in pindex :
	print(df['Name'][i],end=" ")
	if(i!=pindex[len(pindex)-1]):
		print('&',end=" ")
print()
#Finding Chemistry Topper(s)
cmax=df['Chemistry'].max()
cindex=df.index[df['Chemistry']==cmax].tolist()
print('Topper(s) in Chemistry :',end=" ")
for i in cindex :
	print(df['Name'][i],end=" ")
	if(i!=cindex[len(cindex)-1]):
		print('&',end=" ")
print()
#Finding Hindi Topper(s)
hmax=df['Hindi'].max()
hindex=df.index[df['Hindi']==hmax].tolist()
print('Topper(s) in Hindi :',end=" ")
for i in hindex :
	print(df['Name'][i],end=" ")
	if(i!=hindex[len(hindex)-1]):
		print('&',end=" ")
print()
print()
#Finding top 3 students in the class
r,c=df.shape
avg=[]
for i in range(r) :
	sum=0
	for j in df.columns.values[1:] :
		sum+=int(df[str(j)][i])
	sum/=(c-1)
	a=round(sum,2)
	avg+=[a]
df['Average']=avg
df = df.sort_values(by='Average', ascending=False, ignore_index=True)
print('Best students in the class : ')
for i in range(3) :
	print(df['Name'][i])
	
#Time Complexity of algorithm : O(mn) where m is no. of students and n is no. of subjects 
