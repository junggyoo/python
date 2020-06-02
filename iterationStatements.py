#반복문(iteration statements
현실 세계의 많은 문제들은 대체로 반복적인 형태를 하고 있는 것이 많습니다. 이것은 곧 어떤 조건을 만족시킬
때까지 특정 행동을 지속적으로 반복해서 수행해야 한다는 의미입니다.
프로그래밍에서 이러한 반복 작업은 단순히 소스 코드를 반복해서 작성해도 원하는 결과를 얻을 수 있습니다.

하지만 함수의 호출이 몇 번 안 되면 모르겠지만 만약 이와 같은 함수의 호출이 1억번 이상 수행되어야 한다면
해당 소스 코드의 길이는 굉장히 길어지게 되고 가독성 또한 매우 나빠지게 될 것입니다.

따라서 파이썬을 비롯한 대부분의 프로그래밍 언어에서는 반복해서 특정 명령이나 연산을 수행해야 할 경우 사용
할 수 있도록 반복문이라는 것을 제공하고 있습니다. 반복문(iteration statements)이란 프로그램 내에서
똑같은 명령을 일정 횟수만큼 반복하여 수행하도록 제어해 주는 명령문을 의미합니다.

while 문
파이썬에서 사용할 수 있는 가장 간단한 반복문은 while 문입니다.
while 문은 조건식이 특정 조건을 만족할 때까지 계속해서 명령문을 반복 실행합니다.

파이썬에서 while 문은 다음과 같은 방식으로 사용할 수 있습니다.
while 조건식:
    조건식의 결과가 참(True)인 동안 반복적으로 실행되는 명령문

while 문을 만난 프로그램은 가장 먼저 조건식의 결과가 참(True)인지를 검사합니다. 만약 조건의 결과가
참(True)이라면 프로그램의 흐름은 while 문 내부로 진입하며, 만약 결과가 거짓(False)이라면 while 문
에 진입하지 않고 건너뛰게 됩니다.

while 문 내부로 진입한 프로그램은 내부에 포함된 모든 명령문을 실행하고 나서 또다시 조건식을 검사합니다.
이렇게 조건식을 검사하고 명령문을 모두 수행한 후 또다시 조건식을 검사하는 모양이 마치 고리와 같다고 하여
반목문을 루프(loop)라고도 부릅니다.

i = 1
while i < 11: #조건식
    print("파이썬 " + str(i))
    i = i + 1 #탈출 조건
#무한 루프(infinite loop)
while 문의 동작에서 가장 중요한 것이 바로 조건식의 결과를 변경하는 명령문입니다.
while 문에 진입하기 위해서는 조건식의 결과가 참(True)이어야 하는데, 이러한 조건식의 결과를 변경하는
명령문(탈출조건)이 while 문 내부에 존재하지 않는다면, 조건식의 결과는 언제나 참(True)으로 고정되므로
while 문은 영원히 반복될 것입니다.

이렇게 영원히 반복되는 반복문을 무한 루프(infinite loop)라고 부르며, 무한 루프에 빠진 프로그램은 영
원히 종료되지 않습니다.

반복문을 작성할 때 가장 많이하는 실수가 바로 루프를 탈출하기 위한 명령문을 실수로 작성하지 않거나 조건식을
원하는 대로 변경하는데 실패하는 경우입니다. 이처럼 의도치 않게 발생한 무한 루프는 해당 프로그램을 정상적인
방법으로는 끝낼 수 없게 만들며, 결국에는 해당 프로그램뿐만 아니라 프로그램을 돌리는 컴퓨터까지 멈추게 만들
수 있습니다. 따라서 while 문과 같은 반복문을 작성할 때는 조건식의 결과가 어느 순간에는 거짓(False)으
로 변경되도록 반드시 탈출 조건을 포함시켜야 합니다.

이처럼 무한 루프는 특별히 의도한 경우가 아니라면 반드시 피해야 하는 상황이지만, 프로그램을 만들다보면 상황
에 따라 의도적으로 무한 루프를 사용하는 경우도 생깁니다. 파이썬에서는 무한 루프를 다음과 같이 의도적으로
만들 수 있으며, 이때는 탈출 조건에 도욱 신경 써야 합니다.

while True:
    반복적으로 실행하고자 하는 명령문

#for 문
while 문은 구조상 while 문 내부에 조건식의 결과를 변경하는 명령문을 삽입해야하기 때문에 종종 실수를
하게 됩니다. 하지만 for 문은 이러한 조건식의 결과를 변경하는 명령문을 따로 사용하지 않고도 튜플이나 리스
트, 문자열 등을 원하는 횟수만큼 반복할 수 있도록 해줍니다.

문법
for 변수 in 문자열(or 튜플 or 리스트):
    반복적으로 실행하고자 하는 명령문

for 문을 만난 프로그램은 우선 in 키워드가 가리키는 문자열, 튜플 또는 리스트의 첫 번째 요소를 꺼내 변수
에 대입합니다. 이렇게 대입된 변수는 for 문 내부의 명령문에서 자유롭게 사용할 수 있습니다.

for 문 내부의 모든 명령문을 수행하고 나면 또다시 해당 문자열, 튜플 또는 리스트로 돌아가 다음 요소가 있
는지를 검사합니다. 만약 다음 요소가 존재한다면 해당 요소를 변수에 대입하고 또다시 루프를 실행하며, 만약
다음 요소가 존재하지 않는다면 for 문은 종료됩니다.

이처럼 for 문은 대상이 되는 문자열, 튜플, 또는 리스트의 길이만큼만 손쉽게 반복문을 수행할 수 있습니다.
for 문에서 선언된 변수는 for 문 내부에서만 사용할 수 있으며, for 문이 종료되면 사용할 수 없습니다.

str = "hello world"
for ch in str:
    print(ch)

#range() 함수
파이썬에서 for 문과 함께 가장 많이 사용되는 함수는 바로 range()함수일 것입니다.
range() 함수는 전달된 안수에 따라 연석된 정수들을 반환하는 함수로, 전달되는 인수의 수에 따라 다음과 같
이 두 가지 방식으로 사용할 수 있습니다.

문법
1. range(마지막정수)
2. range(시작정수, 마지막정수)

첫 번째 방식처럼 인수가 하나만 전달될 경우에는 0부터 (마지막정수-1)까지 1씩 증가하는 연속된 정수들을
반환합니다.
이때 전달되는 인수가 음의 정수이면 아무런 정수도 반환하지 않습니다.

range(5) #0, 1, 2, 3, 4
range(10) #0, 2, 3, 4, 5, 6, 7, 8, 9
range(-3) #

만약 두 번째 방식처럼 인수가 두 개 전달될 경우에는 시작정수부터 (마지막정수-1)까지 1씩 증가하는 연속된
정수들을 반환합니다.

range(2, 5) #2, 3, 4
range(-3, 5) #-3, -2, -1, 0, 1, 2, 3, 4
range(-7, -2) #-7, -6, -5,-4, -3

다음 예제는 for 문과 range() 함수를 사용하여 구구단을 출력하는 예제입니다.

for col in range(2, 10):
    for row in range(1, 10):
        print(col, " x ", row, " = ", col * row)

위의 예제처럼 for 문 안에 또 다른 for 문을 중첩하여 사용함으로써 문제를 간결하게 표현할 수 있습니다.
하지만 for 문의 무리한 중첩 사용은 프로그램의 실행 속도에 큰 영향을 줄 수 있으므로, 사용할 때 세심한 주
의가 필요합니다.

#break 키워드로 반목문 탈출하기
반목문을 통해 명령문을 반복해서 수행하다보면 프로그램의 흐름상 특정 조건을 만족할 때 더이상 반복문을 수행
하지 않고 그 즉시 해당 반목문을 빠져나가야 할 경우가 생깁니다. 이러한 경우에는 break 키워드를 사용하여
반복 조건에 상관없이 가장 가까운 반복문을 즉시 탈출할 수 있습니다.

다음 예제는 구구단을 5단까지만 출력하도록 한 에제입니다.

for col in range(2, 10):
    if col > 5:
        break
    for row in range(1, 10):
        print(col, " x ", row, " = ", col * row)

#continue 키워드로 처음으로 되돌아가기
break 키워드가 해당 반목문 전체를 빠져나가게 해준다면, continue 키워드는 해당 루프만을 즉시 종료하고
다음 루프를 실행시킵니다.
즉, continue 키워드는 해당 키워드 바로 다음 명령문부터 해당 반목문의 마지막 명령문까지를 모두 건너뛰고
바로 다음 반목문을 실행하는 것입니다.

다음은 1부터 10까지의 정수 중 홀수만을 출력하는 예제입니다.

for n in range(1, 11):
    if n % 2 == 0:
        continue
    print(n, "은 홀수입니다")

위의 예제 2번 라인의 if문에서 변수 n을 2로 나눈 나머지가 0인 경우는 n이 짝수인 경우입니다. 즉, n이
짝수이면 그 즉시 해당 반복을 중지하고 n의 크기를 1 증가시킨 후 2번 라인부터 다시 조건식을 검사하게
됩니다. 