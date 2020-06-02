#문자열 타입(text sequence types):str
문자열(string)이란 문자로 이루어진 데이터의 집합을 의미하며, 파이썬에서는 다음과 같이 다양한 방법으로
문자열을 표현할 수 있습니다.

1. 큰따옴표(" ")로 감싸기
2. 작은따옴표(' ')로 감싸기
3. 큰따옴표 3개(""" """)로 감싸기
4. 작은따옴표 3개(''' ''')로 감싸기

큰따옴표와 작은따옴표의 용법상 차이는 전혀 없으며, 이 두 가지 따옴표를 모두 사용하는 이유는 문자열 내에서
따옴표를 정확히 표현하기 위함입니다.
하지만 따옴표가 등장하는 순서에 따라 정확하게 사용하지 않으면 예상치 못한 문제가 발생할 수 있으므로,
그 사용에 주의를 기울여야 합니다.

#여러 줄의 문자열 표현하기
큰따옴표나 작은따옴표 3개를 연속해서 사용하면 여러 줄의 문자열을 그대로 표현할 수 있습니다.

print("""큰따옴표 3개는
여러 줄의 문자열을 표현할 때
사용합니다.""")

#문자열끼리의 연산
파이썬에서는 숫자처럼 문자열끼리 서로 더하거나 문자열에 숫자를 곱할 수도 있습니다. 문자열끼리의 더하기(+)
연산은 두 문자열을 서로 연결시켜주며, 문자열과 정수의 곱하기(*)연산은 해당 문자열을 정수배만큼 반복해서
연걸해 줍니다.

i = "파이썬 "
j = "문자열"

print(i + j)
print(i * 3)

#문자열에서 문자 선택하기
문자열은 문자들의 연속된 집합이라고 볼 수 있습니다. 따라서 파이썬에서는 문자열 내에서 특정 위치의 문자를
손쉽게 선택할 수 있도록 다음 예제와 같이 문자열을 문자들의 배열로 다룰 수 있게 해줍니다.

py = "파이썬으로 코딩을 배우자!"

print(py[0])    #파
print(py[6])    #코
print(py[-1])   #!
print(len(py))  #14

위 예제의 3번 라인처럼 문자열의 첫 번째 문자의 인덱스(index)는 0부터 시작해서 1씩 증가되며, 이때 띄어
쓰기(white space)도 하나의 문자로 취급됩니다. 파이썬에서는 음의 인덱스도 지원하며, 음의 인덱스는 문자
열의 마지막 문자를 -1로 놓고 역순으로 증가하게 됩니다.

대부분의 프로그래밍 언어에서는 한글과 영문자의 크기가 서로 다르게 취급되는데, 파이썬에서는 한글과 영문자의
크기를 동일하게 취급합니다.

#문자열 자르기
문자열을 다루다보면 문자열의 일부분만을 사용하거나 문자열의 일부만을 변경해야 할 경우가 생깁니다. 이러한
경우 손쉽게 처리할 수 있도록 파이썬에서는 문자열의 일부분을 잘라 반환해주는 문자열 슬라이싱(slicing)을
지원하고 있습니다.

py = "우리집 강아지 이름은 멍멍입니다."

print(py[4])
print(py[4:7])
print(py[:4])
print(py[4:])

위 예제의 4번 라인처럼 콜론(:)기호를 사용하면 문자열의 일부만을 자를 수 있으며, 이때 콜론의 앞쪽에 위치
한 인덱스부터 콜론의 뒤쪽에 위치한 인덱스 바로 앞 문자까지를 반환합니다.
이처럼 콜론의 앞쪽에 위치한 인덱스는 곧바로 시작 인덱스가 되지만, 클론 뒤쪽에 위치한 인덱스는 해당 인덱스
에서 1을 뺀 인덱스가 마지막 인덱스가 됩니다.

#특정 문자의 개수 및 위치
count() 함수는 해당 문자열에 인수로 전달받은 문자가 모두 몇 개 포함되어 있는지를 확인하여 반환합니다.
또한, find()나 index()함수를 사용하면, 해당 문자열에 인수로 전달받은 문자가 처음으로 등장하는 인덱스
(index)를 알 수 있습니다.

py = "python programming"

print(py.count('p'))

print(py.find('o'))
print(py.index('o'))

print(py.find('z'))
print(py.index('z'))

위 예제에서 find()와 index()함수의 결과는 동일하게 4로 출력됩니다.
이 두 함수의 차이점은 해당 문자열에 포함되어 있지 않은 문자를 검색할 때 나타납니다.
find()함수는 해당 문자열에 전달받은 문자가 포함되어 있지 않으면 -1을 반환하지만.
index()함수는 ValueError를 발생시키며 프로그램을 강제 종료합니다.

따라서 index()함수를 사용할 때는 반드시 전달받은 문자가 해당 문자열에 포함되어 있는지를 먼저 확인하고
사용해야 합니다.

#문자열의 대소문자 변환
upper()함수는 문자열의 모든 문자를 대문자로 변환해주며, lower()함수는 문자열의 모든 문자를 소문자로
변환시켜 줍니다.

py = "Python"

print(py.upper())   #PYTHON
print(py.lower())   #python
print(py)           #Python

#문자열 변경하기
replace()함수는 첫 번째 인수로 전달된 문자열을 해당 문자열에서 찾아 두 번째 인수로 전달된 문자열로 변
경해 줍니다. 이때 해당 문자열에서 첫 번째 인수로 전달된 문자열을 찾을 수 없으면, 원본 문자열을 그대로 반
환합니다.

py = "파이썬 공부는 너무 재밌어요!"

print(py.replace("파이썬", "자바"))    #자바 공부는 너무 재밌어요!
print(py)                           #파이썬 공부는 너무 재밌어요!

#문자열 나누기
split()함수는 전달받은 문자를 기준으로 해당 문자열을 여러 개의 부분 문자열로 나누어 하나의 리스트로 반
환합니다.

py = "파이썬 공부는 너무 재밌어요!"

print(py.split(' '))    #['파이썬', '공부는', '너무', '재밌어요!']
print(py.split())       #['파이썬', '공부는', '너무', '재밌어요!']

위 예제는 문자열 py를 띄어쓰기를 기준으로 나누고 있습니다. 또한 split()함수에 아무런 인수도 전달하지
않으면, 자동으로 띄어쓰기나 탭 문자, 줄바꿈 문자 등과 같은 공백(white space)를 기준으로 문자열을 나누
게 됩니다. 