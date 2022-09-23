from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['족발', '피자', '치킨', '떡볶이', '초밥', '파스타', '짜장면']
    foods_img = [
        'http://image.auction.co.kr/itemimage/23/f5/a6/23f5a6ee96.jpg',
        'https://cdn.dominos.co.kr/admin/upload/goods/20200311_x8StB1t3.jpg',
        'https://pelicana.co.kr/resources/images/menu/original_menu01_200529.png',
        'https://doewxs707ovkc.cloudfront.net/v3/prod/image/item/mainpage/907/ad4474bef39c4167b84477eaa7a5052f20210708171733.',
        'https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/00/a0000370/img/basic/a0000370_main.jpg?20201002142956&q=80&rw=750&rh=536',
        'https://bakeitwithlove.com/wp-content/uploads/2021/10/lemon-garlic-shrimp-pasta-sq.jpg',
        'https://img-cf.kurly.com/shop/data/goodsview/20201012/gv10000126356_1.jpg',
    ]
    pick = random.choice(foods)
    context = {
        'name': pick,
        'image': foods_img[foods.index(pick)],
    }
    return render(request, 'today-dinner.html', context)

def lotto(request):
    win_number = [3, 11, 15, 29, 35, 44]
    bonus_number = 10
    lotto_paper = []

    for i in range(5):
        cnt = 0
        result = 0
        numbers = random.sample(range(1, 46), 6)

        for j in numbers:
            if j in win_number:
                cnt += 1
        if cnt < 3:
            result = 0
        elif cnt == 3:
            result = 5
        elif cnt == 4:
            result = 4
        elif cnt == 5:
            if bonus_number not in numbers:
                result = 3
            else:
                result = 2
        elif cnt == 6:
            result = 1

        lotto_paper.append([sorted(numbers), result])

        context = {
            'lotto_paper' : lotto_paper,
        }
    print(context)

    return render(request, 'lotto.html', context)
