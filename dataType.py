#데이터 타입
변수뿐만 아니라 프로그램에 사용되는 모든 데이터에도 타입이 존재합니다. 데이터 타입(data type,자료형)
이란 해당 데이터가 메모리에 어떻게 저장되고, 프로그램 내에서 어떻게 처리되어야 하는지를 명시적으로
알려주는 역할을 합니디ㅏ.

파이썬에서는 다음과 같은 기본 데이터 타입을 제공하고 있습니다.
1. 숫자형 타입(numberic types)
2. 불리언 타입(boolean types)
3. 문자열 타입(text sequence types)

이외에도 리스트(list)와 튜플(tuple), 집합(set), 딕셔너리(dict), 등과 같은 타입 등의 복잡한
데이터 타입도 존재한다.

#숫자형 타입(numberic types):int, float
숫자형 타입이란, 1, 2, 3.14와 같이 숫자의 형태로 이루어진 데이터 타입을 의미합니다.
이중에서 1과 2와 같이 소수점이 없는 숫자형 데이터를 정수형(integer)타입이라고 하며, 3.14와 같이
소수점을 가지고 있는 숫자형 데이터를 실수형(floating-point)타입이라고 합니다.

클래스(class)란 객체 지향 프로그래밍에서 객체(object)를 만들어 내기 위한 일종의 설계도라 할 수 있
으며, 객체(object)란 실생활에서 우리가 인식할 수 있는 사물로 설명할 수 있습니다.

#산술 연산자(arithmetic operator)
숫자형 데이터끼리는 더하기(+), 뺴기(-), 곱하기(*), 나누기(/)와 같은 산술 연산자를 사용하여 사칙연산을
수행할 수 있습니다.

파이썬에서 정수형 데이터끼리의 나눗셈을 제외한 사칙 연산은 언제나 정수형 데이터를 결과로 반환하며,
실수형 데이터끼리의 사칙 연산은 언제나 실수형 데이터를 결과로 반환합니다. 단, 정수형 데이터끼리의 나눗셈의
결과는 정수형이 아닌 실수형으로 반환됨으로 이 점 주의해야 합니다.
마지막으로 실수형 데이터와 정수형 데이터 사이의 사칙 연산은 언제나 실수형 데이터를 결과로 반환합니다.

나눗셈의 몫을 실수가 아닌 정수로 얻고 싶다면 나눗셈(/) 연산자가 아닌 몫(//) 연산자를 사용해야 합니다.
또한, 나눗셈의 나머지를 얻고 싶을 때에는 나머지(%) 연산자를 사용하면 됩니다. 
