#-*- coding:utf-8 -*-
import grade_data as d
import sys

from math import sqrt
#==================================================================================================
# person1과 person2의 그레디언트 거리 계산
def sim_distance(prefs, person1, person2):
    si = dict()

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    sum_of_squares = sum([(prefs[person1][item] - prefs[person2][item])**2 for item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sqrt(sum_of_squares))

#==================================================================================================

def sim_pearson(prefs, p1, p2):
    si = dict() # 같이 평가한 항목들의 목록을 구함

    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si) # 공통 항목 갯수

    # 공통 항목이 없으면 0
    if n == 0:
        return 0

    # 모든 선호도 합 계산
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # 제곱의 합 계산
    sum1Sq = sum([(prefs[p1][it])**2 for it in si])
    sum2Sq = sum([(prefs[p2][it])**2 for it in si])

    # 곱의 합 계산
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # 피어슨 점수 계산
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n) * (sum2Sq-pow(sum2,2)/n))
    if den==0:
        return 0

    r = num/den

    return r

#==================================================================================================
# 선호도 dict를 사용하여 평가 유사도가 높은 상대편을 구함
def top_match(prefs, person, n=5, similarity=sim_pearson):
    scores = [ (similarity(prefs, person, other), other) for other in prefs if other!=person ]

    scores.sort()
    scores.reverse()
    return scores[:n]

#==================================================================================================
# 다른 사람과의 순위의 가중 평균값을 이용해서 특정 사람을 추천
def get_recommendations(prefs, person, similarity=sim_pearson):
    total = dict()
    sim_Sum = dict()

    for other in prefs:
        if other == person:
            continue
        sim = similarity(prefs, person, other)  #person과 other 사이의 유사도 점수를 구함

        # 0 이하 점수는 무시
        if sim <= 0:
            continue

        # other가 평가한 데이트 장소
        for item in prefs[other]:
            # 내가 평가하지 않은 장소만을 대상으로 함
            if item not in prefs[person] or prefs[person][item] == 0:
                # 유사도*점수
                total.setdefault(item, 0)
                total[item] += prefs[other][item]*sim  # other가 평가한 영화의 점수 * person과 other의 상관계수
                # 유사도 합계
                sim_Sum.setdefault(item, 0)
                sim_Sum[item] += sim

    # 정규화된 목록 생성
    ranking = [ (total/sim_Sum[item], item) for item, total in total.items() ]

    # 정렬된 목록 리턴
    ranking.sort()
    ranking.reverse()

    return ranking

#==================================================================================================
# 결과값 출력

print("추천 데이트 장소 추출 완료")

sys.stdout=open('recommend.txt', 'a') # 결과값을 텍스트파일로 저장

place_grade_rank=0
print("★선호장소가 유사한 회원★")

for score, other in top_match(d.grade, "기원"):
    place_grade_rank = place_grade_rank + 1
    print(place_grade_rank, "순위", other, "(", round(score, 2), ")")

print()

recommend_grade_rank = 0
print("★추천 데이트장소★")

for score, item in get_recommendations(d.grade, "기원", similarity=sim_distance):
    recommend_grade_rank = recommend_grade_rank + 1
    print(recommend_grade_rank, "순위", item, "(", round(score,2), ")")



