from django.shortcuts import render
import random

def index(request):
    return render(request, 'index.html')

def is_odd_even(request, number):
    
    if number % 2 == 0:
        number_type = '짝수'
    elif number % 2 == 1:
        number_type = '홀수'

    if number == 0:
        number_type = '0'
    
    context = {
        'number' : number,
        'number_type' : number_type,
    }
    return render(request, 'is_odd_even.html', context)
    
def calculate(request, number1, number2):
    plusnumbers = number1 + number2
    minusnumbers = number1 - number2
    multiplynumbers = number1 * number2
    dividenumbers = number1 // number2

    context = {
        'number1' : number1,
        'number2' : number2,
        'plusnumbers' : plusnumbers,
        'minusnumbers' : minusnumbers,
        'multiplynumbers' : multiplynumbers,
        'dividenumbers' : dividenumbers,
    }
    return render(request, 'calculate.html', context)

def pastlife_input(request):
    return render(request, 'pastlife_input.html')

def pastlife_output(request):
    name = request.GET.get('name')
    animals = ['고양이', '강아지', '거북이', '토끼', '뱀', '사자', '호랑이', '표범', '치타', '하이에나', '기린', '코끼리', '코뿔소', '하마', '악어', '펭귄', '부엉이', '올빼미', '곰', '돼지', '소', '닭', '독수리', '타조', '고릴라', '오랑우탄', '침팬지', '원숭이', '코알라', '캥거루', '고래', '상어', '칠면조', '직박구리', '쥐', '청설모', '메추라기', '앵무새', '삵', '스라소니', '판다', '오소리', '오리', '거위', '백조', '두루미', '고슴도치', '두더지', '우파루파', '맹꽁이', '너구리', '개구리', '두꺼비', '카멜레온', '이구아나', '노루', '제비', '까치', '고라니', '수달', '당나귀', '순록', '염소', '공작', '바다표범', '들소', '박쥐', '참새', '물개', '바다사자', '살모사', '구렁이', '얼룩말', '산양', '멧돼지', '카피바라', '도롱뇽', '북극곰', '퓨마', '', '미어캣', '코요테', '라마', '딱따구리', '기러기', '비둘기', '스컹크', '돌고래', '까마귀', '매', '낙타', '여우', '사슴', '늑대', '재규어', '알파카', '양', '다람쥐', '담비']
    pick_animal = random.choice(animals)
    context = {
        'name' : name,
        'pick_animal' : pick_animal,
    }
    return render(request, 'pastlife_output.html', context)

def ipsum_input(request):
    return render(request, 'ipsum_input.html')

def ipsum_output(request):
    paragraph_number = request.GET.get('paragraph_number')
    word_number = request.GET.get('word_number')
    ipsum_words = ['❤️','🧡','💛','💚','💙','💜','⭐','🌟','🌈','⚡','🤍','🤎','🖤','💗','🌕']
    
    ipsum_list = []
    for char in range(int(word_number)):
        pick_emogi = random.choice(ipsum_words)
        ipsum_list.append(pick_emogi)

    context = {
        'ipsum_list' : ipsum_list,
        'range' : range(1, int(paragraph_number) + 1),
        'word_number_range' : range(int(word_number)),
    }
    return render(request, 'ipsum_output.html', context)
