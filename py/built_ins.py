print(any([0,0,1,1,]))
print(any([0,0,0,0]))

print(any(['','','']))
print(any(['non empty','']))

my_str='my_string'
for position,val in enumerate(my_str):
    print(position,val)

my_list_string=['s1','s2','s3']
print(list(enumerate(my_list_string)))

marks_data=[91,92,45,70,60,50,100,99,75,85]

def filter_fun(x):
    return  x<75

for marks in filter(filter_fun,marks_data):
    print("what are u going to do with the future of students who socred",marks)

def to_upper(x):
    return x.upper()

my_list = ['a', 'b', 'c', 'd', 'e']
for item in map(to_upper, my_list):
    print(item)

keys=[1,2,3,4,5]
values=['a','b','c','d','e']

print(list(zip(keys,values)))
print(dict(zip(keys,values)))


my_str="this is string"
my_unicode_str = u'this is unicode string'
print(type(my_str))
print(type(my_unicode_str))

english_variable = "This is English variable"
hindi_चर = "This is Hindi variable"
urdu_متغیر = "This is Urdu variable"
telugu_చరము = "This is Telugu variable"
kannada_ಚರ = "This is Kannada variable"
tamil_மாறி = "This is Tamil variable"
marathi_चल = "This is Marathi variable"
gujarati_ચલ = "This is Gujarati variable"
bengali_চলক = "This is Bengali variable"
arabic_متغير = "This is Arabic variable"

french_variable = "This is French variable"
finnish_muuttuja = "This is Finnish variable"
swedish_variabel = "This is Swedish variable"
korean_변수 = "This is Korean variable"
chinese_变量 = "This is Chinese variable"
japanese_変数 = "This is Japanese variable"


print(english_variable)
print(hindi_चर)
print(urdu_متغیر)
print(telugu_చరము)
print(kannada_ಚರ)
print(tamil_மாறி)

print(marathi_चल)
print(gujarati_ચલ)
print(bengali_চলক)
print(arabic_متغير)
print(french_variable)
print(swedish_variabel)
print(finnish_muuttuja)
print(korean_변수)
print(chinese_变量)
print(japanese_変数)
