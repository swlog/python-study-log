# ex3- 초를 분과 초로 바꾸기
# 어떤 영상의 재생 시간이 250초입니다. 이 250초는 몇 분 몇 초 인지 계산해서 출력해 보세요.

total_sec = 250
m = total_sec//60
sec = total_sec%60

print(f"{m}분 {sec}초")