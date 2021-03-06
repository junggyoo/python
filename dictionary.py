#딕셔너리(dictionary)
딕셔너리는 단어 그대로의 '사전'과 같이 별도로 정의한 키(key)를 통해 각 요소에 접근할 수 있또록 만들어진
데이터 타입입니다.

사전에서 단어를 가지고 그 단어의 설명을 찾을 수 있듯이, 딕셔너리에서는 키(key)를 가지고 그 키에 해당하는
값(value)을 찾을 수 있는 것입니다.

#딕셔너리 선언하기
딕셔너리는 중괄호({})로 감싸서 선언하며, 딕셔너리의 각 요소(element)들은 쉼표(,)를 사용하여 구분합니
다. 이러한 딕셔너리의 요소는 또다시 키(key)와 값(value)의 한 쌍으로 구성되며, 이 둘은 콜론(:)으로
연결됩니다.

BTS = {
    '진': {
        '본명': '김석진',
        '생년월일': '1992년 12월 4일'
    },
    '슈': {
        '본명': '민윤기',
        '생년월일': '1993년 3월 9일'
    },
    '제이홉': {
        '본명': '정호석',
        '생년월일': '1999년 2월 18일생'
    },
    'RM': {
        '본명': '김남준',
        '생년월일': '1994년 9월 12일'
    },
    '지민': {
        '본명': '박지민',
        '생년월일': '1995년 10월 13일'
    },
    '뷔': {
        '본명': '김태형',
        '생년월일': '1995년 12월 30일'
    },
    '정국': {
        '본명': '전정국',
        '생년월일': '1997년 9월 1일'
    }
}

print(BTS['뷔']['본명'])
