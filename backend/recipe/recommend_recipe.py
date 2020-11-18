import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "save_your_ingredient.settings")
django.setup()

from random import shuffle
import datetime
from dateutil.parser import parse as dateparse
import datetime as pydatetime
import json

from recipe.models import Recipe
from stock.models import Stock


# list to json
def list_to_json(list):
    lst = []
    for pn in list:
        d = {}
        d["id"] = pn
        lst.append(d)
    return json.dumps(lst)


# 사용자 재고 리스트 가져오기 => 이건 이제필요없어짐
def get_stock_list():
    all_stock = Stock.objects.all() # filter 넣어야함: .objects.filter(author=request.user)
    stock_list = []
    for stock in all_stock:
        stock_list.append(stock.ingredient_id.id)
    return stock_list


# 재료 기반 레시피 추천
def recommend_ingredient(my_stock):
    all_recipes = Recipe.objects.all()
    recommend_recipe_id_list = []
    this_stock = my_stock
    stock_list = []
    for stock in this_stock:
        stock_list.append(stock.ingredient_id.id)
    # print(stock_list)
    for recipe in all_recipes:
        if not(recipe.ingredient_ids):
            continue
        ss = recipe.ingredient_ids.split(',')
        re_list = []
        for s in ss:
            re_list.append(int(s))
# 재고에 있는 재료를 모두 사용해서 만들 수 있는 요리부터 추천
        if len(re_list) != 0 and len(set(stock_list) - set(re_list)) == 0:
            if len(recommend_recipe_id_list) < 20:
                recommend_recipe_id_list.append(recipe.reci_id)
    if len(recommend_recipe_id_list) < 10:
        for recipe in all_recipes:
            if not (recipe.ingredient_ids):
                continue
            ss = recipe.ingredient_ids.split(',')
            re_list = []
            for s in ss:
                re_list.append(int(s))
            if len(re_list) != 0 and 0 < len(set(stock_list) - set(re_list)) < 2:  # and len(set(re_list) - set(stock_list)) < 10:
                if len(recommend_recipe_id_list) < 20:
                    recommend_recipe_id_list.append(recipe.reci_id)
    if len(recommend_recipe_id_list) < 10:
        for recipe in all_recipes:
            if not (recipe.ingredient_ids):
                continue
            ss = recipe.ingredient_ids.split(',')
            re_list = []
            for s in ss:
                re_list.append(int(s))
            if len(re_list) != 0 and 1 < len(set(stock_list) - set(re_list)) < 3:
                if len(recommend_recipe_id_list) < 20:
                    recommend_recipe_id_list.append(recipe.reci_id)
    result = {}
    result['ids'] = recommend_recipe_id_list
    return result


def parse_korean_type_date(d, assert_min_year=1900):
    """
    날짜문자열(년도가 앞, 일자가 뒤 형태)을 입력받아 datetime 인스턴스를 반환
    파싱이 불가능한 경우 또는 assert_min_year년도 이전인 경우 None 반환
    """
    try:
        d_parsed = dateparse(d, yearfirst=True, dayfirst=False)
        if d_parsed.year < assert_min_year: # 보장해야하는 최소 년도보다 작은 경우 None 반환
            return None
        else:
            return d_parsed
    except: # 파싱이 불가능한 경우 None 반환
        return None


def get_time_diff(start_date, end_date, unit='second'):
    """
    datetime 인스턴스의 시작과 종료일자를 받아 시간차이를 반환
    unit이 day인 경우 일수 차이 반환
    unit이 second 등일 경우 초 차이 반환
    """
    assert isinstance(start_date, pydatetime.datetime), 'start_date required datetime instance'
    assert isinstance(end_date,   pydatetime.datetime), 'end_date   required datetime instance'
    _timedelta = end_date - start_date
    if unit=='day':
        return abs(_timedelta.days)
    return abs((_timedelta.days * (_timedelta.max.seconds + 1)) + _timedelta.seconds)


# 유통기한 기반 레시피 추천
def recommend_expiration_date(my_stock):
    now = datetime.datetime.now()
    nowDates = now.strftime('%Y-%m-%d')
    nowDate = nowDates.replace('-', '')
    this_stock = my_stock
    # print(all_stocks)
    expiration_list = []
    for stock in this_stock:
        # print(stock.expiration_date, type(stock.expiration_date))
        stock_time = str(stock.expiration_date).replace('-', '')
        ex_day = get_time_diff(parse_korean_type_date(nowDate), parse_korean_type_date(stock_time), unit='day')
        if ex_day < 5:
            expiration_list.append(stock.ingredient_id.id)
    # print(expiration_list)

    recommend_recipe_list = []
    all_recipes = Recipe.objects.all()
    for recipe in all_recipes:
        if not(recipe.ingredient_ids):
            continue
        ss = recipe.ingredient_ids.split(',')
        re_list = []
        for s in ss:
            re_list.append(int(s))
            # 유통기한이 얼마 안남은 재고가 모두 포함되는 레시피들을 담자
        if len(re_list) != 0 and len(set(expiration_list) - set(re_list)) == 0:
            if len(recommend_recipe_list) < 20:
                recommend_recipe_list.append(recipe.reci_id)
                # 리스트에 10개도 안담겼다면 유통기한이 얼마 안남은 재고중 하나를 제외하고 만들수 있는 레시피들을 추가로 담자
        if len(recommend_recipe_list) < 10:
            for recipe in all_recipes:
                if not (recipe.ingredient_ids):
                    continue
                ss = recipe.ingredient_ids.split(',')
                re_list = []
                for s in ss:
                    re_list.append(int(s))
                if len(re_list) != 0 and len(set(expiration_list) - set(re_list)) == 1:
                    if len(recommend_recipe_list) < 20:
                        recommend_recipe_list.append(recipe.reci_id)
    result = dict()
    result['ids'] = recommend_recipe_list

    return result

# 랜덤으로 레시피 추천(만개의 레시피에서 인기레시피 100을 가져오면 우리가 파싱해온 레시피중에 없는게 있을수도 있어서 걍 랜덤으로 받음요)
def recommend_random():
    my_qset = Recipe.objects.all()
    my_list = list(my_qset)
    shuffle(my_list)
    recommend_recipe_list = []
    for item in my_list[:20]:
        print(item.reci_id)
        recommend_recipe_list.append(item.reci_id)
    result = dict()
    result['ids'] = recommend_recipe_list
    return result