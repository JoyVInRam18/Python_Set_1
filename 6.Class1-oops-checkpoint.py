{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7bc4ed37-04cc-42e5-ae8b-00f20c46ae3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the age: 23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adult\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"Enter the age:\"))\n",
    "agecate=AgeCategory()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "aeee637c-bd93-4528-bf58-ad5398b4f592",
   "metadata": {},
   "outputs": [],
   "source": [
    "def AgeCategory():\n",
    "    if(age<18):\n",
    "        print(\"Children\")\n",
    "        cate=\"Children\"\n",
    "    elif(age<35):\n",
    "        print(\"Adult\")\n",
    "        cate=\"Adult\"\n",
    "    elif(age<59):\n",
    "        print(\"Citizen\")\n",
    "        cate=\"Citizen\"\n",
    "    else:\n",
    "        print(\"Senior Citizen\")\n",
    "        cate=\"Senior Citizen\"\n",
    "    return cate  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f6f8873f-3b32-4c57-aed6-a53d1366eec3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adult\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Adult'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "AgeCategory()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1cc56e01-693f-4ad5-9870-a38f77512f38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the age: 56\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Citizen\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"Enter the age:\"))\n",
    "agecate=AgeCategory()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "34a026db-d82f-497a-9898-0a386e78bb06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Citizen\n"
     ]
    }
   ],
   "source": [
    "print(agecate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "3068a7fb-a852-4d88-a17b-e10c04de3d6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def AgeCategoryNoR():\n",
    "    if(age<18):\n",
    "        print(\"Children\")\n",
    "        cate=\"Children\"\n",
    "    elif(age<35):\n",
    "        print(\"Adult\")\n",
    "        cate=\"Adult\"\n",
    "    elif(age<59):\n",
    "        print(\"Citizen\")\n",
    "        cate=\"Citizen\"\n",
    "    else:\n",
    "        print(\"Senior Citizen\")\n",
    "        cate=\"Senior Citizen\"\n",
    "    #return cate  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "24b35240-a99c-48c6-9bb1-01515cd65fbc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the age: 44\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Citizen\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"Enter the age:\"))\n",
    "agecate=AgeCategoryNoR()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "87cf2467-bfdf-4432-a935-6c6c4d6eb089",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(agecate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "60d74bdd-7acc-4b7d-925e-9ec07f1de828",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the age: 23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adult\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"Enter the age:\"))\n",
    "agecate1=AgeCategory()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c09829d4-8415-4793-8f46-643d7d8180e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def oddEven():\n",
    "    num = int(input(\"Enter a number: \"))\n",
    "    if num % 2 == 0:\n",
    "        print(f\"{num} is Even\")\n",
    "        message=\"Even\"\n",
    "    else:\n",
    "        print(f\"{num} is Odd\")\n",
    "        message=\"Odd\"\n",
    "    return message   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d823cc06-a133-4e7c-bcc9-8e83c0852e8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 is Even\n"
     ]
    }
   ],
   "source": [
    "message=oddEven()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3fdd6945-b21a-400d-abb1-ac32cf6e5bcf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The given number is Even\n"
     ]
    }
   ],
   "source": [
    "if(message==\"Even\"):\n",
    "    print(\"The given number is Even\")\n",
    "else:\n",
    "    print(\"The given number is Odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "877ce8cb-8378-4447-94ab-831f97760670",
   "metadata": {},
   "outputs": [],
   "source": [
    "def BMI():\n",
    "    BMI=int(input(\"Enter the BMI Index:\"))\n",
    "    if(BMI<18.5):\n",
    "        print(\"UnderWeight\")\n",
    "        message=\"UnderWeight\"\n",
    "    elif(BMI<24.9):\n",
    "        print(\"Normal\")\n",
    "        message=\"Normal\"\n",
    "    elif(BMI<29.9):\n",
    "        print(\"OverWeight\")\n",
    "        message=\"OverWeight\"\n",
    "    else:\n",
    "        print(\"Very OverWeight\")\n",
    "        message=\"Very OverWeight\"\n",
    "    return message\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0e6a016d-7a1b-45fc-9bed-f3f76a7d82be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the BMI Index: 35\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Very OverWeight\n"
     ]
    }
   ],
   "source": [
    "bmi=BMI()  #Non parameterised function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b3c9321f-b7fa-49b0-bca1-3aa36efce319",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Very OverWeight'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bmi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "eb96321a-7a76-438c-b407-638ca98d4638",
   "metadata": {},
   "outputs": [],
   "source": [
    "def addition(num1,num2):\n",
    "    add=num1+num2\n",
    "    return add"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "527611fa-69aa-4b01-817e-2938ad729bc2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "addition(5,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "af680e07-9785-40a8-adae-ae2d521353dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def sub(num1,num2):\n",
    "    sub=num1-num2\n",
    "    return sub"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9298d6b8-9f01-4b2a-aeed-6e26cc5a27bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sub(2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "9b86545b-b0a8-45f0-9c43-dcac3c9934a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "class multipleFunctions():\n",
    "    def oddEven():\n",
    "        num = int(input(\"Enter a number: \"))\n",
    "        if num % 2 == 0:\n",
    "            print(f\"{num} is Even\")\n",
    "            message=\"Even\"\n",
    "        else:\n",
    "            print(f\"{num} is Odd\")\n",
    "            message=\"Odd\"\n",
    "        return message \n",
    "    def BMI():\n",
    "            BMI=int(input(\"Enter the BMI Index:\"))\n",
    "            if(BMI<18.5):\n",
    "                print(\"UnderWeight\")\n",
    "                message=\"UnderWeight\"\n",
    "            elif(BMI<24.9):\n",
    "                print(\"Normal\")\n",
    "                message=\"Normal\"\n",
    "            elif(BMI<29.9):\n",
    "                print(\"OverWeight\")\n",
    "                message=\"OverWeight\"\n",
    "            else:\n",
    "                print(\"Very OverWeight\")\n",
    "                message=\"Very OverWeight\"\n",
    "            return message\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "1ce920d2-9ef0-4908-8021-af44068195cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the BMI Index: 45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Very OverWeight\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Very OverWeight'"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multipleFunctions.BMI()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "afe338c8-b44e-418c-81af-20a0a345cb60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23 is Odd\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Odd'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multipleFunctions.oddEven()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1621c9c-8327-4b87-82c9-bf4b40c60c10",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
