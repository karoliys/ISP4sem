import re
import string
frequency = {}
document_text = open('text.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,100}\b', text_string)
count_words = len(match_pattern)
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])

new_text = re.sub(r'[.!?]\s', r'§', text_string)
sent_num = len(new_text.split('§'))

print('Ср. кол-во слов в предложении: {}.'.format(count_words/sent_num))

words_sentence = re.split(r'§', new_text)

me = [0]* len(words_sentence)
for count in range(len(words_sentence)):
    me[count] =(len(words_sentence[count].split(' ')))
me.sort()
num = len(me)
if (num % 2) == 0:
    print ("Медиана: {}".format((me[len(me)/2]+me[len((me)/2)+1])/2))
else:
    print("Медиана: {}".format(me[int(len(me)/2+0.5)]))


def ngrams(inpt = " ", n = 3):
    output =[" "] * (len(inpt)-n+1)
    for i in range(len(inpt)-n+1):
        output[i] = inpt[i:i+n]
    return output

ngrams_dic = {}
n=3
for word in match_pattern:
    out = ngrams(word, n)
    for i in range(len(out)):
        count = ngrams_dic.get(out[i],0)
        ngrams_dic[out[i]] = count + 1
     
ngrams_dic_list = ngrams_dic.keys()
    


sorted_items = sorted(ngrams_dic.items(),
                              key=lambda item: item[1],
                              reverse=True
                              )
dictionary = dict(sorted_items)

k=10

for (key, value) in list(dictionary.items())[:k]:
    print(f'{key}:{value}')
