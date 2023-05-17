n=int(input())
s=input()
##input()
#ターミナル上に文字列を入力し，それがinput()の中に入る
#2個連続であるのでそれぞれ順番にある

def is_ok(s):
	l=s.find('|') 
    ##find()
    #指定した文字列が最初に現れるインデックスを返す
	r=s.rfind('|') 
    ##rfind()
    #指定した文字列が最後に現れるインデックスを返す
	tgt=s.find('*') 
	
	if l<tgt<r:
		return True
	return False
	
print('in' if is_ok(s) else 'out')