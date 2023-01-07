{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9e78740d-e1e0-479d-9b4d-c3c54dd8de8e",
   "metadata": {},
   "source": [
    "# [문자열안에 문자열](https://school.programmers.co.kr/learn/courses/30/lessons/120908)\n",
    " - lv0, python3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "645859e7-b49a-4fb9-a38a-38dcd4908c65",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(str1, str2):\n",
    "    if str2 in str1:\n",
    "        answer = 1\n",
    "    else : \n",
    "        answer =2\n",
    "# 1줄\n",
    "\n",
    "# 1 if str2 in str1 else 2\n",
    "    return answer\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "307a081d-b6fc-41dd-9633-d030452d6a0c",
   "metadata": {},
   "source": [
    "# [옷 가게 할인 받기](https://school.programmers.co.kr/learn/courses/30/lessons/120818)\n",
    " - lv0, python3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "de50eca7-25c9-4d3e-b2fb-0c2bf97ee264",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(price):\n",
    "    if price>=500000:\n",
    "        price = price *0.8\n",
    "    elif price>=300000:\n",
    "        price = price *0.9\n",
    "    elif price>=100000:\n",
    "        price = price * 0.95\n",
    "    return int(price)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "609c098f-0287-4377-86a1-362ee8e7ba7d",
   "metadata": {},
   "source": [
    "# [제곱수 판별하기](https://school.programmers.co.kr/learn/courses/30/lessons/120909)\n",
    "- Lv0, python3\n",
    "- idea\n",
    "    - 제곱수의 경우 나누는 수와 몫이 같다! \n",
    "    - another : 제곱수의 경우 제곱근이 Int이다!!!!!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "13190edf-33cf-4dbf-ab2c-b885eb666b41",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n):\n",
    "    for i in range(1,n+1):\n",
    "        if n/i == i : ## //을 쓰지 말것\n",
    "            return i\n",
    "    return 2\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4489ca60-7266-4f30-9d08-a7fba1254f8d",
   "metadata": {},
   "source": [
    "# [배열의 유사도](https://school.programmers.co.kr/learn/courses/30/lessons/120903)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - set 복습\n",
    "     - 문제의 제한 사항에서 중복된 원소를 가지고 있지 않다를 이용해 발상"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "49368569-4395-45f2-98ed-6d85422b6e6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(s1, s2):\n",
    "    return len(set(s1).intersection(s2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fff4b454-4f2a-4471-9023-5b7db45b2d9c",
   "metadata": {},
   "source": [
    "# [자릿수 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/120906)\n",
    "- Lv0, python3\n",
    "- idea\n",
    "    - 문자열화 하면 하나의 리스트가 됨. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9aa38aac-56bc-494a-8a4a-ab04586b3fea",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n):\n",
    "    answer = sum([int(i) for i in str(n)])\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa2f2b2f-522a-49d9-9282-6e0531d068ae",
   "metadata": {},
   "source": [
    "# [순서쌍의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/120836)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 숫자를 하나씩 나눠보아도 최대 N까지만 나누면 된다\n",
    "     - 즉 1부터 N 까지 나누었을때 나머지가 0 인것들의 갯수를 찾아주면 된다 -> 약수의 개념"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "91c923ed-0e96-40fd-9063-81bc758ec96f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n):\n",
    "    answer = 0\n",
    "    for i in range(1,n+1):\n",
    "        if n%i ==0:\n",
    "            answer +=1\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0086c25e-65c3-45f0-922d-a041baec4e66",
   "metadata": {},
   "source": [
    "# [숨어있는 숫자의 덧셈(1)](https://school.programmers.co.kr/learn/courses/30/lessons/120851)\n",
    "- Lv0 ,python3\n",
    "- iead\n",
    "    - Str list 배열\n",
    "    - try/ except 사용"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "65fdee1f-edf2-433f-9753-77725c49560e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(my_string):\n",
    "    answer = 0\n",
    "    for i in my_string:\n",
    "        try:\n",
    "            answer += int(i)\n",
    "        except:\n",
    "            pass\n",
    "\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d69f87fd-a936-4bbe-85e0-8ad39059cb2d",
   "metadata": {},
   "source": [
    "# [모음 제거](https://school.programmers.co.kr/learn/courses/30/lessons/120849)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "    - 내포이용\n",
    "    - method.2 replace 이용해보자. \n",
    "    `'변수. replace(old, new, [count])' `\n",
    "    - 주의) replce 함수 공부 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "d89c19b6-1fc4-4022-8b26-f0f6ac7309a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(my_string):\n",
    "    rm_string = ['a','e','i','o','u']\n",
    "    answer = [i for i in my_string if i not in rm_string]\n",
    "    return ''.join(answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "57706a8d-ff74-4c84-96b7-6dffe3bf885c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(my_string):\n",
    "    rm_string = ['a','e','i','o','u']\n",
    "    for i in rm_string:\n",
    "        my_string = my_string.replace(i,'')\n",
    "    return my_string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "82aaf0db-a1e7-4d39-80df-b7660623b64c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'nc t mt y'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution(my_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "62a66367-8b12-4fef-98c4-59725bba1b82",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_string = \"nice to meet you\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "87da74e7-1d08-4541-b1fc-ad1748a7c2eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'nce to meet you'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_string.replace('i','')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5b7b6b14-ef73-4232-82ad-c3a53c9bbb2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'nice to meet you'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_string # 객체가 저장되지 않음"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "722d5e8f-15fe-4d07-ba7b-af762be9cc13",
   "metadata": {},
   "source": [
    "# [개미 군단](https://school.programmers.co.kr/learn/courses/30/lessons/120837)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 공격력이 큰 개미의 병력 배치를 우선\n",
    "         - 즉 장군개미의 병력을 우선 배치 -> 전체 Hp//장군개미\n",
    "         - Hp-(장군개미)//병정개미 = (hp/5)의 나머지를 /3\n",
    "         - Hp-(장군)-(병정)//일개미 (hp/5)의 나머지의 /3 의 나머지\n",
    "         - 각 몫의 합!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "05758eea-d3bb-4bb4-9c72-d819684898a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(hp):\n",
    "    answer = 0\n",
    "    answer += hp//5\n",
    "    hp -= (hp//5)*5\n",
    "    answer += hp//3\n",
    "    hp -= (hp//3)*3\n",
    "    answer += hp//1\n",
    "    \n",
    "    return answer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "59e35aa2-4b1d-4646-ae66-81e14c62a01d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 나머지를 이용해서\n",
    "def solution(hp):\n",
    "    answer = ((hp//5) + ((hp%5)//3) + ((hp%5)%3))\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76592354-664e-4129-86c9-60fea59aa64e",
   "metadata": {},
   "source": [
    "# [세균 증식](https://school.programmers.co.kr/learn/courses/30/lessons/120910)\n",
    " - Lv 0, python3\n",
    " - idea\n",
    "     - 2의 t승"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "41e310b6-9ef3-40d4-be04-af74215c7d77",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n, t):\n",
    "    return n*(2**t)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11781a45-4751-4dc0-b1dd-25c1104edb56",
   "metadata": {},
   "source": [
    "# [n의 배수 고르기](https://school.programmers.co.kr/learn/courses/30/lessons/120905)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 배수는 반대로 말하면 약수 -> 나누어 떨어지는 수 \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "6a53a59e-f2e1-40d6-a426-5d83b1b18cf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n, numlist):\n",
    "    answer = [i for i in numlist if i%n ==0]\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7141000-586c-4238-be89-d0ff6ce79ebc",
   "metadata": {},
   "source": [
    "# [직각삼각형 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/120823)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - str에 `*` 연산자를 취하면 해당 횟수 만큼 만복"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "b5f13243-d561-48b3-ac96-fec61d7c02de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*\n",
      "**\n",
      "***\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "for i in range(1, n+1):\n",
    "    print('*'*i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5f36c3d-0f7b-4f67-8b5a-452546590135",
   "metadata": {},
   "source": [
    "# [대문자와 소문자](https://school.programmers.co.kr/learn/courses/30/lessons/120893)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 내장함수 islower()\n",
    " - 다른 사람 풀이\n",
    "     - swapcase() : 영문 대/소 문자의 상호전환"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "ee81d885-d93a-4fd7-87a1-e862e216ea64",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(my_string):\n",
    "    answer = []\n",
    "    for i in my_string:\n",
    "        if i.islower():\n",
    "            answer.append(i.upper())\n",
    "        else:\n",
    "            answer.append(i.lower())\n",
    "            \n",
    "    \n",
    "    return ''.join(answer)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a7dff61-8a21-4996-9adf-9a9b48901f10",
   "metadata": {},
   "source": [
    "# [암호 해독](https://school.programmers.co.kr/learn/courses/30/lessons/120892)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - slicing/ Stack 활용 `참고 : str list : 슬라이싱도 가능 따라서 리스트화 필요 없다`\n",
    "     - Index는 0번부터\n",
    "         - 시작점은 code-1 부터\n",
    "         - len(cipher)+1 끝까지 : 슬라이싱은 이상,미만(끝까지는 사실 안적어도 됨)\n",
    "         `cipher[code-1::code]`\n",
    "         - stack: 띄어 세는 갯수\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "5b2c9d2b-0aed-4072-9e0a-22a889847f36",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(cipher, code):\n",
    "    cipher = list(cipher)\n",
    "    answer = cipher[code-1:len(cipher)+1:code]\n",
    "    return ''.join(answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "132cb353-6ca6-47c8-ac3a-a3d44bd37ce1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'bdf'"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 'abcdefg'\n",
    "a[1::2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c52c1c81-517f-43d7-ab50-86b99ef0682d",
   "metadata": {},
   "source": [
    "# [가위 바위 보](https://school.programmers.co.kr/learn/courses/30/lessons/120839)\n",
    " - Lv 0, python3\n",
    " - idea\n",
    "     - str 은 합 연산이 가능하다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "8584eb1f-463c-42dd-b663-90c3cc02f771",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(rsp):\n",
    "    answer = ''\n",
    "    for i in rsp:\n",
    "        if i=='2':\n",
    "            answer += '0'\n",
    "        if i == '0':\n",
    "            answer += '5'\n",
    "        if  i == '5':\n",
    "            answer += '2'\n",
    "    \n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d0d7a9ba-979d-4bd7-8fe2-1be1d6654bbd",
   "metadata": {},
   "source": [
    "# [문자열 정렬하기(1)](https://school.programmers.co.kr/learn/courses/30/lessons/120850)\n",
    " -Lv0, python3\n",
    " - idea\n",
    "     - .isdigit() : 정수이면 True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "e6aabd48-4687-4c85-971e-a0af40fd282c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(my_string):\n",
    "    \n",
    "    answer = [int(i) for i in my_string if i.isdigit()]\n",
    "    return sorted(answer)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d98d85b-9e6a-4e7c-bdb9-c1cd4a3fca74",
   "metadata": {},
   "source": [
    "# [주사위 개수](https://school.programmers.co.kr/learn/courses/30/lessons/120845)\n",
    " - Lv0, python3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "2b1ae264-27ec-4ce7-8b51-8faab8d6ed02",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(box, n):\n",
    "    answer = (box[0]//n)*(box[1]//n)*(box[2]//n)\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "248ac978-5722-4bd1-ab17-5ac2f7cd0a10",
   "metadata": {},
   "source": [
    "# [가장 큰 수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/120899)\n",
    " - Lv0, python3\n",
    " - 다른 사람 풀이\n",
    "     - method 이용\n",
    "     - array.index() : 특정한 원소가 몇 번째에 `처음으로` 등장했는지를 알려주는 메소드(즉, 중복이 없는 경우만 사용할 수 있다.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1903545-c906-49d4-9df8-f20006fb8db3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(array):\n",
    "    m_value = array[0]\n",
    "    for m_idx in range(len(array)):\n",
    "        if m_value < array[m_idx]:\n",
    "            m_value = array[m_idx]\n",
    "            idx = m_idx\n",
    "    \n",
    "    return [m_value,idx]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8132cf0-dede-4568-a778-57cb1b4e9513",
   "metadata": {},
   "source": [
    "# [약수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/120897)\n",
    "- Lv0, python3\n",
    "- idea\n",
    "    - 약수는 나누어 떨어진다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c04b18b-d085-402a-84a0-58e483dd1009",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n):\n",
    "    answer = []\n",
    "    for i in range(1,n+1):\n",
    "        if n%i==0:\n",
    "            answer.append(i)\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "f341e28b-10a3-4df3-a104-6040b82a437d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# short cording\n",
    "def solution(n):\n",
    "    return [i for i in range(1, n+1) if n%i==0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d63b83c-605b-419b-b5af-86975422ee6e",
   "metadata": {},
   "source": [
    "# [배열 회전시키기](https://school.programmers.co.kr/learn/courses/30/lessons/120844)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 인덱스를 회전시킴\n",
    "         - 문제) 회전시키고 저장하는 과정에서 문제가 발생 - 새로운 리스트의 필요\n",
    "    - 다른풀이의 내장함수 확인의 필요성\n",
    "    - 내장함수를 이용하지 않고 rotate의 규칙성에 집중할 필요\n",
    "    </br>`\n",
    "def solution(numbers, direction):\n",
    "    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "67299006-48c0-46b9-bc5b-d9504faf0d89",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(numbers, direction):\n",
    "    answer = [0]*len(numbers)\n",
    "    if direction == 'right':\n",
    "        for idx in range(len(numbers)):\n",
    "            if idx == len(numbers)-1:\n",
    "                answer[0] = numbers[-1] \n",
    "            if idx != len(numbers)-1:\n",
    "                answer[idx+1] = numbers[idx]\n",
    "    if direction == 'left':\n",
    "        for idx in range(len(numbers)):\n",
    "            if idx == 0:\n",
    "                answer[-1] = numbers[0]\n",
    "            else:\n",
    "                answer[idx-1] = numbers[idx]\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "f9724a9d-6dca-437b-8774-c7a403fecf4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from collections import deque\n",
    "\n",
    "def solution(numbers, direction):\n",
    "    numbers = deque(numbers)\n",
    "    if direction == 'right':\n",
    "        numbers.rotate(1)\n",
    "    else:\n",
    "        numbers.rotate(-1)\n",
    "    return list(numbers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7833e0c4-fa07-4ae2-80d0-626762da4ce2",
   "metadata": {},
   "source": [
    "# [외계행성의 나이](https://school.programmers.co.kr/learn/courses/30/lessons/120834)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - `list` index의 활용"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "badab42d-b8b0-4538-83cb-569cd2988341",
   "metadata": {},
   "source": [
    "```python\n",
    "list index\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ee8a672f-4ba5-4c56-af52-d1d389e59163",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "a= 0, b=1, c=2, d=3, ... , j=9\n",
    "\n",
    "ex) cd = 23살\n",
    "\n",
    "각 알파벳에 숫자를 변수로 대입\n",
    "\n",
    "'''\n",
    "def solution(age):\n",
    "    age = str(age)\n",
    "    answer = ''\n",
    "    alpha = \"abcdefghij\"\n",
    "    for i in age:\n",
    "        answer += alpha[int(i)]\n",
    "    return answer\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "148c91f9-69e3-4b55-90d8-93d9e5259c3e",
   "metadata": {},
   "source": [
    "# [최댓값 만들기(2)](https://school.programmers.co.kr/learn/courses/30/lessons/120862)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 최댓값이 되려면 양수\n",
    "     - 양수의 가장 큰 값 둘의 곱\n",
    "     - 음수의 가장 큰 값 둘의 곱\n",
    "     - 그 중에서 큰 값 찾기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "82035bf2-4883-47a6-b408-015aadab8c2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(numbers):\n",
    "    # 양수 최대의 곱\n",
    "    numbers = sorted(numbers)\n",
    "    p_mul = numbers[1]*numbers[0]\n",
    "    # 음수 최대의 곱\n",
    "    m_mul = numbers[-1]*numbers[-2]\n",
    "    answer = max(p_mul, m_mul)\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5cd0e9a4-cd28-4f4a-9ecd-5e82e9c3c7e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution([1, 2, -3, 4, -5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9930c23-f4b1-4f62-b4a4-c0d432da435f",
   "metadata": {},
   "source": [
    "# [피자 나눠 먹기(2)](https://school.programmers.co.kr/learn/courses/30/lessons/120815)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - n 명이 6의 배수인 경우\n",
    "     - 6의 배수가 아닌경우 n과 6의 최소공배수를 구하고 그 최소공배수//6의 값을 피자 판수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a8c80abe-cecb-48c9-8e35-9017823a09b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n):\n",
    "    if n%6 == 0:\n",
    "        return n//6\n",
    "    elif n%6 != 0:\n",
    "        for i in range(n*6+1):\n",
    "            if i%6==0 and i%n==0:\n",
    "                gl = i\n",
    "        return gl//6"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c60f84d5-721b-48b5-9fbb-a4618f5a425e",
   "metadata": {},
   "source": [
    "# [인덱스 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/120895) \n",
    " - Lv 0, python3\n",
    " - idea\n",
    "     - list의 index 이용\n",
    "     - 문자열을 list로 보기는 하지만, items 화 하여 사용할 수 없다!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "f53b22c7-5651-4d39-be34-372e6131672b",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "num1, num2 해당 인덱스의 문자를 바꾸자\n",
    "'''\n",
    "def solution(my_string, num1, num2):\n",
    "    my_string = list(my_string)\n",
    "    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]\n",
    "    return my_string"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ffcf0997-3eb7-43be-a4af-cda10a012caa",
   "metadata": {},
   "source": [
    "# [숫자 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/120904) \n",
    " - Lv 0, python3\n",
    " - idea\n",
    "     - 숫자를 문자화 하여 리스트 처럼 사용하자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "8e0399fb-0037-433f-b2e0-c7945d6b5d18",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(num, k):\n",
    "    if str(k) in str(num):\n",
    "\n",
    "        for idx in range(len(str(num))):\n",
    "            if str(num)[idx] == str(k):\n",
    "                return idx+1\n",
    "    else:\n",
    "        return -1\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "89964c79-3c53-46ad-a13d-b7ba6f4bb9ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution(29183,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "6420e7a9-8f97-45c4-9990-778c8c472edf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution(123456,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "c28a4613-c300-4228-9ad0-01fe0243ecea",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 다른 사람 풀이"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "859ca0af-4579-47e7-82d6-96427815905b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(num, k):\n",
    "    for i, n in enumerate(str(num)):\n",
    "        if str(k) == n:\n",
    "            return i + 1\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a55d4d59-e669-423d-8771-49646c36f757",
   "metadata": {},
   "source": [
    "# [3,6,9 게임](https://school.programmers.co.kr/learn/courses/30/lessons/120891)\n",
    "- Lv0, python3\n",
    "- idea\n",
    "    - 문자열 처럼 파악해 하나씩 열거하여 3,6,9 인경우 cnt 를 하나씩 더한다\n",
    "\n",
    "- 다른 사람의 풀이\n",
    "    - method : .count('str') 해당 문자열을 count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "a78bb321-9ec6-4823-8c9c-20d60be263cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(order):\n",
    "    cnt = 0\n",
    "    for i in str(order):\n",
    "        if i in ['3','6','9']:\n",
    "            cnt += 1\n",
    "    return cnt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77821959-e45b-4bba-aef1-9b0471fd0e3f",
   "metadata": {},
   "source": [
    "# [문자열 정렬하기(2)](https://school.programmers.co.kr/learn/courses/30/lessons/120911)\n",
    " - Lv0, python3\n",
    " - tip)\n",
    "     - 하나씩 꺼내서 정렬하지 않아도 된다! "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "1d0678f7-c9a1-4d8b-abc4-0f787fc095e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(my_string):\n",
    "    my_string = [i.lower() for i in my_string]\n",
    "    my_string.sort()\n",
    "    return ''.join(my_string)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "7196e922-63ba-46af-ad74-0401b9598254",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abcd\n"
     ]
    }
   ],
   "source": [
    "a = solution('Bcad')\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a46c51b-9d98-4993-b42f-1193b2fcb5d9",
   "metadata": {},
   "source": [
    "# [합성수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/120846) \n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 약수란 그 숫자를 나누었을때 나누어떨어지는 수들을 약수라고 한다. \n",
    "     - 따라서 나누어 떨어졌을때 생기는 숫자가 3개이상인 수를 걸러내면 된다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "131450da-9eee-4a6e-9cbc-a28e4fe0b6d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "n 이하의 합성수의 개수를 Return 하시오\n",
    "'''\n",
    "def solution(n):\n",
    "    answer = 0\n",
    "    for i in range(1,n+1):\n",
    "        # n 이하의 자연수들의 약수 구하기\n",
    "        measures = [j for j in range(1,i+1) if i%j==0 ]\n",
    "        # i 가 합성수 인지 판별하기\n",
    "        if len(measures) >= 3:\n",
    "            answer += 1\n",
    "    return answer\n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "b56dbc0f-8a2e-4160-bf7f-d71a67b9f3b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "fcd04b62-1f71-400c-afd2-c41d5bf9e634",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution(15)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "184e31f7-b49f-43d9-a1ef-ae260b6149e5",
   "metadata": {},
   "source": [
    "# [중복된 문자 제거](https://school.programmers.co.kr/learn/courses/30/lessons/120888)\n",
    " - Lv0, python3\n",
    " - 즉 unique 한것을 찾으시오\n",
    "     - 중복을 허용하지 않는 set 을 이용해보자 -> 테스트 문자열에서 중복된 순서대로 제거 되지 않는 문제점 발생\n",
    "```\n",
    "string 에서 앞에서 부터 하나 빼고\n",
    "채울 list에 확인 후 넣기\n",
    "그래야 앞에서 부터 채울 수 있다\n",
    "```\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "a2bea2d8-4205-44b2-9ac6-d7095adbdc6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "my_string 에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return 하시오\n",
    "\n",
    "'''\n",
    "\n",
    "def solution(my_string):\n",
    "    my_string = set(my_string)\n",
    "    return ''.join(my_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "795c31da-c756-4c45-a45a-1b58117dda60",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(my_string):\n",
    "    answer = []\n",
    "    for i in my_string:\n",
    "        if not i in answer:\n",
    "            answer.append(i)\n",
    "    return ''.join(answer)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "9b73e344-5a5d-47c4-94d6-460bbaee46fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'We arthwold'"
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution('We are the world')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7736f67b-c6f7-4faa-90b3-c2db72e348c7",
   "metadata": {},
   "source": [
    "# [팩토리얼](https://school.programmers.co.kr/learn/courses/30/lessons/120848) \n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - factorial을 구현하는 가장 대표적인 것은 재귀함수이다.\n",
    "     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "824f733b-aa08-4946-88da-defa8555c50e",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "i! <= n 을 만족하는 최대 정수 i 값을 찾아라\n",
    "'''\n",
    "def solution(n):\n",
    "    for i in range(1,11):\n",
    "        fact = 1\n",
    "        for j in range(1, i+1): # factorial 계산\n",
    "            fact *= j\n",
    "        if fact > n: # 비교\n",
    "            return i-1\n",
    "        if fact == n:\n",
    "            return i\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "d82b931b-641d-4444-8f8e-e7d2c28ef1ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 마음에 드는 다른 사람의 답안\n",
    "def solution(n):\n",
    "    answer = 1\n",
    "    factorial = 1\n",
    "    while factorial <= n:\n",
    "        answer += 1\n",
    "        factorial = factorial * answer\n",
    "    answer -= 1\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa61da0a-7201-4f4a-9fd6-dabeb98e733c",
   "metadata": {},
   "source": [
    "# [A로 B만들기](https://school.programmers.co.kr/learn/courses/30/lessons/120886)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - before 에 있는 모든 문자가 after에 존재해야한다.\n",
    "     - sort 해서 비교"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2709282-eb57-458d-8d0e-6349893223a7",
   "metadata": {},
   "source": [
    "> .sort는 str에 사용할 수 없지만\n",
    "> sorted(list)는 사용할 수 있다\n",
    "```python\n",
    "\n",
    "def solution(before, after):\n",
    "    before=sorted(before)\n",
    "    after=sorted(after)\n",
    "    if before==after:\n",
    "        return 1\n",
    "    else:\n",
    "        return 0\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c96b904d-7c94-46f5-aa0b-6e633a0a95c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(before, after):\n",
    "    before = list(before)\n",
    "    after = list(after)\n",
    "    before.sort()\n",
    "    after.sort()\n",
    "    for idx in range(len(before)):\n",
    "        if before[idx] == after[idx]:\n",
    "            continue\n",
    "        elif before[idx] != after[idx]:\n",
    "            return 0\n",
    "    return 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d2f66b3-123f-4a21-a0c0-3750350e2443",
   "metadata": {},
   "source": [
    "# [모스부호(1)](https://school.programmers.co.kr/learn/courses/30/lessons/120838)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 모스 부호가 dic 형식으로 주어져있다.\n",
    "     - key 값을 입력받으면 value를 뱉어내는 dic의 성질을 이용하자\n",
    "     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "cdee0e7a-12e4-4e83-9ebd-d5531f333c5c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'n', 'd', 'g', 'de', 'f']"
      ]
     },
     "execution_count": 190,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 'a,n,d,g,de,f'\n",
    "al = a.split(',')\n",
    "al"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "098712a0-a3b9-49ce-8f2e-37828ca49014",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "받은 letter 의 모스부호를 알파벳으로 뱉어내자\n",
    "'''\n",
    "\n",
    "def solution(letter):\n",
    "    answer = ''\n",
    "    morse = { \n",
    "    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',\n",
    "    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',\n",
    "    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',\n",
    "    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',\n",
    "    '-.--':'y','--..':'z'}\n",
    "    letter = letter.split(' ')\n",
    "    for key_dix in letter:\n",
    "        answer += morse[key_dix]\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aec1b640-a6bf-485b-a006-f433299784cf",
   "metadata": {},
   "source": [
    "# [2차원으로 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/120842)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - numpy의 .reshape() 를 사용하면 편리하다.\n",
    "     - ndarray를 다시 list 화 `arr.tolist()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "id": "dcc88ec0-60e2-45c0-87fc-1d3dfed54377",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "num_list의 배열을 -1 by n 행렬로 변환하라\n",
    "'''\n",
    "def solution(num_list, n):\n",
    "    import numpy as np\n",
    "    num_list = np.array(num_list)\n",
    "    num_list = num_list.reshape(-1,n)\n",
    "    num_list = num_list.tolist()\n",
    "    return num_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "id": "9b046d19-6bd7-4ba1-ae75-63d680f7c0fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 2], [3, 4], [5, 6], [7, 8]]"
      ]
     },
     "execution_count": 203,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution([1,2,3,4,5,6,7,8],2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "id": "90426c02-46d6-4907-b2c4-02c7e23aad50",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 다른 사람의 풀이 numpy 이용 안하기\n",
    "def solution(num_list, n):\n",
    "    answer = []\n",
    "    for i in range(0, len(num_list), n):\n",
    "        answer.append(num_list[i:i+n])\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "030c7430-14c1-4691-be0a-60b7084c9da6",
   "metadata": {},
   "source": [
    "# [가까운 수](https://school.programmers.co.kr/learn/courses/30/lessons/120890)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 가장 가까운수를 찾아라 -> 두수의 절댓값 차가 가장 적은 숫자 찾기 \n",
    "     - sort 한 후 차이값을 apped하여 그 값이 가장 작은 값의 인덱스를 찾는다\n",
    "     - `.idex()`의 값은 같은 값이 있으면 앞쪽의 인덱스를 내어주기 때문"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c9867d7e-b612-4368-96c6-356dc95d9646",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 10개 중 2개만 맞음\n",
    "def solution(array, n):\n",
    "    d_min = 100\n",
    "    for idx in range(len(array)):\n",
    "        if abs(array[idx] - n) < d_min:\n",
    "            d_min = abs(array[idx] - n)\n",
    "            d_idx = idx\n",
    "        elif abs(array[idx] - n) == d_min:\n",
    "            if array[idx] < array[d_idx]:\n",
    "                return array[idx]\n",
    "            elif array[idx] > array[d_idx]:\n",
    "                return array[d_idx]\n",
    "    return array[d_idx]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "1f4db111-1f33-4817-986c-0c647a711ce4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(array, n):\n",
    "    result = []\n",
    "    array.sort()\n",
    "    for i in array:\n",
    "        result.append(abs(i-n))\n",
    "    idx = result.index(min(result))\n",
    "    return array[idx]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "0f544c42-846d-4cbf-b620-fa75f5382ded",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [3,7,5,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "50a7afa4-c007-4df1-b050-8098f4b44bc7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.index(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "d354278e-a071-4edf-bc60-35dd084f3811",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "17"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array = [3, 10, 28]\n",
    "abs(array[0] - 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "72ea228d-c638-4195-ace2-e13b292157d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution([10, 11, 12], 13)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d26b82f1-653e-4d4c-a481-e7247084b7e1",
   "metadata": {},
   "source": [
    "# [K의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/120887)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 입력받은 숫자를 str list로 저장 각 항목을 뽑아서 1의 개수를 카운딩\n",
    "     - `count()` 문자열에서 해당 문자의 개수를 찾는 method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "281d082d-f5a8-44d7-a723-0e2f39258eca",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(i, j, k):\n",
    "    numbers = [str(n) for n in range(i,j+1)]\n",
    "    cnt = 0\n",
    "    for num in numbers:\n",
    "        cnt += num.count(str(k))\n",
    "    return cnt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3a08f3ee-197e-4f99-921f-a4312d10ec51",
   "metadata": {},
   "source": [
    "# [진료 순서 정하기](https://school.programmers.co.kr/learn/courses/30/lessons/120835)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 정렬된 숫자의 각 인덱스를 찾아가는 방식\n",
    "     - `.index()` 를 이용하자!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "c59d2414-3d52-46a1-86ea-27b15493e369",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(emergency):\n",
    "    sort_em = sorted(emergency, reverse=True)\n",
    "    # 즉 정렬된 값의 인덱스를, 원래 배열의 순서대로 출력\n",
    "    answer = [sort_em.index(num)+1 for num in emergency]\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "96cb181e-3848-45f6-af7a-09dee20fcaf8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 3, 5, 1]"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution([30,10,23,6,100])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f9186483-66a0-49f9-b5ab-ff9e0c0470b3",
   "metadata": {},
   "source": [
    "# [한 번만 등장한 문자](https://school.programmers.co.kr/learn/courses/30/lessons/120896)\n",
    " - Lv.0 python3\n",
    " - idea\n",
    "     - count == 1 값 찾기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "202a379d-63cd-489f-b413-9dc427cec3a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "한번만 등장한 문자 찾기\n",
    "'''\n",
    "def solution(s):\n",
    "    answer = sorted([i for i in s if s.count(i)==1])\n",
    "    return ''.join(answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "a0678b2c-dc2f-487c-8745-14242abd228e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'eho'"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution(\"hello\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02fe9478-7855-4da8-9f02-feb74aa47c3e",
   "metadata": {},
   "source": [
    "# [7의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/120912)\n",
    " - Lv0, python3\n",
    " - idea \n",
    "     - 7이 몇개? -> count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "9c206ab7-8889-4921-b7cb-b88976d9a9a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(array):\n",
    "    answer = sum([str(num).count('7') for num in array])\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f14b31ca-1140-4f1f-a74e-81d0ecce8adc",
   "metadata": {},
   "source": [
    "str(array) 하면?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "87053c17-5733-4c8d-a68a-e2d3577371ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str([1,25,34,55, 34, 65,23,65,987, 345]).count('5')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1947e20-45c3-473e-aa5a-e73a4a5827a1",
   "metadata": {},
   "source": [
    "# [이진수 더하기](https://school.programmers.co.kr/learn/challenges/beginner?order=acceptance_desc&page=1&statuses=unsolved&languages=python3)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 2진수 -> bin 이용하여 숫자만 나타내기 `bin(21)[2:]` : str로 나타내짐\n",
    "     - 2진수를 -> 정수로 구하는 방법"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d7d580b-bc2a-4ace-9a2e-0db65875c372",
   "metadata": {},
   "source": [
    " - str : 10110 와 같은 숫자를 2진수로 나타내는 방법\n",
    " `int('101',2)`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "bebce5e2-e042-4edf-ae3c-666b77821d8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1010100'"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bin(int('1010100',2))[2:]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d7dad50-24f0-4e18-8ba8-c7823f84ea79",
   "metadata": {},
   "source": [
    "https://itholic.github.io/python-reverse-reversed/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "3099965c-9c8f-4153-aa34-71d30e05110c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(bin1, bin2):\n",
    "    \n",
    "    a = list(reversed(str(bin1)))\n",
    "    b = list(reversed(str(bin2)))\n",
    "\n",
    "\n",
    "    intger1 = sum([ (int(a[idx]))*(2**idx) for idx in range(len(a))])\n",
    "    intger2 = sum([ (int(b[idx]))*(2**idx) for idx in range(len(b))])\n",
    "\n",
    "    result = intger1 + intger2\n",
    "    return str(bin(result))[2:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "d488e242-04ef-4006-bf54-821739675eb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "bin1 = 1001 # 1*2^0 + 0*2^1 + 0*2^2 + 1*2^3\n",
    "bin2 = 1111"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "c0100882-e993-4b54-bd4a-9038ae782589",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11000\n"
     ]
    }
   ],
   "source": [
    "a = list(reversed(str(bin1)))\n",
    "b = list(reversed(str(bin2)))\n",
    "\n",
    "\n",
    "intger1 = sum([ (int(a[idx]))*(2**idx) for idx in range(len(a))])\n",
    "intger2 = sum([ (int(b[idx]))*(2**idx) for idx in range(len(b))])\n",
    "\n",
    "result = intger1 + intger2\n",
    "print(str(bin(result))[2:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "b9b421e1-9d42-46a1-81e8-4d724f079b79",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def solution(bin1, bin2):\n",
    "    answer = bin(int(bin1,2) + int(bin2,2))[2:]\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c4160cec-d7cf-43b5-854e-fcd5ad9b413f",
   "metadata": {},
   "source": [
    "# [숨어있는 숫자의 덧셈(2)](https://school.programmers.co.kr/learn/courses/30/lessons/120864)\n",
    " - Lv0, python3\n",
    " - idea\n",
    "     - 숫자만 뽑아내자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "11f1c9c7-51ea-44dd-81c2-e477eadc4c74",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "My_string 안의 자연수들의 합을 return 하라 다만, 연속된 숫자의 경우 a34b32c 이면\n",
    "34+32 이다\n",
    "'''\n",
    "\n",
    "def solution(my_string):\n",
    "    answer=0\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "df015833-7c4f-4878-97ab-63ea5c140795",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution(\"1a2b3c4d123Z\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d3e9d92-7ec2-4e0e-ad59-52a7eb88f498",
   "metadata": {},
   "source": [
    "# [공 던지기](https://school.programmers.co.kr/learn/courses/30/lessons/120843)\n",
    " - Lv0, python3\n",
    " - idea "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "dcbe8efd-1203-461d-ad18-9c4f544575bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(numbers, k):\n",
    "    return numbers[2 * (k - 1) % len(numbers)]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "160fcd0c-5f91-4f62-8da0-c21292a219bd",
   "metadata": {},
   "source": [
    "# [소인수분해](https://school.programmers.co.kr/learn/courses/30/lessons/120852)\n",
    "- Lv 0, python3\n",
    "- idea\n",
    "    - 소인수 분해 -> 소수로 분해\n",
    "    - 1. 소수를 먼저 찾고\n",
    "```python\n",
    "# 12로 연습하자\n",
    "\n",
    "약수의 개수가 2인 수\n",
    "for i in range(1,13):\n",
    "    i의 약수 = [j for j in range(1,i+1) if i%j==0]\n",
    "    if len(i의 약수) == 2:\n",
    "        소수.append(i)\n",
    "answer = [i for i in 소수 if 12%i==0]\n",
    "        \n",
    "```\n",
    "    - 2. 나누어지는 소수를 구하자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d5adcb7-4475-449e-b2e0-0f7b39557a4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(n):\n",
    "    prime_number = []\n",
    "    for i in range(1, n+1):\n",
    "        divisor = [j for j in range(1,i+1) if i%j==0]\n",
    "        if len(divisor) == 2:\n",
    "            prime_number.append(i)\n",
    "    answer = [i for i in prime_number if n%i == 0]\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b66315c3-b506-4beb-b5f8-25f4ba01f290",
   "metadata": {},
   "source": [
    "# [영어가 싫어요](https://school.programmers.co.kr/learn/courses/30/lessons/120894)\n",
    "- Lv 0, python3\n",
    "- idea"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "06facb4a-38d5-49ad-b0c8-a7c142036409",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "영어로 표기된 문자를 숫자 바꾸려고 한다.\n",
    "매개변수는 공백없이 조합 ( zero~nine)\n",
    "e_nums = [\"zero\", \"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"]\n",
    "integers = [0,1,2,3,4,5,6,7,8,9]\n",
    "num_dic ={}\n",
    "for k, v in set(e_num, numbers):\n",
    "    num_dic[k] = v\n",
    "for e_num in e_nums:\n",
    "    numbers.replace(e_num,num_dic[e_num]\n",
    "'''\n",
    "def solution(numbers):\n",
    "    e_nums = [\"zero\", \"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"]\n",
    "    intger = '0123456789'\n",
    "    num_dic ={}\n",
    "    for k, v in zip(e_nums, intger):\n",
    "        num_dic[k] = v\n",
    "    for e_num in e_nums:\n",
    "        numbers = numbers.replace(e_num,num_dic[e_num])\n",
    "    return numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "fe42636e-535d-4d80-850f-4db3091f1aa7",
   "metadata": {},
   "outputs": [],
   "source": [
    "e_nums = [\"zero\", \"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"]\n",
    "intger = '0123456789'\n",
    "num_dic ={}\n",
    "for k, v in zip(e_nums, intger):\n",
    "    num_dic[k] = v"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bac8a284-8755-4aa8-8954-a3cda795c346",
   "metadata": {},
   "source": [
    "# [잘라서 배열로 저장하기](https://school.programmers.co.kr/learn/courses/30/lessons/120913)\n",
    " - Lv0 , python3\n",
    "``` \n",
    "my_str을 n 씩 잘라 저장한 배열을 retrun\n",
    "whlie k+n < len(my_str)    \n",
    "    k = 0\n",
    "    answer.append(my_str[k:k+n])\n",
    "    k += n\n",
    "    k+n > 길이보다 길면...\n",
    "    answer.append(my_str[k:]\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "0c58b297-eb77-4590-b91b-36e8bf4f030d",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def solution(my_str, n):\n",
    "    return [my_str[i: i + n] for i in range(0, len(my_str), n)]\n",
    "# 아 맞아 step... "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "26aab1d2-4059-42d3-82f3-870ff3409570",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solution(my_str, n):  # 16, 6\n",
    "    answer = []\n",
    "    k = 0\n",
    "    while k+n < len(my_str):\n",
    "        if k+n < len(my_str):\n",
    "            answer.append(my_str[k:k+n])\n",
    "            k += n\n",
    "\n",
    "    answer.append(my_str[k:])\n",
    "    return answer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "9de2689e-a406-4be1-9dd8-d2364f37afea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['abc1Ad', 'dfggg4', '556b']"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "solution(\"abc1Addfggg4556b\",6)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
